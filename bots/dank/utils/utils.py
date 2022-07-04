def count_whitespaces(text):
    for index, char in enumerate(text):
        if char == ":":
            return index


def remove_whitespaces_from_array(array):
    new_array = []
    for i in array:
        if i != "":
            new_array.append(i)
    
    return new_array