import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Hypothesis hyp = new Hypothesis(0.1, 0.1);
        PerformanceSys.trainHumanTeacher(hyp, sc);
        sc.close();
    }
}
