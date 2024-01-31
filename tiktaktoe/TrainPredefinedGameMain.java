import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;

public class TrainPredefinedGameMain {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        System.out.println("Loading stored weights.");
        File weightsfile = new File("weights.txt");
        Scanner weightsreader = new Scanner(weightsfile);
        double w0 = weightsreader.nextDouble();
        double w1 = weightsreader.nextDouble();
        double w2 = weightsreader.nextDouble();
        double w3 = weightsreader.nextDouble();
        double w4 = weightsreader.nextDouble();
        double w5 = weightsreader.nextDouble();
        double w6 = weightsreader.nextDouble();
        double w7 = weightsreader.nextDouble();
        weightsreader.close();

        Hypothesis hyp = new Hypothesis(0.01, w0, w1, w2, w3, w4, w5, w6, w7);
        System.out.println("The algorithm will be trained on the games supplied to stdin.");
        System.out.println("See the README.TXT for more details.");

        Scanner sc = new Scanner(System.in);
        int games = sc.nextInt();
        int xwins = 0;
        int owins = 0;
        int ties = 0;
        for (int i = 0; i < games; i++) {
            char startingplayer = sc.next().charAt(0);
            ArrayList<int[]> moves = new ArrayList<>();
            while (true) {
                int x = sc.nextInt();
                int y = sc.nextInt();

                if (x == -1)
                    break;
                else
                    moves.add(new int[] {x, y});
            }

            var exp = PerformanceSys.trainAgainstPredefinedGame(hyp, startingplayer, moves);
            if (exp == null)
                continue;

            switch ((char)exp.getWinner()) {
                case 'X':
                    xwins++;
                    break;
                case 'O':
                    owins++;
                    break;
                case 'T':
                    ties++;
                    break;
                default:
                    throw new RuntimeException("Logic Error");
            }

            var crits = Criticism.criticize(hyp, exp);
            hyp = Generalizer.generalize(hyp, crits);
        }

        sc.close();
        System.out.println("Done.");
        System.out.println("Won " + xwins + " times. Lost " + owins + " times. Tied " + ties + " times.");
        System.out.println("New weights: " + hyp.toString());
        System.out.println("Writing weights to weights.txt");
        FileWriter weightswriter = new FileWriter(weightsfile);
        weightswriter.write(hyp.toString());
        weightswriter.close();
    }
}
