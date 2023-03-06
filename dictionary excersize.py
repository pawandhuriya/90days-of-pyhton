# key=['Ten','Twenty','Thirty']
# values=[10,20,30]

# output=dict(zip(key,values))
# print(output)

# res_dict=dict()
# for i in range(len(key)):
#     res_dict.update({key[i]:values[i]})
#     print(res_dict)

# ex-2

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# # dict3 = {**dict1, **dict2}
# # print(dict3)
# dict3=dict1.copy()
# dict3.update(dict2)
# print(dict3)

# #ex-3
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }# understand how to located the nested key
# # sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# # sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# # sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}
# print(sampleDict['class']['student']['marks']['history'])

# ex-5
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
out_dict=dict.fromkeys(employees,defaults)
print(out_dict)


