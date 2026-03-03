class DecisionTree {

    // Simple dataset
    static int[][] X = {
            {1, 1},
            {1, 0},
            {0, 1},
            {0, 0}
    };

    static int[] y = {1, 1, 0, 0}; // Labels

    public static void main(String[] args) {
        buildTree();
    }

    static void buildTree() {
        int featureIndex = 0; // Split using first feature

        System.out.println("Decision Tree:");
        System.out.println("If Feature[" + featureIndex + "] == 1 -> Class 1");
        System.out.println("Else -> Class 0");
    }
}