public class fracknap {
    public static void main(String args[]) {
        int[] p = {75, 80, 120, 100, 60}; // Profits
        int[] w = {50, 40, 30, 20, 10};  // Weights
        int n = 5; // Number of items
        float[] frac = new float[n]; // Fraction of each item to include
        for(int i=0;i<n;i++){
            for(int j=0;j<n-1;j++){
                if((float)(p[j]/w[j])<(float)(p[j+1]/w[j+1])){
                    int temp = p[j];
                    p[j]=p[j+1];
                    p[j+1]=temp;
                    temp = w[j];
                    w[j]=w[j+1];
                    w[j+1]=temp;
                }
            }
        }
        int m = 50;
        float rem = m;
        int k=0;
        for(int i=0;i<n;i++){
            if(w[i]<=rem){
                frac[i]=1;
                rem-=w[i];
            }else{
                k=i;
                break;
            }
        }
        if(k<=n){
            frac[k]=(float)(rem/w[k]);
        }
        for(int i=0;i<n;i++){
            System.out.println((float)frac[i]*p[i]);
            
        }
    }
}
