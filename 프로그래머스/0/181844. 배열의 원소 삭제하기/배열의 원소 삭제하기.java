import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        int[] answer = {};
        
        ArrayList<Integer> tmp = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            boolean isDelete = false;
            for (int j = 0; j < delete_list.length; j++) {
                if (arr[i] == delete_list[j]) {
                    isDelete  = true;
                    break;
                }
            }
            
            if (!isDelete) {
                tmp.add(arr[i]);
            }
        }
        

        answer = tmp.stream().mapToInt(Integer::valueOf).toArray();
        return answer;
    }
}