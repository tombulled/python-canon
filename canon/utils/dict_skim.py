def dict_skim(dictionary, value=None):
    """
    Skim {dictionary} of all key->val pairs
    ... where val={value}
    """

    keys = list(dictionary.keys())

    for key in keys:
        val = dictionary[key]

        if val == value:
            dictionary.pop(key)

    return dictionary
