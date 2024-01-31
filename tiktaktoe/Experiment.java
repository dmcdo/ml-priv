import java.util.ArrayList;

public class Experiment {
    public char[][] board;
    public char startingPlayer;
    public ArrayList<int[]> hist;

    public Experiment(char startingPlayer) {
        assert startingPlayer == 'X' || startingPlayer == 'O';

        this.hist = new ArrayList<>();
        this.startingPlayer = startingPlayer;
        this.board = new char[][] {
            {'\0', '\0', '\0'},
            {'\0', '\0', '\0'},
            {'\0', '\0', '\0'}
        };
    }

    public void move(int i, int j) {
        board[i][j] = nextPlayer();
        hist.add(new int[] {i, j});
    }

    public char nextPlayer() {
        if (hist.size() % 2 == 0)
            return startingPlayer == 'X' ? 'X' : 'O';
        else
            return startingPlayer == 'X' ? 'O' : 'X';
    }



    public static int[][] getEmptyCells(char[][] board) {
        ArrayList<int[]> empty = new ArrayList<>();

        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (board[i][j] == '\0')
                    empty.add(new int[] {i, j});

        return (int[][])empty.toArray();
    }
}