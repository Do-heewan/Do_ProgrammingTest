K, D, A = map(int, input().split("/"))

print("hasu" if (D == 0) or (K + A < D) else "gosu")