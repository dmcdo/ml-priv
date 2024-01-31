import java.util.Scanner;
import java.util.Random;

public class PerformanceSys {
    public static Experiment trainHumanTeacher(Hypothesis hyp, Scanner sc) {
        Random rnd = new Random();
        Experiment exp = new Experiment(rnd.nextInt(2) == 0 ? 'X' : 'O');

        System.out.println("You will be O.");
        System.out.println("Player " + exp.nextPlayer() + " will go first.");
        System.out.println();

        while (exp.getWinner() == null) {
            if (exp.nextPlayer() == 'X')
                PerformanceSys.cpuMove(exp, hyp);
            else
                PerformanceSys.cpuMove(exp, hyp);
                // PerformanceSys.humanMove(exp, hyp, sc);

            System.out.println(exp.getStateString());
        }

        System.out.println();
        System.out.println("GAME OVER!");
        System.out.println("----------");
        System.out.println(exp.getStateString());
        return exp;
    }

    public static void cpuMove(Experiment exp, Hypothesis hyp) {
        var legalMoves = exp.getLegalMoves();
        assert legalMoves.size() > 0;

        int bestMove = 0;
        double bestScore = Double.NEGATIVE_INFINITY;
        for (int i = 0; i < legalMoves.size(); i++) {
            // Make copy of board state
            var state = exp.cloneState();
            state[legalMoves.get(i)[0]][legalMoves.get(i)[1]] = 'X';

            // Calculate score
            double score = hyp.v_hat(state);
            if (score > bestScore) {
                bestMove = i;
                bestScore = score;
            }
        }

        exp.move(legalMoves.get(bestMove)[0], legalMoves.get(bestMove)[1]);
    }

    public static void humanMove(Experiment exp, Hypothesis hyp, Scanner sc) {
        System.out.println("It's your turn.");
        System.out.println(exp.getStateString());
        System.out.println("--------");
        System.out.println("Enter your move in the form of 'x y':");

        while (true) {
            int i = sc.nextInt();
            int j = sc.nextInt();

            if (exp.state[i][j] == ' ') {
                exp.move(i, j);
                break;
            }

            System.out.println("That square is occupied. Choose another:");
        }

        System.out.println();
    }
}

