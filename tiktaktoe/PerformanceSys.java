import java.util.Scanner;
import java.util.Random;

public class PerformanceSys {
    public static Experiment trainHumanTeacher(Hypothesis hyp, Scanner sc) {
        Random rnd = new Random();
        Experiment exp = new Experiment(rnd.nextInt(2) == 0 ? 'X' : 'O');

        System.out.println("You will be O.");
        System.out.println("Player " + exp.nextPlayer() + " will go first.");

        while (!exp.gameIsOver()) {
            if (exp.nextPlayer() == 'X')
                PerformanceSys.cpuMove(exp, hyp);
            else
                PerformanceSys.cpuMove(exp, hyp);
                // PerformanceSys.humanMove(exp, hyp, sc);

            System.out.println(exp.getBoardString());
        }

        System.out.println();
        System.out.println("GAME OVER!");
        System.out.println("----------");
        System.out.println(exp.getBoardString());
        return null;
    }

    public static void cpuMove(Experiment exp, Hypothesis hyp) {
        int[][] legalMoves = exp.getLegalMoves();
        assert legalMoves.length > 0;

        int bestMove = 0;
        double bestScore = Double.NEGATIVE_INFINITY;
        for (int i = 0; i < legalMoves.length; i++) {
            // Make copy of board state
            var state = exp.cloneBoardState();
            state[legalMoves[i][0]][legalMoves[i][1]] = 'X';

            // Calculate score
            double score = hyp.v_hat(state);
            if (score > bestScore) {
                bestMove = i;
                bestScore = score;
            }
        }

        exp.move(legalMoves[bestMove][0], legalMoves[bestMove][0]);
    }

    public static void humanMove(Experiment exp, Hypothesis hyp, Scanner sc) {
        System.out.println(exp.getBoardString());
        System.out.println("--------");
        System.out.println("Enter your move in the form of 'x y':");

        while (true) {
            int i = sc.nextInt();
            int j = sc.nextInt();
            
            if (exp.board[i][j] == ' ') {
                exp.move(i, j);
                break;
            }

            System.out.println("That square is occupied. Choose another:");
        }
    }
}

