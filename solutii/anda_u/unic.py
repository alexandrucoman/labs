def gaseste(istoric):
    result = 0
    for i in istoric:
        result ^= i;
    return result
if __name__ == "__main__":
    assert gaseste([1, 2, 3, 2, 1]) == 3
    assert gaseste([1, 1, 1, 2, 2]) == 1

