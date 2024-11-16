import java.util.*;

public class JobScheduling {
    public static void main(String[] args) {
        int n = 4; // Number of jobs
        int[] profits = {40,30,20,10}; // Profits of the jobs
        int[] deadlines = {2, 2, 4,1}; // Deadlines of the jobs

        // Sort jobs by profit in descending order using bubble sort
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (profits[j] < profits[j + 1]) {
                    // Swap profits
                    int tempProfit = profits[j];
                    profits[j] = profits[j + 1];
                    profits[j + 1] = tempProfit;

                    // Swap corresponding deadlines
                    int tempDeadline = deadlines[j];
                    deadlines[j] = deadlines[j + 1];
                    deadlines[j + 1] = tempDeadline;
                }
            }
        }
        int maxd = 0;
        for(int i=0;i<n;i++){
            maxd=Math.max(maxd,deadlines[i]);
        }
        int[] res = new int[maxd+1];
        Arrays.fill(res,-1);
        int maxprofit=0;
        for(int i=0;i<n;i++){
            for(int j=deadlines[i];j>0;j--){
                if(res[j]==-1){
                    res[j]=i;
                    maxprofit+=profits[i];
                    break;
                }
            }
        }
        System.out.println(maxprofit);
        
        
    }
}
