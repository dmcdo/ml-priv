public class Main {
    public static void main(String[] args) {
        Hypothesis hyp = new Hypothesis(0.1, 0.1);
        PerformanceSys.trainHumanTeacher(hyp, 'O');
    }
}
