# interatively determines the maximum from a list of ints
# list -> int
def max_list_iter(int_list):  # must use iteration not recursion
    if int_list == None:
        raise ValueError
    elif len(int_list) == 0:
        return None
    else:
        max = int_list[0]
        for val in int_list:
            if val > max:
                max = val
        return max
    # """finds the max of a list of numbers and returns the value (not the index)
    # If int_list is empty, returns None. If list is None, raises ValueError"""


# recursively reverses a list of ints
# list -> list
def reverse_rec(int_list):  # must use recursion
    if int_list == None:
        raise ValueError
    elif len(int_list) == 0:
        return int_list
    else:
        return reverse_rec(int_list[1:]) + (int_list[0:1])

    # """recursively reverses a list of numbers and returns the reversed list
    # If list is None, raises ValueError"""


# recursively determines if a target value exists within the specified bounds of a list
# list - > int (assuming found)
def bin_search(target, low, high, int_list):  # must use recursion
    if int_list == None:  # the list was none
        raise ValueError
    elif len(int_list) == 0 or high < low:  # the target was not found
        return None
    else:
        if int_list[high] == target:
            return high
        else:
            return bin_search(target, low, high - 1, int_list)
    # """searches for target in int_list[low..high] and returns index if found
    # If target is not found returns None. If list is None, raises ValueError """
