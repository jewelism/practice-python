# -*- coding: utf-8 -*- #

# tmp_input = input('input some string')
# 
# tmp = ""
# for word in tmp_input.upper().split():
#     tmp += word[0]
# 
# print(tmp)

sentence = input('input : ')

table = {'alpha':0, 'digit':0, 'space':0}

for i in sentence:
    if i.isalpha():
        table['alpha'] += 1
    if i.isdigit():
        table['digit'] +=1
    if i.isspace():
        table['space'] +=1
print(table)