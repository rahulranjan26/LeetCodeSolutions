class Solution {
    public int findMin(int[] arr) {
        int low = 0, high = arr.length - 1;
        int n = arr.length;

        // If the array is not rotated


        while (low <= high) {
            int mid = (low + high) / 2;

            if (arr[low] <= arr[high]) {
                return arr[low];
            }
            int next = (mid + 1) % n;
            int prev = (mid + n - 1) % n;
            if (arr[mid] <= arr[next] && arr[mid] <= arr[prev]) {
                return arr[mid];
            }

            if (arr[low] <= arr[mid])
                low = mid + 1;
            else
                high = mid - 1;
        }
        return -1;
    }
        
    }
