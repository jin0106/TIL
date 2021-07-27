# hw 1
# def count_vowels(word):
#     vowels = 'aeiou'
#     total = 0
#     for vowel in vowels:
#         total += word.count(vowel)
    
#     return total

# print(count_vowels('apple'))
# print(count_vowels('banana'))
# print(count_vowels('bananaeeeeiiou'))


# hw3
# def only_square_area(value1, value2):
#     # 1 이중 for 사용
#     # area_list = []
#     # for v1 in value1:
#     #     for v2 in value2:
#     #         if v1 == v2:
#     #             area_list.append(v1**2)
    

#     # 2 list comprehension
#     area_list = [v1**2 for v1 in value1 for v2 in value2 if v1 == v2]

#     return area_list

# print(only_square_area([32, 55, 63], [13, 32, 42, 55]))


# ws 1
# def get_dict_avg(score_dict):
#     # 1
#     # total = 0
#     # length = 0
#     # for score in score_dict.values():
#     #     total += score
#     #     length += 1
    
#     # return total / length

#     # 내장함수 버전
#     return sum(score_dict.values()) / len(score_dict)


# avg = get_dict_avg({
#     'python': 80,
#     'algorithm': 90,
#     'django': 89, 
#     'web': 83,
# })
# print(avg)


# ws 2
# def count_blood(blood_list):
#     blood_dict = {}
#     # 1
#     # for blood in blood_list:
#     #     if blood_dict.get(blood):
#     #         blood_dict[blood] += 1
#     #     else:
#     #         blood_dict[blood] = 1

#     # 2
#     for blood in blood_list:
#         blood_dict[blood] = blood_dict.get(blood, 0) + 1

#     return blood_dict

# result = count_blood([
#     'A', 'B', 'A', 'O', 'AB', 'AB',
#     'O', 'A', 'B', 'O', 'B', 'AB',
#     ])

# print(result)