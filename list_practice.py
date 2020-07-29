list_numbers = [5, 1, 2, 3, 71, 57, 88]

# 1 SUM THE NUMBERS
# total = 0
# for num in list_numbers:
#     total += num
# print(total)

# print(sum(list_numbers))

# 2 LARGEST NUMBER
# list_numbers.sort()
# print(list_numbers[-1])

# print(max(list_numbers))


# 3 SMALLEST NUMBER
# list_numbers.sort()
# print(list_numbers[0])

# print(min(list_numbers))


# 4 EVEN NUMBERS
# for num in list_numbers:
#     if num % 2 == 0:
#         print(num)


# 5 POSITIVE NUMBERS
# numbers = [-5, -4, 0, 2, 4, 5, 7]

# for num in numbers:
#     if num > 0:
#         print(num)


# 6 POSITIVE NUMBERS II
# positive_numbers = []
# for num in numbers:
#     if num > 0:
#         positive_numbers.append(num)
# print(positive_numbers)


# 7 MULTIPLY A LIST
# numbers = [1, 2, 3, 99, 345, 631, 1002]
# factor = 9

# multiplied_numbers = []

# for number in numbers:
#     new_number = number * factor
#     multiplied_numbers.append(new_number)

# print(multiplied_numbers)


# 8 REVERSE
number_list = [1, 2, 3, 4]

print(number_list)
number_list.reverse()
print(number_list)


test_stuff = "Brittani"
string_list = []
for letter in test_stuff:
    string_list.append(letter)
print(string_list)
string_list.reverse()
pring(string_list)



a_string = "This is a string"
a = len(a_string) -1
b_string = ""
while a >= 0:
    b_string = b_string + a_string(a)
    a -= 1

print(b_string)