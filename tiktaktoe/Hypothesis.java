public class Hypothesis {
    public double learnRate;
    public double zerothweight;
    public double[] weights;

    public Hypothesis(
        double learnRate,
        double w0,
        double w1,
        double w2,
        double w3,
        double w4,
        double w5,
        double w6,
        double w7
    ) {
        this.learnRate = learnRate;
        this.zerothweight = w0;
        this.weights = new double[] {w1, w2, w3, w4, w5, w6, w6};
    }

    public double v_hat(char[][] state) {
        double[] values = getFeatureValues(state);
        assert weights.length == values.length;

        double sum = zerothweight;
        for (int i = 0; i < weights.length; i++) {
            sum += weights[i] * values[i];
        }

        return sum;
    }

    public static double[] getFeatureValues(char[][] state) {
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

        // X in 2, X in 1, X in 0, O in 2, O in 1, O in 0, unoccupied squares
        double[] featurevals = new double[] {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};

        for (int[][] line : lines) {
            int xs = 0;
            int os = 0;
            for (int[] pos : line)
                if (state[pos[0]][pos[1]] == 'X')
                    xs++;
                else if (state[pos[0]][pos[1]] == 'O')
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

        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (state[i][j] == ' ')
                    featurevals[6]++;

        return featurevals;
    }

    public String toString() {
        return String.format(
            "%f %f %f %f %f %f %f %f",
            zerothweight,
            weights[0],
            weights[1],
            weights[2],
            weights[3],
            weights[4],
            weights[5],
            weights[6]
        );
    }
}
