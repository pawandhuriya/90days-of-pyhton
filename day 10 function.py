# function with output
#  def my_fucntion()--
# def format_name():
#     f_name=input("Enter the first name ")
#     l_name=input("Enter the last name ")
#     print("welcome",f_name,l_name)

# format_name()
# ----------
# def is_leap(year):
#     if year %4==0:
#         if year%100==0:
#             if year%400==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
    
# def day_in_month(year,month):
#     if month>12 or month<1:
#         print("Invalid inpur")
#     month_days=[31,28,31,30,31,30,31,30,31,30,31,30]        
#     if is_leap(year) and month==2:
#         return 29
#     return month_days[month-1]

# #year and month
# year=int(input("Enter year: "))
# month=int(input("Enter the months: ")) 
# days=day_in_month(year,month)
# print(days)

# -----Excerisize----- calculator
def add(n1,n2):
    return n1+n2

def mult(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def subs(n1,n2):
    return n1-n2




operation= {
    "+":add,
    "-":subs,
    "*":mult,
    "/":subs
}

def cal():
    num1=int(input("first number: "))
    for symbol in operation:
      print(symbol)
    should_con=True
    while should_con:
     operation_symbol=input("Pick the symbol: ")
     cal_function=operation[operation_symbol]
     num2=int(input("secound number: "))
     answer=cal_function(num1,num2)

     print(f"{num1} {operation_symbol} {num2} ={answer}")
     if input(f"Do you want to continoue with {answer} ? :if yes press 'y' or no 'n' to exist : ")=='y':
         num1=answer
     else:
          should_con=False
cal()
  







