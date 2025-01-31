def temsoma(arr, X):
    seen = set()
    for num in arr:
        if X - num in seen:
            return True
        seen.add(num)
    return False

arr = [1, 15, 2, 7, 2, 5, 7, 1, 4]
numero = int(input("Digite um número: "))
print(temsoma(arr, numero))