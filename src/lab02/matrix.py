def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    num = len(mat[0])
    if any(len(row) != num for row in mat):
        return "ValueError"
    return [[mat[i][j] for i in range(len(mat))] for j in range(num)]


print("transpose")
print(transpose([[1, 2], [3, 4]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    if mat and any(len(row) != len(mat[0]) for row in mat):
        return "ValueError"
    return [sum(row) for row in mat]


print("row_sum")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    num = len(mat[0])
    if any(len(row) != num for row in mat):
        return "ValueError"
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(num)]


print("col_sums")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
