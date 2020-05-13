# import required library
import ast 

# pass the input array
# input_arr = [[3, 2], [4, 3], [2, 3], [3, 4]]
array = input('Enter seat config. eg:[[3, 2], [4, 3], [2, 3], [3, 4]]: ')
input_arr = ast.literal_eval(array)
print(input_arr)

def split_seats():
    """ Function that splits the seats based on input """
    length = len(input_arr)
    main_count = 1
    main_list = []

    for data in input_arr:
        count = 0
        row = 0
        column = 0
        for inp in data:
            if count == 1:
                column = inp
            else:
                row = inp
            count = count+1    

        arr_val = []
        for x in range (0, column):
            if main_count == 1:
                val = '  W  ' + (row-2) * '  M  ' + '  A  '
            elif main_count == length:
                val = '  A  ' + (row-2) * '  M  ' + '  W  '
            else:
                val = '  A  ' + (row-2) * '  M  ' + '  A  '
            arr_val.append(val)
        main_list.append(arr_val)
        main_count = main_count+1
    # print seat layout in the console
    prety_print_layout(main_list)
    return main_list


def fill_seats(main_list):
    """ Fill the seats based on the seat layouts """
    main_count = 1
    ais_list, win_list, fin_list = [], [], []
    
    for n in range(0, len(main_list)):
        main_count, aisle_list = fill_seat(main_list, n, main_count, 'A')
        ais_list.append(aisle_list)

    for n in range(0, len(main_list)):
        main_count, window_list = fill_seat(ais_list, n, main_count, 'W')
        win_list.append(window_list)

    for n in range(0, len(main_list)):
        main_count, middle_list = fill_seat(win_list, n, main_count, 'M')
        fin_list.append(middle_list)
    
    # print the seat number
    prety_print_seat(fin_list)
    return fin_list


def fill_seat(main_list, n, main_count, layout):
    child_list = []
    for list_a in main_list:
        if len(list_a) > n:
            str_va = list_a[n]

            if layout == 'A':
                str_va, main_count, child_list = fill_seat_layout(str_va, main_count, child_list, layout)
            if layout == 'W':
                str_va, main_count, child_list = fill_seat_layout(str_va, main_count, child_list, layout)
            if layout == 'M':
                str_va, main_count, child_list = fill_seat_layout(str_va, main_count, child_list, layout)

        else:
            child_list.append('')
            
    return main_count, child_list

def fill_seat_layout(str_va, main_count, child_list, layout):
    """ Assign seat number based on seat layout """ 
    if layout in str_va:
        if str_va.count(layout) == 1:
            str_rep = str_va.replace(layout, str(main_count))
        else:
            str_rep = str_va.replace(layout, str(main_count), 1)
            main_count = main_count+1
            str_rep = str_rep.replace(layout, str(main_count), 1)
        
        main_count = main_count+1
        child_list.append(str_rep)
    else:
        child_list.append(str_va)
    return str_va, main_count, child_list


def prety_print_layout(main_arr):
    """ Utility function to print the seat layout """
    print(120 * '-')
    print('Seating Layout')
    print(120 * '-')
    for n in range(0, len(main_arr)):
        for arr in main_arr:
            if len(arr) > n:
                    print(arr[n], end="\t\t")
            else:
                print('\t', end="\t\t")
        print()
    print(120 * '-')

def prety_print_seat(main_arr):
    """ Utility function to print the seat number """
    print(120 * '-')
    print('Seating Number')
    print(120 * '-')
    for arr in main_arr:
        for val in arr:
            if val is '':
                print('\t\t', end='\t\t')
            else:
                print(val, end="\t\t")
        
        print('')
    print(120 * '-')


if __name__ == '__main__':
    # call to split and fill the seats
    fill_seats(split_seats())
