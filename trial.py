import numpy as np
import math

def checkDiagonal(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                continue
            else:
                if abs(arr[i][j]) > 0.619:
                    return False
    return True

def normalize(u):
    a = 0
    for x in u:
        a += x*x
    return math.sqrt(a)

def gram_schmidt_process(A):
    """
    Perform QR decomposition of matrix A using Gram-Schmidt process.
    """
    num_rows = np.shape(A)[0]

    # Initialize empty orthogonal matrix Q.
    Q = np.empty([num_rows, num_rows])
    cnt = 0

    # Compute orthogonal matrix Q.
    for a in np.transpose(A):
        u = np.copy(a)
        for i in range(0, cnt):
            proj = np.dot(np.dot(Q[:, i].T, a), Q[:, i])
            u -= proj

        e = u / normalize(u)
        Q[:, cnt] = e

        cnt += 1  # Increase columns counter.

    # Compute upper triangular matrix R.
    R = np.dot(np.transpose(Q), A)

    return (Q, R)

def qrFactorization(arr):
    temp = arr
    i = 0
    while(True):
        Q,R = gram_schmidt_process(temp)
        temp = np.dot(R, Q)
        if(checkDiagonal(temp)):
            print("Number of Factorizations: " + str(i+1))
            break
        else:
            i += 1
    return temp

def printLambda(arr):
    count = 1
    for i in range(len(arr)):
        temp = arr[i][i]
        if(abs(temp) < 0.000000000001):
            temp = 0
        print("Lamda"+str(count) +": " + str(temp))
        count += 1
    
def read():
    f = open('matrix.txt', 'r')
    temp = f.read().split('\n')
    arr = []
    for i in temp:
        if i == '':
            continue
        arr.append(i.split(" "))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = float(arr[i][j])
    return arr

def main():
    arr = read()
    matrix = np.array(arr)
    print(matrix)
    printLambda(qrFactorization(arr))

main()