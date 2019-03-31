def selection_sort(v):
    for i in range(len(v)):
        index_min = i
        for j in range(i+1, len(v)):
            if(v[j] > v[index_min]):
                index_min = j

        v[i], v[index_min] = v[index_min], v[i]

def insertion_sort(v):
    for i in range(1, len(v)):
        j = i
        while j != 0 and v[j] > v[j-1] :
            v[j], v[j-1] = v[j-1], v[j]
            j -= 1

def bubble_sort(v):
    for i in range(len(v)):
        troca = False
        for j in range(0, len(v)-i-1):
            if v[j] < v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
                troca = True

        if troca == False:
            break

def shell_sort(v):
    gap = len(v)//2
    while gap > 0:
        for i in range(gap, len(v)):
            temp = v[i]
            j = i
            while j >= gap and v[j-gap] < temp:
                v[j] = v[j-gap]
                j -= gap

            v[j] = temp
        gap //= 2
