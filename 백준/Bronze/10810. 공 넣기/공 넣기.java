import java.util.*;

public class Main {
    public static void main(String[] args) {
        int num_arr[] = new int[101];

        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int m = s.nextInt();

        for (int i = 0; i < m; i++) {
            int no1 = s.nextInt();
            int no2 = s.nextInt();
            int no3 = s.nextInt();

            for (int j = no1; j < no2+1; j++) {
                num_arr[j] = no3;
            }
        }
        
        for (int k = 1; k < n+1; k++) {
            System.out.print(num_arr[k] + " ");
        }

        s.close();
    }
}
