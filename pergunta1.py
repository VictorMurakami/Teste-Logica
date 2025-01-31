def organizar(arr):
    count = 0
    n = len(arr)
    resultado = [0] * n

    for i in range(n):
        if arr[i] == 1:
            resultado[count] = 1
            count += 1

    x = count
    for i in range(n):
        if arr[i] != 1:
            resultado[x] = arr[i]
            x += 1

    for i in range(n):
        arr[i] = resultado[i]

    return arr

arr = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
print(organizar(arr))
