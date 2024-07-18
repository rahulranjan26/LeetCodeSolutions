class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        n1, n2 = len(a), len(b)
        # if n1 is bigger swap the arrays:
        if n1 > n2:
            return self.findMedianSortedArrays(b, a)

        n = n1 + n2  # total length
        left = (n1 + n2 + 1) // 2  # length of left half
        # apply binary search:
        low, high = 0, n1
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            # calculate l1, l2, r1, and r2;
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            if mid1 < n1:
                r1 = a[mid1]
            if mid2 < n2:
                r2 = b[mid2]
            if mid1 - 1 >= 0:
                l1 = a[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = b[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0

            # eliminate the halves:
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0  # dummy statement
    
    
    """
    First we decompose this problem into simpler subproblems:

Find a given index idx in a sorted a+b array. Let len(a)=m, len(b)=n, l=m+n. Having solution to this problem we can easily compute median as we just need to find:
a) idx=l // 2 when l is odd as this is median index in odd length array
e.g. [1,2,3], l = 3, idx = l//2 = 1
b) idx=l//2 and idx=l//2-1 when l is even as these are median indices in this case
e.g. [1,2,3,4], l = 4, idx1 = l//2 = 2, idx2 = l//2-1 = 1

 def findMedianSortedArrays(self, a, b):

 	l = len(a) + len(b)

 	if l % 2:
 		return self.get_median(a, b, l // 2)
 	else:
 		return (self.get_median(a, b, l // 2) + self.get_median(a, b, l // 2 - 1))  / 2
Find recursively value at idx in a+b by cutting off part of a or b where idx is surely not present.
a) We take two indices ai = len(a)//2 in array a and bi = len(b)//2 in array b. They roughly cut both arrays in half which will lead to log(m+n) time complexity. Denoting ma = a[ai] and mb = b[bi] the two arrays look like:

 a=[????? ma *****]
 b=[........ mb ######]
where ?, ., * and # just visualize elements we do not know.
b) We know the values ma and mb. Not to consider many sub-scenarios we make it so that ma <= mb i.e.

  if ma > mb:
 	ma, mb = mb, ma
 	ai, bi = bi, ai
 	a, b = b, a
Thanks to this simplification we will always be able to either cut off beginning of array a or end of array b as will be explained below.

c) Now the rough visualization of combined array is:

 a+b=[&&&&&& ma &&&& mb &&&&&&]
Where & is composed of ?, ., * and # in some way. How exactly we cannot say but we can at least place them with respect to ma and mb:

 a+b=[.??.?.?.?? ma **.*.**.. mb ##*##**#*#]
Notice that we have three parts here: .??.?.?.??, **.*.**.. and ##*##**#*#.

d) Now what can be the maximum possible index of ma in a+b array? This is if all . were to the left of ma i.e.

 a+b=[.??.?.?.?? ma ***** mb ##*##**#*#]
then len(?????) = len(a)//2, len(......) = len(b)//2 so
max_idx_ma = len(a) // 2 + len(b) // 2

e) Now if max_idx_ma < idx then we know that index we are looking for is surely not located among ?????? ma i.e. left part of array a because it is located in
***** mb ##*##**#*# part of array a+b. So we can just cut this part off and repeat the reasoning in 2. on a[ai+1:], b, idx - (len(??????) + 1) = idx - (len(a)//2 + 1) (+1 because we also throw out ma).

f) Else we know that max_idx_ma >= idx. In other words in a+b array

 a+b=[.??.?.?.?? ma ***** mb ##*##**#*#]
idx is located in .??.?.?.?? ma part. Whatever the length of ***** because ma and mb are two different elements in a sorted array a+b and ma <= mb:

 max_idx_ma  < min_idx_mb
and

 idx <= max_idx_ma  < min_idx_mb
which means that we can throw away mb ###### part of b array in this case and consider new problem on a, b[:bi], idx.

Remarks:

Without simplification in 1. we need to be looking for two indices and considering total lenght of the array which greatly complicates solution.
Without simplification in 2. b) we would need to consider 4 subcases depending on relative values of ma and mb.
A very important point is that we throw out ma or mb every time we cut off. This way we make sure that we always throw out at leas one element making it possible to reach the point where either a is empty or b is empty.
Time complexity:

We always cut off half of a or half of b. Therefore it will take O(log(m) + log(n)) to cut to zero.

O(log(m) + log(n)) <= O(log(max(m, n)) + log(max(m, n))) = O(log(max(m, n))) <= O(log(m+n))
    
    
    
    """






        