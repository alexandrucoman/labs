

#!/usr/bin/env python
# *-* coding: UTF-8 *-*

istoric=list()
istoric.append(1)
istoric.append(2)
istoric.append(3)
istoric.append(4)
istoric.append(5)
istoric.append(1)
istoric.append(2)
istoric.append(3)
istoric.append(4)
def gaseste(istoric):
        p=istoric.pop()
        for i in istoric:
            p=i^p
        return p

if __name__ == "__main__":
        print(gaseste(istoric))


