import bisect

def compress(a):
    """1次元座標圧縮 (大小関係の抽出) O(NlogN)

    Args:
        a (list): 対象の配列

    Returns:
        list: 圧縮済みの配列
    """
    tmp = sorted(list(set(a)))
    compressed = []
    for v in a:
        compressed.append(bisect.bisect_left(tmp, v))

    return compressed


# Driver Code
if __name__ == "__main__":
    A = [1, 4, 3, 4, 8, 6]
    print(compress(A))
    # [0, 2, 1, 2, 4, 3]