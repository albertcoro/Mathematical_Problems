def pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

for row in pascals_triangle(5):
    print(row)