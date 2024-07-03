import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = {};
        int last_num = num_list[num_list.length - 1];
        int previous_num = num_list[num_list.length - 2];
        
        answer = Arrays.copyOf(num_list, num_list.length + 1);
        
        if (last_num > previous_num) {
            answer[answer.length - 1] = last_num - previous_num;
        } else {
            answer[answer.length - 1] = last_num * 2;
        }
        
        return answer;
    }
}