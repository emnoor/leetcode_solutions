class Solution {
    public int numSpecial(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[] mc = new int[m];
        int[] nc = new int[n];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                mc[i] += mat[i][j];
                nc[j] += mat[i][j];
            }
        }
        
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1 && mc[i] == 1 && nc[j] == 1) {
                    count += 1;
                }
            }
        }
        
        return count;
    }
}