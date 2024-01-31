import java.util.Scanner;

public class PerformanceSys {
    public static Experiment trainHumanTeacher(Hypothesis hyp, char startingPlayer) {
        Scanner sc = new Scanner(System.in);
        Experiment exp = new Experiment(startingPlayer);

        System.out.println("You will be O.");
        System.out.println("Player " + exp.nextPlayer() + " will go first.");

        while (!exp.gameIsOver()) {
            if (exp.nextPlayer() == 'X' && false) {
                // TODO
            }
            else {
                System.out.println(exp.getBoardString());
                System.out.println("--------");
                System.out.println("Enter your move in the form of 'x y':");
                int i = sc.nextInt();
                int j = sc.nextInt();
                exp.move(i, j);
            }
        }

        sc.close();
        return null; // TODO
    }
}
