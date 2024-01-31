import java.util.Scanner;
import java.util.Random;

public class PerformanceSys {
    public static Experiment trainAgainstSelf(Hypothesis hyp) {
        Random rnd = new Random();
        Experiment exp = new Experiment(rnd.nextInt(2) == 0 ? 'X' : 'O');

        while (exp.getWinner() == null) {
            if (exp.nextPlayer() == 'X') {
                int[] move = PerformanceSys.cpuMove(exp.state, hyp);
                exp.move(move[0], move[1]);
            }
            else {
                // Invert board for opponent
                char[][] state = exp.cloneState();
                for (int i = 0; i < 3; i++)
                    for (int j = 0; j < 3; j++)
                        if (state[i][j] == 'X')
                            state[i][j] = 'O';
                        else if (state[i][j] == 'O')
                            state[i][j] = 'X';

                int[] move = PerformanceSys.cpuMove(exp.state, hyp);
                exp.move(move[0], move[1]);
            }
        }

        return exp;
    }

    public static Experiment trainHumanTeacher(Hypothesis hyp, Scanner sc) {
        Experiment exp;

        System.out.println("You will be O.");
        System.out.println("Would you like to go first? Y/N:");
        String ans = sc.nextLine();
        if (ans.length() > 0 && ans.toUpperCase().equals("Y"))
            exp = new Experiment('O');
        else
            exp =new Experiment('X');

        System.out.println("Player " + exp.nextPlayer() + " will go first.");
        System.out.println();

        while (exp.getWinner() == null) {
            if (exp.nextPlayer() == 'X') {
                int[] move = PerformanceSys.cpuMove(exp.state, hyp);
                exp.move(move[0], move[1]);
            }
            else {
                int[] move = PerformanceSys.humanMove(exp.state, hyp, sc);
                exp.move(move[0], move[1]);
            }
        }

        System.out.println();
        System.out.println("GAME OVER!");
        System.out.println("----------");
        System.out.println(exp.getStateString());
        return exp;
    }

    public static int[] cpuMove(char[][] state, Hypothesis hyp) {
        var legalMoves = Experiment.getLegalMoves(state);
        assert legalMoves.size() > 0;

        int bestMove = 0;
        double bestScore = Double.NEGATIVE_INFINITY;
        for (int i = 0; i < legalMoves.size(); i++) {
            // Make copy of board state
            var newstate = Experiment.cloneState(state);
            newstate[legalMoves.get(i)[0]][legalMoves.get(i)[1]] = 'X';

            // Calculate score
            double score = hyp.v_hat(newstate);
            if (score > bestScore) {
                bestMove = i;
                bestScore = score;
            }
        }

        return new int[] {legalMoves.get(bestMove)[0], legalMoves.get(bestMove)[1]};
    }

    public static int[] humanMove(char[][] state, Hypothesis hyp, Scanner sc) {
        System.out.println("It's your turn.");
        System.out.println(Experiment.getStateString(state));
        System.out.println("--------");
        System.out.println("Enter your move in the form of 'x y':");

        int i, j;
        while (true) {
            i = sc.nextInt();
            j = sc.nextInt();

            if (state[i][j] == ' ') {
                break;
            }
            System.out.println("That square is occupied. Choose another:");
        }

        System.out.println();
        return new int[] {i, j};
    }
}

