class EMAlgorithm {

    static double[] data = {1.0, 1.5, 2.0, 8.0, 9.0, 10.0};

    public static void main(String[] args) {

        double mean1 = 2;
        double mean2 = 9;

        for (int iter = 0; iter < 5; iter++) {

            double sum1 = 0, sum2 = 0;
            int count1 = 0, count2 = 0;

            for (double point : data) {

                if (Math.abs(point - mean1) < Math.abs(point - mean2)) {
                    sum1 += point;
                    count1++;
                } else {
                    sum2 += point;
                    count2++;
                }
            }

            mean1 = sum1 / count1;
            mean2 = sum2 / count2;
        }

        System.out.println("Cluster 1 Mean: " + mean1);
        System.out.println("Cluster 2 Mean: " + mean2);
    }
}