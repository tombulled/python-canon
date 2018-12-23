def list_from_dict(list_map):
    """
    Convert {list_map}, which is in the form:
        {
            0: item1,
            1: item2,
            ...
        }
    Into a list, e.g: [item1, item2]
    """

    max_index = max(index for index in list_map.keys())

    decoded_list = [None for _ in range(max_index + 1)]

    for index, item in list_map.items():
        decoded_list[index] = item

    return decoded_list
