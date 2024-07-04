import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] num_list, int n) {
        int answer = 0;
        
        List<Integer> tmp = Arrays.stream(num_list).filter(v -> v == n).boxed().collect(Collectors.toList());

        if (tmp.isEmpty()) {
            answer = 0;
        } else  {
            answer =  1;
        }
        
        return answer;
    }
}