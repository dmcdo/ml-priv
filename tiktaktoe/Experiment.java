import java.util.ArrayList;

public class Experiment {
    public char[][] state;
    public char startingPlayer;
    public ArrayList<char[][]> trace;
    public ArrayList<double[]> tracefvals;

    public Experiment(char startingPlayer) {
        assert startingPlayer == 'X' || startingPlayer == 'O';

        this.trace = new ArrayList<>();
        this.tracefvals = new ArrayList<>();
        this.startingPlayer = startingPlayer;
        this.state = new char[][] {
            {' ', ' ', ' '},
            {' ', ' ', ' '},
            {' ', ' ', ' '}
        };
    }

    public void move(int i, int j) {
        state[i][j] = nextPlayer();
        trace.add(cloneState());
        tracefvals.add(Hypothesis.getFeatureValues(state));
    }

    public char nextPlayer() {
        if (trace.size() % 2 == 0)
            return startingPlayer == 'X' ? 'X' : 'O';
        else
            return startingPlayer == 'X' ? 'O' : 'X';
    }

    public ArrayList<int[]> getLegalMoves() {
        return Experiment.getLegalMoves(state);
    }

    public Character getWinner() {
        return Experiment.getWinner(state);
    }

    public String getStateString() {
        return Experiment.getStateString(state);
    }

    public char[][] cloneState() {
        return Experiment.cloneState(state);
    }

    public static ArrayList<int[]> getLegalMoves(char[][] state) {
        ArrayList<int[]> empty = new ArrayList<>();

        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (state[i][j] == ' ')
                    empty.add(new int[] {i, j});

        return empty;
    }

    public static Character getWinner(char[][] state) {
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

        // Check if a player has won.
        for (int[][] line : lines)
            if (state[line[0][0]][line[0][1]] == state[line[1][0]][line[1][1]] &&
                state[line[1][0]][line[1][1]] == state[line[2][0]][line[2][1]] &&
                state[line[2][0]][line[2][1]] != ' ')
                return state[line[0][0]][line[0][1]];

        // Check if there are any empty spaces.
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (state[i][j] == ' ')
                    return null;

        // The game has ended in a tie.
        return 'T';
    }

    public static String getStateString(char[][] state) {
        return String.format(
            " |0|1|2\n" +
            "0|%c|%c|%c\n" +
            "1|%c|%c|%c\n" +
            "2|%c|%c|%c\n",
            state[0][0],
            state[1][0],
            state[2][0],
            state[0][1],
            state[1][1],
            state[2][1],
            state[0][2],
            state[1][2],
            state[2][2]
        );
    }

    public static char[][] cloneState(char[][] state) {
        char[][] clone = new char[3][3];
        clone[0] = state[0].clone();
        clone[1] = state[1].clone();
        clone[2] = state[2].clone();
        return clone;
    }
}