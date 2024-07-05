import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        
        List<Integer> X = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0;  j < arr[i]; j++) {
                X.add(arr[i]);
            }
        }
        
        
        int[] answer = new int[X.size()];
        
        for (int i = 0; i < X.size(); i++) {
            answer[i] = X.get(i);
        }
        
        return answer;
    }
}