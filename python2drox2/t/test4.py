def my_func(a, b, c, d=3, *y, **z):
    pass

if __name__ == '__main__':
    my_list = [1, 2, 3]
    my_dict = {'i': 'j', 'k': 'l'}
    my_func(7, 8, 9, *my_list, **my_dict)

