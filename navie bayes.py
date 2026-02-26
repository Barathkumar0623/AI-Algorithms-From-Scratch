# Naive Bayes from scratch (Categorical Data)

from collections import defaultdict

# Dataset
dataset = [
    ("Sunny", "Hot", "No"),
    ("Sunny", "Mild", "No"),
    ("Overcast", "Hot", "Yes"),
    ("Rainy", "Cool", "Yes"),
    ("Rainy", "Mild", "Yes"),
    ("Sunny", "Cool", "No")
]

def train_naive_bayes(data):
    total = len(data)
    
    class_counts = defaultdict(int)
    feature_counts = defaultdict(lambda: defaultdict(int))
    
    for outlook, temp, label in data:
        class_counts[label] += 1
        feature_counts[label]["outlook_" + outlook] += 1
        feature_counts[label]["temp_" + temp] += 1
    
    return total, class_counts, feature_counts

def predict(sample, total, class_counts, feature_counts):
    outlook, temp = sample
    probabilities = {}
    
    for label in class_counts:
        prior = class_counts[label] / total
        
        outlook_prob = feature_counts[label]["outlook_" + outlook] / class_counts[label]
        temp_prob = feature_counts[label]["temp_" + temp] / class_counts[label]
        
        probabilities[label] = prior * outlook_prob * temp_prob
    
    return max(probabilities, key=probabilities.get)

# Train model
total, class_counts, feature_counts = train_naive_bayes(dataset)

# Predict
sample = ("Sunny", "Cool")
result = predict(sample, total, class_counts, feature_counts)

print("Prediction:", result)