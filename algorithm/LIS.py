import bisect

def lis(array):
    """最長増加部分列 O(NlogN)

    Args:
        array (list): 対象の配列

    Returns:
        int: 最長増加部分列の長さ
    """
    seq = [array[0]]
    for v in array:
        if seq[-1] < v:
            seq.append(v)
        else:
            seq[bisect.bisect_left(seq, v)] = v

    return len(seq)


# Driver Code
if __name__ == "__main__":
    A = [1, 5, 3, 6, 2, 4, 8, 7]
    print(lis(A))
    # 4