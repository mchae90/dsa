# def odd_or_even(n):
#     if n % 2 == 1:
#         print('odd')
#     else:
#         print('even')

# odd_or_even(2)

# def ask_name():
#     name = input('give me name')
#     print ('your name is ' + name)

# ask_name()

# def list_less_10(a):
#     x = []
#     for e in a:
#         if e < 10:
#             x.append(e)
#     return x

# print(list_less_10([1,4,23,11,4]))

# def find_divisor(n):
#     x = []
#     for e in range(1, n):
#         if n % e == 0:
#             x.append(e)
#     return x

# print(find_divisor(20))

# def list_overlap(l1, l2):
#     x = []
#     for e in l1:
#         if (e in l2) and (e not in x):
#             x.append(e)
#     return x

# print(list_overlap([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

# def is_palindrome(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False

# print(is_palindrome('dsa'))

# def even_elements(a):
#     return [n for n in a if n % 2 == 0]

# print(even_elements([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))

# class User:
#     def __init__(self, full_name, birthday):
#         self.name = full_name
#         self.birthday = birthday

#         name_pieces = full_name.split("")
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[-1]

# user = User("My Name", "121213")

