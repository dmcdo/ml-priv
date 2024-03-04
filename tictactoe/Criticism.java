import java.util.ArrayList;

public class Criticism {
    private char[][] _state;
    private double[] _fvals;
    private double _v_train;
    public char[][] state() { return _state; }
    public double[] fvals() { return _fvals; }
    public double v_train() { return _v_train; }
        public Criticism(char[][] _state, double[] _fvals, double _v_train) {
                this._state = _state;
                this._fvals = _fvals;
                this._v_train = _v_train;
        }

    public static ArrayList<Criticism> criticize(Hypothesis hyp, Experiment exp) {
        ArrayList<Criticism> criticisms = new ArrayList<>();

        for (int i = exp.startingPlayer == 'X' ? 0 : 1; i < exp.trace.size(); i += 2) {
            double v_train;
            if (i + 1 < exp.trace.size()) {
                v_train = hyp.v_hat(exp.trace.get(i + 1));
            }
            else {
                switch ((char)Experiment.getWinner(exp.trace.get(i))) {
                    case 'X':
                        v_train = 100.0;
                        break;
                    case 'O':
                    case 'T':
                        v_train = -100.0;
                        break;
                    default:
                        throw new RuntimeException("Logic Error");
                }
            }

            criticisms.add(
                new Criticism(
                    Experiment.cloneState(exp.trace.get(i)),
                    exp.tracefvals.get(i),
                    v_train
                )
            );
        }

        return criticisms;
    }
}
