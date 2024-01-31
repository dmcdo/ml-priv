public class Hypothesis {
    double learnRate;
    double zerothweight;
    double[] weights;

    public Hypothesis(double learnRate, double initialWeight) {
        this.learnRate = learnRate;
        this.weights = new double[] {
            initialWeight,
            initialWeight,
            initialWeight,
            initialWeight,
            initialWeight,
            initialWeight
        };
    }

    public double v_hat(char[][] board) {
        int[] values = getFeatureValues(board);
        assert weights.length == values.length;

        double sum = zerothweight;
        for (int i = 0; i < weights.length; i++) {
            sum += weights[i] * values[i];
        }

        return sum;
    }

    public static int[] getFeatureValues(char[][] board) {
        final int[][][] lines = {
            {{0, 0}, {1, 0}, {2, 0}},
            {{0, 1}, {1, 1}, {2, 1}},
            {{0, 2}, {1, 2}, {2, 2}},
            {{0, 0}, {0, 1}, {0, 2}},
            {{1, 0}, {1, 1}, {1, 2}},
            {{2, 0}, {2, 1}, {2, 2}},
            {{0, 0}, {1, 1}, {2, 2}},
            {{2, 0}, {1, 1}, {0, 2}}
        };

        // X in 2, X in 1, X in 0, O in 2, O in 1, O in 0
        int[] featurevals = new int[] {0, 0, 0, 0, 0, 0};

        for (int[][] line : lines) {
            int xs = 0;
            int os = 0;
            for (int[] pos : line)
                if (board[pos[0]][pos[1]] == 'X')
                    xs++;
                else if (board[pos[0]][pos[1]] == 'O')
                    os++;

            if (xs > 0 && os > 0)
                continue;
            else if (xs == 1)
                featurevals[0]++;
            else if (xs == 2)
                featurevals[1]++;
            else if (xs == 3)
                featurevals[2]++;
            else if (os == 1)
                featurevals[3]++;
            else if (os == 2)
                featurevals[4]++;
            else if (os == 3)
                featurevals[5]++;
        }

        return featurevals;
    }
}
