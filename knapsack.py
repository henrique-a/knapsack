import numpy as np
import time

def main():

    #Instance
    c = 750 # weight capacity
    V = np.array([135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240,]) # values
    P = np.array([ 70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]) # weights
    
    start = time.time()
    S_dp = dp(V, P, c)
    end = time.time()
    print(S_dp)
    print(sum([V[i] for i in S_dp]))
    print("Tempo: {} s".format(round(end - start, 5)))
    start = time.time()
    S_f = fptas(V, P, c, 0.5) 
    end = time.time()
    print(S_f)
    print(sum([V[i] for i in S_f]))
    print("Tempo: {} s".format(round(end - start, 5)))

# Fully Polynomial Time Approximation Scheme   
def fptas(V, P, c, e):
    n = len(V)
    R = e*max(V)/n
    Vf = np.floor(V/R)
    return dp(Vf, P, c)

# Dynamic Programming solution
def dp(V, P, c):
    n = len(V)
    max_v = int(max(V))
    M = np.zeros(shape=(n+1,n*max_v+1))
    S = []
    for i in range(n+1):
        S.append([])
        for j in range(n*max_v+1):
            S[i].append([])
    
    for i in range(n+1):
        for l in range(n*max_v+1):
            if i == 0 and l > 0:
                M[i,l] = np.infty
            elif l == 0:
                M[i,l] = 0
            elif V[i-1] <= l:
                M[i,l] = min(M[i-1,l], M[i-1, l-int(V[i-1])] + P[i-1])
                if M[i,l] == M[i-1, l-int(V[i-1])] + P[i-1]:
                    S[i][l] = list(S[i-1][l-int(V[i-1])])
                    S[i][l].append(i-1)
                else:
                    S[i][l] = list(S[i-1][l])
            elif V[i-1] > l:
                M[i,l] = M[i-1,l]
                S[i][l] = list(S[i-1][l])

    for l in range(n*max_v, -1 , -1):
        if M[n,l] <= c:
            return S[n][l]

if __name__ == '__main__':
    main()
