import java.util.*;

import javax.swing.plaf.basic.BasicInternalFrameUI.InternalFramePropertyChangeListener;

public class sumofsub {
    public static void sum(int[] arr,int n,int k,int i,int sum,List<Integer> res){
        if(sum==k){
            for(int id : res){
                System.out.println(id);
            }
            return ;
        }
        if(sum>k || i==n){
            return;
        }
        res.add(arr[i]);
        sum(arr,n,k,i+1,sum+arr[i],res);
        res.remove(res.size()-1);
        sum(arr,n,k,i+1,sum,res);
        
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements of the array: ");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.print("Enter the target sum: ");
        int k = sc.nextInt();
        List<Integer> l = new ArrayList<>();
        sum(arr,n,k,0,0,l);
    }
}