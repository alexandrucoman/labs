"""Fill islated spaces"""


def umple(imagine, punct, visited):
    """Completarea sectiunilor izolate din matrice."""
    to_visit = []
    if visited is None:
        visited = []
    if punct in visited:
        return
    visited.append(punct)
    imagine[punct[0]][punct[1]] = '*'
    if punct[0] < 0 or punct[0] > len(imagine):
        return
    # jos
    if punct[1] + 1 < len(imagine) - 1 \
            and imagine[punct[0] + 1][punct[1]] == '-':
        to_visit.append((punct[0] + 1, punct[1]))
    if punct[1] + 1 < len(imagine[punct[0]]) - 1 \
            and imagine[punct[0]][punct[1] + 1] == '-':
        to_visit.append((punct[0], punct[1] + 1))
    if punct[0] > 0 and imagine[punct[0] - 1][punct[1]] == '-':
        to_visit.append((punct[0] - 1, punct[1]))
    if punct[1] > 0 and imagine[punct[0]][punct[1] - 1] == '-':
        to_visit.append((punct[0], punct[1] - 1))
    for each in [x for x in to_visit if x not in visited]:
        umple(imagine, each, visited)


def main():
    """First runned function"""
    imaginea = [
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
    ]
    umple(imaginea, (1, 3), [])
    umple(imaginea, (5, 11), [])

if __name__ == "__main__":
    main()
