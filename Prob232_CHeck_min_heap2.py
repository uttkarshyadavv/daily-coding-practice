def solution(arr):
    n=len(arr)
    for ind in range(n//2-1,-1,-1):
        L_child= (2*ind)+1
        R_child= (2*ind)+2
        if L_child<n and arr[L_child]<arr[ind]:
            return False
        if R_child<n and arr[R_child]<arr[ind]:
            return False
    return True