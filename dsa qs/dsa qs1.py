# DSA -Day- 1
# Merge sorted array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,9,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

def mergesortedarray(num1,m,num2,n):
    i=m-1 #represent length of num1
    j=n-1 #represent length of num2
    k=m+n-1 #represent length of mergesort num1 which is 5 in this example
    while i>=0 and j>=0: #put the condition check that length is greter that 0 or not if it is negeitive this condion fails
        if num1[i]>num2[j]: #then compare the pointers i and j which is greater place at k's last position in this condition checks that last element of the num1 is greater than last element of the num2 if it is true ..
            num1[k]=num1[i] #updates the k value which is 0 replace with num1[i] value
            i-=1 #then i decrements it represents the pointer goes before index
        
        else:
            num1[k]=num2[j] #if that if condition is failes if comes the else condition if updates num2[j] into num[k#]
            j-=1 #then j decrements
        k-=1 #k decremets either if or else is excuted.
        #second while loop for left elements in num2 because no need to ceck num1 why because num1 is already sorted it already in correcr place when we merge in also in num1 only.
    while j >= 0:
        num1[k] = num2[j]
        j -= 1
        k -= 1



num1 = [0,0,0]
m = 3
num2 = [2,5,6] 
n = 3
mergesortedarray(num1,m,num2,n)
print(num1)

# why we need second while loop
# num1 = [0, 0, 0, 0, 0, 0]
# m = 0  # num1 has no elements
# num2 = [2, 5, 6]
# n = 3  # num2 has 3 elements

