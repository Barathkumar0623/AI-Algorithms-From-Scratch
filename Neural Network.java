class NeuralNetwork {

    static double weight = 0.5;
    static double bias = 0.1;
    static double learningRate = 0.1;

    static double[] X = {0, 1};
    static double[] Y = {0, 1};

    public static void main(String[] args) {

        for (int epoch = 0; epoch < 1000; epoch++) {

            for (int i = 0; i < X.length; i++) {

                double output = sigmoid(X[i] * weight + bias);
                double error = Y[i] - output;

                // Gradient update
                weight += learningRate * error * X[i];
                bias += learningRate * error;
            }
        }

        System.out.println("Trained Weight: " + weight);
        System.out.println("Trained Bias: " + bias);
    }

    static double sigmoid(double x) {
        return 1 / (1 + Math.exp(-x));
    }
}