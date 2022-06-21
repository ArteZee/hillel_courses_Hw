# def decorator(func):
#     def wrapper(any_list, *arg):
#         func(any_list, *arg)
#         assert len(any_list) != 0
#         assert len(arg) == 1
#     return wrapper
#
# @decorator
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
print(my_reduce((1,2,3),6))


def check_reduce(first_arg, *second_arg):
    """

    :param a: list or tuple or str
    :param b: int or str
    :return: error if this need
    """

    my_reduce(first_arg, *second_arg)
    # check that only correct when first argument is  tuple or list
    assert first_arg != list() or second_arg != tuple()
    # check that only correct when first argument not empty
    assert len(first_arg) != 0
    # check that len second argument must be
    assert len(second_arg) == 1 or len(second_arg) == 0


check_reduce((1, 2, 3), 6)
