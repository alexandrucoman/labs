"""Solutie la problema unic"""


def gaseste_unic(istoric):
    """Functia pentru aflarea elementului cu numar impar de aparitii"""
    unic = 0
    for curent in istoric:
        unic = unic ^ curent
    return unic


if __name__ == "__main__":
    try:
        assert gaseste_unic([1, 2, 3, 2, 1]) == 3
    except AssertionError:
        print("Nu acesta este angajatul pe care il cautati")

    try:
        assert gaseste_unic([1, 1, 1, 2, 2]) == 1
    except AssertionError:
        print("Nu acesta este angajatul pe care il cautati")
