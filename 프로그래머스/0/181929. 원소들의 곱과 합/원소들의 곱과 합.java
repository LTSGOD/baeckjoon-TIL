class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        int multiply = 1;
        int sum = 0;
        
        for (int i = 0; i < num_list.length; i++) {
            multiply *= num_list[i];
            sum += num_list[i];
        }
        
        
        // System.out.println(multiply);
        // System.out.println(sum);
        
        if (multiply < sum * sum) {
            answer = 1;
        } else {
            answer = 0;
        }
        
        
        return answer;
    }
}