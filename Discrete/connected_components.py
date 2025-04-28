def dfs(node, visited, adj_matrix, component):
    visited[node] = True
    component.append(node)
    for neighbor in range(len(adj_matrix)):
        if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor, visited, adj_matrix, component)


def find_connected_components(n, lower_triangle):
    # ساخت ماتریس مجاورت
    adj_matrix = [[0] * n for _ in range(n)]
    index = 0
    for i in range(1, n):
        for j in range(i):
            adj_matrix[i][j] = lower_triangle[index]
            adj_matrix[j][i] = lower_triangle[index]  # چون گراف غیرجهت‌دار است
            index += 1

    visited = [False] * n
    components = []

    for i in range(n):
        if not visited[i]:
            component = []
            dfs(i, visited, adj_matrix, component)
            components.append(component)

    return components


n = int(input().strip())
lower_triangle = list(map(int, input().split()))

components = find_connected_components(n, lower_triangle)

print(len(components))
for i, component in enumerate(components):
    print(f"مؤلفه {i + 1}: {component}")
