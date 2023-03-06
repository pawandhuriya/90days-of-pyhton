#programing Dictonary 
# Syntax dict={"key:value"} 
# programing_dict={"bug":"Programing bug","Fucntion":"Python fucntion"}
# print(programing_dict["bug"])

# # we cna edit as well
# programing_dict["bug"]="we can change the value "

# for key in programing_dict:
#     print(key)
#     print(programing_dict["bug"])

#Excerise 9.1
# student_scores={"Harry":81,"Ran":78,"Herison":99,"Draco":75}

# #create an empty dict called student_grades
# student_grades={}
# # condition for scores
# for student in student_scores:
#     score=student_scores[student]
#     if score>90:
#         student_grades[student]="Outstanding"
#     elif score>80:
#         student_grades[student]="Exceeds Expect"
#     elif score>50:
#         student_grades[student]="Good"
# print(student_grades)
            

# Dictonry for list exceriseze

# travel_log=[{"counrty":"France","visits":"12","cities":["paris","lille","Dijion"]},
# {"counrty":"Germani","visits":"14","cities":["Berlin","Hustomne","chalna "] }]
# print(travel_log)

#excersize 9.2

bid={}
bidding_finished=False
while not bidding_finished:
    name=input("Whats your name?",)
    price=input("enter the bid amount:- $")
    bid[name]=price
    input("")