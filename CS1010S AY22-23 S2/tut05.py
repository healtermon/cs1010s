def hanoi(n, src, dst, aux):
    if n == 1: return ((src,dst),)
    return hanoi(n-1,src,aux,dst) + hanoi(1,src,dst,aux) + hanoi(n-1,aux,dst,src)
