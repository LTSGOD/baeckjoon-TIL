import java.util.ArrayList;
import java.util.HashMap;
import java.util.Stack;

class Solution {
    
    public String [] names = new String[]{"A", "C", "F", "J", "M", "N", "R", "T"};
    public ArrayList<String> result = new ArrayList<String>();
    public boolean [] visited = new boolean[8];
    public int count;
    
    public void perm(String[] data, int depth){
        
        if (depth == 8) {
            HashMap<String, HashMap<String, Integer> > distance  = new HashMap<String, HashMap<String, Integer> >();
            
            //거리 해쉬맵사용해서 저장 n2 시간
            // write(distance);

            if (check(data)) {
                
                count ++;
            }
            
            return;
        }
        
        
        for (int i = 0; i < 8; i++) {
            
            if (visited[i]) {
                continue;
            }
            
            visited[i] = true;
            result.add(names[i]);
            perm(data, depth + 1);
            visited[i] = false;
            result.remove(result.size() - 1);
            
        }
        
        return ;
    }
    
    public boolean check(String[] data) {
        
        for (String cond : data) {
            
            int dist = Math.abs(result.indexOf(String.valueOf(cond.charAt(0))) -result.indexOf(String.valueOf(cond.charAt(2)))) - 1;
            
            if (cond.charAt(3) == '=') {
                
                if (dist != Character.getNumericValue(cond.charAt(4))) {
                    return false;
                }
            } else if (cond.charAt(3) == '>') {
                
                if (dist <= Character.getNumericValue(cond.charAt(4))) {
                    return false;
                }
            } else {
                
                if (dist >= Character.getNumericValue(cond.charAt(4))) {
                    return false;
                }
                
            }
        }
        
        return true;
    }
    
    
    public void write(HashMap<String, HashMap<String, Integer> > distance){
        
        for (int i = 0; i < 8; i++) {
            HashMap<String, Integer> tmp = new HashMap<String, Integer>();

            for (int j = 0; j < 8; j++) {
                
                tmp.put(result.get(j), Math.abs(j-i)-1);
            }
            distance.put(result.get(i), tmp);
        }
        
        
        return;
    }
    public int solution(int n, String[] data) {
        
        int answer;
        perm(data, 0);
        answer = count;
        return answer;
    }

}