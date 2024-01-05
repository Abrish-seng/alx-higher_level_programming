def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_file = [i for i in my_list]
    new_file[idx] = element
    return new_file
