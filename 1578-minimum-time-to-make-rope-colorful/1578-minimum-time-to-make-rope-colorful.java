class Solution {
    public int minCost(String colors, int[] neededTime) {
        int n = neededTime.length;
        int i = 0;
        int totalTime = 0;
        
        while (i < n) {
            int mx = 0;
            int sm = 0;
            int j = i;
            for (; j < n; j++) {
                if (colors.charAt(j) != colors.charAt(i)) {
                    i = j;
                    break;
                }
                
                sm += neededTime[j];
                if (neededTime[j] > mx) {
                    mx = neededTime[j];
                }
            }
            
            totalTime += sm - mx;
            
            if (j == n) {
                break;
            }
        }
        
        return totalTime;
    }
}