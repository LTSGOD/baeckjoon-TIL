import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        int odd = Integer.parseInt(
            Arrays.stream(num_list).filter(value -> value % 2 != 0).mapToObj(Integer::toString).collect(Collectors.joining())
        );
        
        int even = Integer.parseInt(Arrays.stream(num_list).filter(value->value%2 == 0).mapToObj(Integer::toString).collect(Collectors.joining()));
         
        answer = even + odd;
        
        return answer;
    }
}