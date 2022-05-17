import random

def method_with_args(*args):
    if (len(args)) == 0 :
        print("No arguments passed")
        return
      
    list_with_strings_storage = []
    list_with_strings = []
    list_with_numbers = []
    
    for arg in args:
        if type(arg) is str:
            list_with_strings.append(arg)
        if type(arg) is int:
            list_with_numbers.append(arg)

    list_with_numbers.sort()

    for i in range(0, 9):
        random.shuffle(list_with_strings)
        list_with_strings_storage.append(list_with_strings + list_with_numbers)

    print("#############")
    print(*list_with_strings_storage, sep = "\n")
    print("#############")


method_with_args('aaa', 'bbb', 'rrr', 1000, 'ddd', 444, 1, 'fdfdfd', 'jjj', 5, -1)
method_with_args()

