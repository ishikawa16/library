class BinaryIndexedTree:
    """BIT: Binary Indexed Tree

    Attributes:
        n (int):     要素数
        tree (list): 要素の格納先 (1-indexed)
    """
    def __init__(self, n):
        """初期化 O(1)

        Args:
            n (int): 要素数
        """
        self.n = n
        self.tree = [0] * (n+1)

    def add(self, i, v):
        """値の更新 O(logN)

        Args:
            i (int): 加算対象のindex
            v (int): 加算値
        """
        i += 1
        while i <= self.n:
            self.tree[i] += v
            i += i & -i

    def sum(self, i):
        """区間和の計算 O(logN)

        Args:
            i (int): 区間の右端のindex

        Returns:
            int: [0, i)の区間和
        """
        range_sum = 0
        while i > 0:
            range_sum += self.tree[i]
            i -= i & -i

        return range_sum

    def lower_bound(self, v):
        """BIT上の二分探索 O(logN)

        Args:
            v (int): 対象の値

        Returns:
            int: v <= sum(i) を満たす最小のi
        """
        idx = 0
        for i in range(self.n.bit_length(), -1, -1):
            nxt_idx = idx + (1 << i)
            if nxt_idx <= self.n and self.tree[nxt_idx] < v:
                v -= self.tree[nxt_idx]
                idx = nxt_idx
        return idx + 1


# Driver Code
if __name__ == "__main__":
    bit = BinaryIndexedTree(5)

    bit.add(0, 7)      # [7, 0, 0, 0, 0]
    bit.add(1, 2)      # [7, 2, 0, 0, 0]
    bit.add(2, 5)      # [7, 2, 5, 0, 0]
    bit.add(3, 1)      # [7, 2, 5, 1, 0]
    bit.add(4, 4)      # [7, 2, 5, 1, 4]
    print(bit.sum(3))
    # 14
    print(bit.sum(5))
    # 19
    print(bit.lower_bound(15))
    # 4

    bit.add(1, 7)      # [7, 9, 5, 1, 4]
    print(bit.sum(5))
    # 26