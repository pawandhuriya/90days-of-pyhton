# Number Guessing game
from random  import randint
def start():
 print(f" Welcome to number guessing game! \n "," Thinking Number in between 1 and 100")
 type=input(str(" Choose a difficulty :'easy' or 'hard' :-"))
answer=randint(1,100)

start()

count=10
counts=5

def easy():
  if type=='easy':
    print(f"You have 10 attempts remaining to guess the number")
 
# def hard():
#   if type=='hard':
#     print(f"You have 5 attempts remaining to guess the number")
  
# def hardone():


def easyone():
     guess=int(input("Make a guess: "))
     if guess>answer:
      print(f"Too high")
      global count
      count-=1
      print(f"You have {count} attempt remaning")
      return easyone()
     elif guess<answer:
      print(f"Too Low")
      # global count
      count -=1
      print(f"You have {count} attempt remaning")
     return easyone()
        # else:
        #   return
          
easy()

easyone()