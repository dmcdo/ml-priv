import java.util.ArrayList;

public class Generalizer {
    public static Hypothesis generalize(Hypothesis hyp, ArrayList<Criticism> crits) {
        double learnRate = hyp.learnRate;
        double zerothweight = hyp.zerothweight;
        double[] weights = hyp.weights.clone();

        for (Criticism crit : crits) {
            weights[0] = weights[0] + learnRate * (crit.v_train() - hyp.v_hat(crit.state())) * crit.fvals()[0];
            weights[1] = weights[1] + learnRate * (crit.v_train() - hyp.v_hat(crit.state())) * crit.fvals()[1];
            weights[2] = weights[2] + learnRate * (crit.v_train() - hyp.v_hat(crit.state())) * crit.fvals()[2];
            weights[3] = weights[3] + learnRate * (crit.v_train() - hyp.v_hat(crit.state())) * crit.fvals()[3];
            weights[4] = weights[4] + learnRate * (crit.v_train() - hyp.v_hat(crit.state())) * crit.fvals()[4];
            weights[5] = weights[5] + learnRate * (crit.v_train() - hyp.v_hat(crit.state())) * crit.fvals()[5];
            weights[6] = weights[6] + learnRate * (crit.v_train() - hyp.v_hat(crit.state())) * crit.fvals()[6];

            double avgfval = (double)(crit.fvals()[0] +
                                      crit.fvals()[1] +
                                      crit.fvals()[2] +
                                      crit.fvals()[3] +
                                      crit.fvals()[4]) / 5.0; // Ignore 6 and 7 they're bad.
            zerothweight = zerothweight + learnRate * (crit.v_train() - hyp.v_hat(crit.state())) * avgfval;
        }

        return new Hypothesis(
            learnRate,
            zerothweight,
            weights[0],
            weights[1],
            weights[2],
            weights[3],
            weights[4],
            weights[5],
            weights[6]
        );
    }
}
