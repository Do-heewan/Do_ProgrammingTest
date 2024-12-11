import java.util.*;

public class Main {
    public static void main(String[] args) {
        int num_arr[] = new int[101];

        for (int i = 0; i < num_arr.length; i++) {
            num_arr[i] = i;
        }

        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int m = s.nextInt();

        for (int j = 0; j < m; j++) {
            int no1 = s.nextInt();
            int no2 = s.nextInt();

            int tmp;
            tmp = num_arr[no1];
            num_arr[no1] = num_arr[no2];
            num_arr[no2] = tmp;
        }
        
        for (int k = 1; k < n+1; k++) {
            System.out.print(num_arr[k] + " ");
        }
        s.close();
    }
}
