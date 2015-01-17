# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]


# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    # new_list = []
    # for num in number_list:
    #     if num % 2 != 0:
    #         new_list.append(num)
    # return new_list
    new_list = [num for num in number_list if num % 2 != 0]
    return new_list

# print all_odd(number_list)

# range a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    # new_list = []
    # for num in number_list:
    #     if num % 2 == 0:
    #         new_list.append(num)
    # return new_list
    new_list = [num for num in number_list if num % 2 == 0]
    
    return new_list

# print all_even(number_list)

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
    # new_list = []
    # for word in word_list:
    #     if len(word) >= 4:
    #         new_list.append(word)
    # return new_list
    return [word for word in word_list if len(word) >= 4]



# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    min_num = number_list[0]
    for num in number_list[1:]:
        if num < min_num:
            min_num = num

    return min_num



# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    max_num = number_list[0]
    for num in number_list:
        if num > max_num:
            max_num = num

    return max_num

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    # new_list = []
    # for num in number_list:
    #     new_list.append(float(num)/2)
    # return new_list

    new_list = [float(num)/2 for num in number_list]
    return new_list

# print halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    # new_list = []
    # for word in word_list:
    #     new_list.append(len(word))

    # return new_list

    return [len(word) for word in word_list]

print word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    running_total = 0
    for num in number_list:
        running_total = running_total + int(num)

    return running_total

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    running_total = 1
    for num in number_list:
        running_total = running_total * int(num)

    return running_total

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    new_string = ''
    for word in word_list:
        new_string = new_string + word

    return new_string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return float(sum_numbers(number_list)) / len(number_list)

