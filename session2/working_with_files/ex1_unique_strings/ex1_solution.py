# stage 1
def print_file( path_to_file ):
    with open(path_to_file) as in_file:
        print(in_file.read())

# print_file('session2/working_with_files/ex1_unique_strings/happy_strings.txt')

# stage 2
def get_set_from_file( path_to_file ):
    with open(path_to_file) as in_file:
        file_as_string = in_file.read()
    return set(file_as_string.replace('\n', ' ').split(' '))

# print(get_set_from_file('session2/working_with_files/ex1_unique_strings/happy_strings.txt'))

# stage 3
def get_set_from_file( path_to_file ):
    word_counter = dict()
    with open(path_to_file) as in_file:
        file_as_string = in_file.read()
        words_list = file_as_string.replace('\n', ' ').split(' ')
        for word in words_list:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
    return word_counter

# print(get_set_from_file('session2/working_with_files/ex1_unique_strings/happy_strings.txt'))