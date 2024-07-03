import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length + 1];
        
        for (int i = 0; i < num_list.length; i++) {
            answer[i] = num_list[i];
        }
        
        int last_num = num_list[num_list.length - 1];
        int previous_num = num_list[num_list.length - 2];
        
        if (last_num > previous_num) {
            answer[answer.length - 1] = last_num - previous_num;
        } else {
            answer[answer.length - 1] = last_num * 2;
        }
        
        return answer;
    }
}