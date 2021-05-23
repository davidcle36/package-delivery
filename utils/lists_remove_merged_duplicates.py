def lists_remove_merged_duplicates(a1, a2):
    updated_list = []
    for num in a1:
        if num not in a2:
            updated_list.append(num)
    return updated_list
