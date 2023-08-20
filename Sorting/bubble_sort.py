A = [64, 25, 12, 22, 11]


for i in range(len(A)):
    for j in range(len(A)-i-1):
        if A[j+1] < A[j]:
            a = A[j]
            b =A[j+1]
            A[j+1]=a 
            A[j] =b

            # A[j-1] =A[j]
print(A)
