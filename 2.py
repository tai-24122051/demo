# # def dem(n):
# #     count_max = 0
# #     score = n[0]
# #     for i in n:
# #         if n.count(i) > count_max:
# #             score = i
# #             count_max = n.count(i)
# #     return score
# #
# # def max_number(n):
# #     left = 0
# #     lst_max = [n[0]]
# #     for right in range(0,len(n)):
# #         if n[right] < 50:
# #             left = right + 1
# #         lst = n[left:right + 1]
# #         if len(lst) > len(lst_max):
# #             lst_max = lst
# #     return lst_max
# #
# #
# #
# #
# #
# # n = list(map(int,input().split()))
# # result = dem(n)
# # print(result)
# # print(max_number(n))
# #
# # a = [[1,5,8],
# #      [4,3,1],
# #      [6,5,2]]
# # for i in range(len(a)):
# #     result = (a[i][i:])
# #     print(' ' * 2 * i, end='')
# #     for x in result:
# #         print(x, end = ' ')
# #     print()
# #
# #
# # for j in range(len(a)):
# #     result =a[j][0:j + 1]
# #     for y in result:
# #         print(y,end = ' ')
# #     print()
#
# # matrix = [[1,5,8],
# #           [4,3,1],
# #           [6,5,2]]
# # matrixT = []
# # for i in range(len(matrix)):
# #     new_row = []
# #     for row in matrix:
# #         new_row.append(row[i])
# #     matrixT.append(new_row)
# # print(matrixT)
#
# # with open('text','r',encoding='utf-8') as fo:
# #     read_content = fo.readlines()
# #     result = []
# #     for i in read_content:
# #         if i != '\n':
# #             for j in i.split():
# #                 if j[-1].isalpha() and j not in result:
# #                     result.append([j,1])
# #                 elif not j[-1].isalpha() and j[0:-1] not in result:
# #                     result.append([j[0:-1],1])
# #                 elif j[-1].isalpha() and j in result:
# #                     result[result.index(j)][1] += 1
# #                 else:
# #                     result[result.index(j[0:-1])][1] += 1
# #     print(result)
#
# def count_occurrences(file_name):
#     with open(file_name,'r', encoding ='utf-8') as fo:
#         read_content = fo.read()
#         count ={}
#         lst = []
#         for words in read_content.split():
#             clean = ''
#             for word in words.lower():
#                 if word.isalpha() or word == "-":
#                     clean += word
#             if clean:
#                 count[clean] = count.get(clean,0) + 1
#         for key,value in count.items():
#             lst.append([key,value])
#         print(lst)
#
# def word_appear_most(file_name):
#     with open(file_name,'r',encoding = 'utf-8') as fo:
#         read_content = fo.read()
#         count = {}
#         max_c = 0
#         for words in read_content.split():
#             clean = ''
#             for word in words.lower():
#                 if word.isalpha():
#                     clean += word
#             if len(clean) > 0:
#                 count[clean] = count.get(clean, 0) + 1
#         for value,key in count.items():
#             if key > max_c:
#                 result = value
#                 max_c = key
#         print(result, max_c)
#
# def word_appear_less(file_name):
#     with open(file_name,'r',encoding = 'utf-8') as file:
#         read_content = file.read()
#         count = {}
#         min_c = float('inf')
#         for words in read_content.split():
#             clean = ''
#             for word in words.lower():
#                 if word.isalpha():
#                     clean += word
#             if len(clean) > 0:
#                 count[clean] = count.get(clean, 0) + 1
#         for value,key in count.items():
#             if key < min_c:
#                 min_c = key
#                 result = value
#     print(result)
# def count_end(file_name, k):
#     with open(file_name,'r',encoding = 'utf-8') as file:
#         read_content = file.read()
#         lst = []
#         for words in read_content.split():
#             clean = ''
#             for word in words.lower():
#                 if word.isalpha():
#                     clean += word
#             if len(clean) > 0 and clean not in lst:
#                 lst.append(clean)
#         count = 0
#         while count < len(lst):
#             if lst[count][-1] == k:
#                 count += 1
#             else:
#                 lst.remove(lst[count])
#
#         print(count, lst)
# def count_letter(file_name):
#     with open(file_name,'r',encoding = 'utf-8') as file:
#         count = {}
#         read_content = file.read()
#         for letter in read_content.lower():
#             if letter.isalpha():
#                 count[letter] = count.get(letter, 0) + 1
#         print(count)
# def count_in(file, n, k):
#     with open(file_name, 'r', encoding = 'utf-8') as file:
#         read_content = file.read()
#         count = {}
#         res = []
#         for words in read_content.split():
#             clean = ''
#             for word in words:
#                 if word.isalpha() or word == '-':
#                     clean += word
#             if len(clean) > 0:
#                 count[clean] = count.get(clean, 0) + 1
#         for value,key in count.items():
#             if n <= key <= k:
#                 res.append([value, key])
#         print(res)
#
# def write_line(file_name,n,k):
#     with open(file_name,'r', encoding = ' utf-8') as file:
#         read_content = file.readlines()
#         result = ''
#         i = 0
#         count = 0
#         while i <= k:
#             if read_content[count] != '\n':
#                 i += 1
#             if n <= i <= k:
#                 result += read_content[count]
#             count += 1
#     with open("output.txt",'w', encoding = 'utf-8') as out:
#         out.write(result)
#
# def appear_immediately(file_name, target):
#     with open(file_name,'r',encoding = 'utf-8') as file:
#         read_content = file.read().lower()
#         # Tạo một từ điển để đếm số lần xuất hiện
#         count = {}
#         words = read_content.split()
#
#         for i in range(len(words)):
#             clean = ''.join(c for c in words[i] if c.isalpha() or c == '-')
#
#             # Nếu từ đã được làm sạch bằng target
#             if clean == target:
#                 if i != 0:  # Đảm bảo có từ trước từ target
#                     prev_word = ''.join(c for c in words[i - 1] if c.isalpha() or c == '-')
#                     count[prev_word] = count.get(prev_word, 0) + 1
#
#         # Tìm từ xuất hiện nhiều nhất
#         if count:
#             result = max(count, key=count.get)
#             print(result, count)
#         else:
#             print(None)
#
# def line_contain(file_name, tar):
#     with open(file_name,'r', encoding = 'utf-8') as file:
#         read_content = file.readlines()
#         result = ''
#         for line in  read_content:
#             if tar in line.lower():
#                 result += line
#         print(result)
#
# def insert_line(file_name, tar, n):
#     with open(file_name, 'r', encoding = 'utf-8') as file:
#         read_content = file.readlines()
#         result = ''
#         i = 0
#         count = 1
#         while i < len(read_content):
#             if count  == n:
#                 result += tar
#                 result += read_content[i]
#                 count += 1
#             elif read_content[i] != '\n':
#                 result += read_content[i]
#                 count += 1
#             i += 1
#     print(result)
#
# def delete_line(file_name, n):
#     with open(file_name, 'r', encoding = 'utf-8') as file:
#         read_content = file.readlines()
#         res = ''
#         i = 0
#         count = 1
#         while i < len(read_content):
#             if count == n:
#                 count += 1
#                 i += 1
#                 continue
#             elif read_content[i] != '\n':
#                 res += read_content[i]
#                 count += 1
#             i += 1
#     print(res)
#
# def write_ele(s):
#     with open('output2.txt', 'w', encoding = 'utf-8') as file:
#         for i in s:
#             file.write(i + '\n')
#
#
# if __name__ == "__main__":
#     file_name = "D:/Tai/text.txt"
#     # count_occurrences(file_name)
#     # word_appear_less(file_name)
#     # word_appear_most(file_name)
#     # count_end(file_name, 'k')
#     # count_letter(file_name)
#     # count_in(file_name, 2, 5)
#     # write_line(file_name,2,5)
#     # appear_immediately(file_name, 'pikachu')
#     # line_contain(file_name, 'pikachu')
#     # insert_line(file_name, 'huy oc cho vai ca lol', 4)
#     # delete_line(file_name, 3)
#     # write_ele(['anh thich em','em khong thich anh'])