def count_whitespaces(text):
    for index, char in enumerate(text):
        if char == "<":
            return index

    return 0


def remove_whitespaces_from_array(array):
    return [i for i in array if i != ""]
