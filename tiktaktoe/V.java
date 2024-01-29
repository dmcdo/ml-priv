public class V {
    public static final int E = 0;
    public static final int X = 1;
    public static final int O = 2;
    public static final int[][][] lines = {
        {{0, 0}, {1, 0}, {2, 0}},
        {{0, 1}, {1, 1}, {2, 1}},
        {{0, 2}, {1, 2}, {2, 2}},
        {{0, 0}, {0, 1}, {0, 2}},
        {{1, 0}, {1, 1}, {1, 2}},
        {{2, 0}, {2, 1}, {2, 2}},
        {{0, 0}, {1, 1}, {2, 2}},
        {{2, 0}, {1, 1}, {0, 2}}
    };

    public static int[] getFeatureValues(int[][] board) {
        // X in 2, X in 1, X in 0, O in 2, O in 1, O in 0
        int[] analysis = new int[] {0, 0, 0, 0, 0, 0};

        for (int[][] line : lines) {
            int xs = 0;
            int os = 0;
            for (int[] pos : line)
                if (board[pos[0]][pos[1]] == X)
                    xs++;
                else if (board[pos[0]][pos[1]] == O)
                    os++;

            if (xs > 0 && os > 0)
                continue;
            else if (xs == 1)
                analysis[0]++;
            else if (xs == 2)
                analysis[1]++;
            else if (xs == 3)
                analysis[2]++;
            else if (os == 1)
                analysis[3]++;
            else if (os == 2)
                analysis[4]++;
            else if (os == 3)
                analysis[5]++;
        }

        return analysis;
    }

    public static void main(String[] args) {
        var x = analyze(new int[][] {{X, X, O}, {O, X, O}, {E, E, O}});

        for (int i : x)
            System.out.println(i);
    }
}