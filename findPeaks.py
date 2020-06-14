A = [1,3,4,5,7,6,4,5,10,1]

print(A)

# Boundary case
if A[0]>=A[1]:
    print(A[0])

for i in range(0,len(A)-1):
    if (A[i]>=A[i-1]) and (A[i]>=A[i+1]):
        print(A[i])
# Boundary case
if A[len(A)-1]>=A[len(A)-2]:
    print(A[len(A)-1])
