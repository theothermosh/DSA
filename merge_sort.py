def merge(list_a, list_b):
    merged_list = []
    len_a, len_b = len(list_a), len(list_b)
    index_a, index_b = 0, 0
    while index_a < len_a and index_b < len_b:
        if list_a[index_a] < list_b[index_b]:
            merged_list.append(list_a[index_a])
            index_a += 1
        else:
            merged_list.append(list_b[index_b])
            index_b += 1

        if index_a < len_a:
            merged_list.extend(list_a[index_a:])
        elif index_b < len_b:
            merged_list.extend(list_b[index_b:])

    return merged_list


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    return merge(left, right)