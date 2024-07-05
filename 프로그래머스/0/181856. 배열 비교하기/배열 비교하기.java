import java.util.*;

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;
        
        int arr1Length = arr1.length;
        int arr2Length = arr2.length;
        
        int arr1Sum = Arrays.stream(arr1).reduce((acc, i) -> acc + i).getAsInt();
        int arr2Sum = Arrays.stream(arr2).reduce((acc, i) -> acc + i).getAsInt();
        
        if (arr1Length < arr2Length) {
            return -1;
        } else if (arr1Length > arr2Length) {
            return 1;
        } else {
            if (arr1Sum < arr2Sum) {
                return -1;
            } else if (arr1Sum > arr2Sum) {
                return 1;
            } else {
                return 0;
            }
        }
        
    }
}