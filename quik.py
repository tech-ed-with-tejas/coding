A = [64, 25, 12, 22, 11]

def partition(low,high,arr):
    pivot = arr[high]

    i = low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1

def quik(low,high,arr):
    if low<high:

        pi = partition(low,high,arr)
        quik(low,pi-1,arr)
        quik(pi+1,high,arr)

quik(0,len(A)-1,A)
print(A)