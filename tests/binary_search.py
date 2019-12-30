# https://www.geeksforgeeks.org/python-program-for-binary-search/
# Iterative Binary Search Function
# It returns location of x in given array arr if present,
# else returns -1
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l)//2;
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
        # If x is smaller, ignore right half
        else:
            r = mid - 1
    # If we reach here, then the element was not present
    return -1

l = [1, 4, 5, 8, 9, 12]
print(binarySearch(l, 0, len(l)-1, 4))
