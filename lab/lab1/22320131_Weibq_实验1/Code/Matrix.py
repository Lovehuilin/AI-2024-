def MatrixAdd(A, B, n):
    result = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
            
    return result

def MatrixMul(A, B, n):
    result = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    
    return result


# 测试样例
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]

print(f"A = {A}")
print(f"B = {B}")
print(f"相加结果为：{MatrixAdd(A, B, 3)}")
print(f"相乘结果为：{MatrixMul(A, B, 3)}")
    