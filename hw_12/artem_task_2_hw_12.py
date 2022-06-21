def my_reduce(any_list, *arg):
    """
    function can get 1 argument or 2 argument already
    :param any_list:list or tuple
    :param arg: int or str
    :return: int
    """
    # create counter to put  in index
    counter = 0

    #  check what type elements in  our list or tuple
    # if second argument empty and elem in any_list is int
    if arg == () and type(any_list[0]) == int:
        omega = 0
    # if second argument empty and elem in any_list is str
    elif arg == () and type(any_list[0]) == str:
        omega = ""
    # if we have the second argument
    else:
        omega = arg[0]

    # summarize our arguments
    while counter != len(any_list):
        omega += any_list[counter]

        counter += 1

    return omega


print("Your number is: ", my_reduce([1, 2, 3]))
