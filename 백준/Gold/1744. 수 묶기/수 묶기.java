import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        ArrayList<Integer> minus = new ArrayList<>();
        List<Integer> plus = new ArrayList<>();


        for (int i = 0; i < N; i++) {
            int tmp = Integer.parseInt(br.readLine());
            if (tmp <= 0){
                minus.add(tmp);
            } else {
                plus.add(tmp);
            }
        }

        minus.sort(Comparator.naturalOrder());
        plus.sort(Comparator.reverseOrder());
        int result = 0;
        for (int i = 0; i < minus.size(); i+=2) {
            if (i == minus.size()-1) {
                result += minus.get(i);
            } else {
                result += (minus.get(i) * minus.get(i+1));
            }
        }

        for (int i = 0; i < plus.size(); i+=2) {
            if (i == plus.size() - 1) {
                result += plus.get(i);
            } else {
                int multi = plus.get(i) * plus.get(i+1);
                int sum = plus.get(i) + plus.get(i+1);
                int tmp = 0;
                if (multi > sum) {
                    tmp = multi;
                } else{
                    tmp = sum;
                }
                result += tmp;
            }
        }

        System.out.println(result);



        
    }
}
