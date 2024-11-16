public class qs{
    public static void qsort(int[] arr,int l,int h){
        if(l<h){
            int j = partition(arr, l, h);
            qsort(arr, l, j-1);
            qsort(arr,j+1,h);
        }
    }
    public static int partition(int[] arr,int l,int h){
        int pivot = arr[l];
        int i=l;
        int j=h+1;
        do{
            do{
                i++;
            }while(i<=h && arr[i]<pivot);
            do{
                j--;
            }while(arr[j]>pivot);
            if(i<j){
                int temp = arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }while(i<j);
        arr[l]=arr[j];
        arr[j]=pivot;
        return j;
    }
    public static void main(String args[]){
        int[] arr = {5,4,2,2,1};
        qsort(arr, 0, 4);
        for(int i : arr){
            System.out.println(i);
        }
    }
}