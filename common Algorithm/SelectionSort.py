def min_index(lst):
    k = 0
    for i in range(len(lst)):
        if lst[i]<lst[k]:
            k = i
    return k

def selection_sort(lst):
    for i in range(len(lst)):
        j = min_index(lst[i:]) + i
        lst[i],lst[j] = lst[j],lst[i]
    return lst


if __name__  == "__main__":
    lst = [5, 3, 1, 4, 2]
    output = selection_sort(lst)
    print(output)