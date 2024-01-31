import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var hyp = new Hypothesis(0.001, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0, 0);

        while (true) {
        var exp = PerformanceSys.trainHumanTeacher(hyp, sc);
        var crits = Criticism.criticize(hyp, exp);

        hyp = Generalizer.generalize(hyp, crits);
        System.out.println(hyp);
        }

        // sc.close();
    }
}
