arr = [9, 2, 3, 1, 4]
n = max(arr)
num_faltando = [i for i in range(n + 1) if i not in arr]
arr.extend(num_faltando)
print(arr)