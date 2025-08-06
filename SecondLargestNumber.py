#find second largest element


def SecondLargest(arr):
    large=second=-1
    for i in range(len(arr)):
        if arr[i]>large:
            second=large
            large=arr[i]
        elif arr[i]>second and arr[i]!=large:
            second=arr[i]
    return second
arr=[12,35,1,10,34,1]
print("second largest",SecondLargest(arr))