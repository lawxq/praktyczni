def remove_duplicates(list):
    result_list= []
    for item in list:
        if item not in result_list:
            result_list.append(item)

    return result_list
def sort_list(input_list):
    numbers = sorted([x for x in input_list if isinstance(x, (int, float))])
    strings = sorted([x for x in input_list if isinstance(x, str)])
    return numbers + strings

test_list=[8,1,2,3,4,"є",5,6,3,4,5,2,"f",7,6,5,4,3,4,230,4,3, 'Привіт', 'анаконда']
unique_list=remove_duplicates(test_list)
print(unique_list)
print(sort_list(unique_list))