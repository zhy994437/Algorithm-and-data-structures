class Disjointset:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

class Reorganization:
    def cost(self, ch):
        if 'A' <= ch <= 'Z':
            return ord(ch) - ord('A')
        else:
            return ord(ch) - ord('a') + 26

    def getcost(self, kingdom, build, destroy):
        n = len(kingdom)
        E1, E2 = [], []
        for i in range(n):
            for j in range(i):
                if kingdom[i][j] == '1':
                    E1.append((i, j, self.cost(destroy[i][j])))
                else:
                    E2.append((i, j, self.cost(build[i][j])))
        E1.sort(key=lambda x: (-x[2], x[0], x[1]))
        E2.sort(key=lambda x: (x[2], x[0], x[1]))

        ds = Disjointset(n)
        cost = 0
        for u, v, w in E1:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
            else:
                cost += w
        for u, v, w in E2:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                cost += w
        return cost

def parse_inputmatrix(input_str):
    rows = input_str.strip("[]").split(",")
    matrix = [row.strip("'") for row in rows]
    return matrix

def main():
    inputs = input().split()
    kingdom = parse_inputmatrix(inputs[0])
    build = parse_inputmatrix(inputs[1])
    destroy = parse_inputmatrix(inputs[2])

    solver = Reorganization()
    min_cost = solver.getcost(kingdom, build, destroy)
    print(min_cost)

if __name__ == "__main__":
    main()