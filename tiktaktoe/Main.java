import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var hyp = new Hypothesis(0.001, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0, 0);

        int xwins = 0;
        int xloss = 0;
        for (int i = 0; i < 10000; i++) {
            // var exp = PerformanceSys.trainHumanTeacher(hyp, sc);
            var exp = PerformanceSys.trainAgainstSelf(hyp);

            if (exp.getWinner() == 'X')
                xwins++;
            else
                xloss++;

            var crits = Criticism.criticize(hyp, exp);
            hyp = Generalizer.generalize(hyp, crits);
            System.out.println(">---------------------");
            System.out.println(exp.getStateString());
            System.out.println(hyp);
            System.err.println("X wins: " + xwins);
            System.out.println("X loss: " + xloss);
            System.out.println("X prct: " + (double)xwins / (double)(xwins + xloss));
            System.out.println("<---------------------");
            System.out.println();

        }

        PerformanceSys.trainHumanTeacher(hyp, sc);
        // sc.close();
    }
}
