class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        
        int count = 0;
        
        for (int i = 0 ; i < str2.length(); i++) {
            
            if (str1.charAt(count) != str2.charAt(i)) {
                count  = 0;
            }
            
            if (str1.charAt(count) == str2.charAt(i)) {
                count += 1;
            }
            
            if (count == str1.length()) {
                answer = 1;
                break;
            }
        }
        
        
        return answer;
    }
}