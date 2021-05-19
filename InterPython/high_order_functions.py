from functools import reduce

def run():

    my_list = [1, 2, 3, 5, 8, 11, 13, 16, 18, 21, 23, 24, 28, 30]

    # FILTER
    print('FILTER: ')

    # use of list comprehensions
    filter_list_comprehension = [i for i in my_list if i % 2 != 0]
    print('list comprehension filter: ', filter_list_comprehension)

    # use of high order function FILTER
    filtered_list = list(filter(lambda x: x % 2 != 0, my_list))
    print('filtered list: ', filtered_list, '\n')

    # MAP
    print('MAP: ')

    # use of list comprehensions
    map_list_comprehension = [i**2 for i in my_list]
    print('list comprehension map', map_list_comprehension)

    # use of high order function MAP
    mapped_list = list(map(lambda x: x**2, my_list))
    print('mapped list', mapped_list, '\n')

    #REDUCE
    print('REDUCE: ')

    # use of for
    my_list_multiplied = 1
    for i in my_list:
        my_list_multiplied *= i
    print('list multiplied for: ', my_list_multiplied)

    #use of high order function REDUCE
    reduce_multiplied = reduce(lambda a, b: a * b, my_list)
    print('reduced list: ', reduce_multiplied)


if __name__ == '__main__':
    run()