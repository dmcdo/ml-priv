import java.util.ArrayList;

public class Experiment {
    public char[][] board;
    public char startingPlayer;
    public ArrayList<int[]> moveHist;

    public Experiment(char startingPlayer) {
        assert startingPlayer == 'X' || startingPlayer == 'O';

        this.moveHist = new ArrayList<>();
        this.startingPlayer = startingPlayer;
        this.board = new char[][] {
            {' ', ' ', ' '},
            {' ', ' ', ' '},
            {' ', ' ', ' '}
        };
    }

    public void move(int i, int j) {
        assert board[i][j] == ' ';
        assert !gameIsOver();

        board[i][j] = nextPlayer();
        moveHist.add(new int[] {i, j});
    }

    public char nextPlayer() {
        if (moveHist.size() % 2 == 0)
            return startingPlayer == 'X' ? 'X' : 'O';
        else
            return startingPlayer == 'X' ? 'O' : 'X';
    }

    public boolean gameIsOver() {
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
            if (board[line[0][0]][line[0][1]] == board[line[1][0]][line[1][1]] &&
                board[line[1][0]][line[1][1]] == board[line[2][0]][line[2][1]] &&
                board[line[2][0]][line[2][1]] != ' ')
                return true;

        // Check if there are any empty spaces.
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (board[i][j] == ' ')
                    return false;

        // The game has ended in a tie.
        return true;
    }

    public int[][] getLegalMoves() {
        ArrayList<int[]> empty = new ArrayList<>();

        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (board[i][j] == ' ')
                    empty.add(new int[] {i, j});

        return (int[][])empty.toArray();
    }

    public String getBoardString() {
        return String.format(
            " |0|1|2\n" +
            "0|%c|%c|%c\n" +
            "1|%c|%c|%c\n" +
            "2|%c|%c|%c\n",
            board[0][0],
            board[1][0],
            board[2][0],
            board[0][1],
            board[1][1],
            board[2][1],
            board[0][2],
            board[1][2],
            board[2][2]
        );
    }
}