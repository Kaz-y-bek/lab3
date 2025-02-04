def unique(num):
    unique_list = []
    for i in num:
        if i not in unique_list:  
            unique_list.append(i)
    return unique_list
print(unique([1, 2, 2, 3, 4, 4, 5]))