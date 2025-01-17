//{ Driver Code Starts
//Initial Template for Java



import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] inputLine;
            inputLine = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine[0]);
            int x = Integer.parseInt(inputLine[1]);
            int[] arr = new int[n];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            Pair ans = new Solve().getFloorAndCeil(arr, n, x);
            System.out.println(ans.floor + " " + ans.ceil);
        }
    }
}

class Pair {
    int floor, ceil;

    Pair() {
        this.floor = 0;
        this.ceil = 0;
    }

    Pair(int floor, int ceil) {
        this.floor = floor;
        this.ceil = ceil;
    }
}

// } Driver Code Ends


//User function Template for Java




class Solve {
    Pair getFloorAndCeil(int[] arr, int n, int x) {
        // code here
        int floor=Integer.MIN_VALUE, ceil=Integer.MAX_VALUE;
        
        // sorting the array
        Arrays.sort(arr);
        
        // base case
        if(arr[0]>x) floor = -1;
        if(arr[n-1]<x) ceil = -1;
        
        int low = 0, high = n-1;
        
        // binary search
        while(low<=high){
            int mid = low + (high-low)/2;
            if(x==arr[mid]){
                // we want to maximize the floor and
                // minimize the ceiling
                floor = Math.max(floor,arr[mid]);
                ceil = Math.min(ceil,arr[mid]);
            }
            if(x>arr[mid]){
                floor = Math.max(floor,arr[mid]);
                low = mid+1;
            }
            else{
                ceil = Math.min(ceil,arr[mid]);
                high = mid-1;
            }
        }
        Pair ans = new Pair(floor, ceil);
        return ans;
    }
}

