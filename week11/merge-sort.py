from random import shuffle

"""                       INSTRUCTIONS
        When you get this up and running, copy-paste your merge() and
        mergeSort() functions into your sorts.py file.
        This way, all of your sorting algorithms will be in one place.
"""

def makeList(N):
    L = []
    for i in range(N):
        L.append(i)
    return L


def merge(L, R, arr):
    """ Implement the merge() function below and you should be good to go """
    # merged = []
    # while len(leftL) > 0 and len(rightL) > 0:
    #     if leftL[0] < rightL[0]:
    #         merged.append(leftL.pop(0))
    #     else:
    #         merged.append(rightL.pop(0))
    # while len(leftL) > 0:
    #     merged.append(leftL.pop(0))
    # while len(rightL) > 0:
    #     merged.append(rightL.pop(0))
    i = 0
    j = 0
    k = 0
 
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(L):
    if len(L) > 1:
        half = len(L) // 2		 # split into two lists
        L1 = L[0:half]
        L2 = L[half:]
        mergeSort(L1)			 # sort each list
        mergeSort(L2)
        merge(L1,L2,L)		     # merge them back into one sorted list


def main():
    N = 10
    L = makeList(N)

    shuffle(L)
    print(L)
    mergeSort(L)
    print(L)
    assert L == makeList(N)
    print(L)


main()
