#time module is used in this project
from time import *
import random as r
strings=["my name is mauli himmat dudhat","what is your name and adress","where are you from"] #here you can take your own list also,this is only for sample case .
str1=r.choice(strings)
print("TYPING SPEED:")
print(str1)
print()

t1=time()
takeinput=input("Enter: ")
t2=time()

def wrong(str2,uip): #used for return time required for the typing and speed.uip here userinput.
    mis=0
    for i in range(len(str2)):
        try:
            if(str2[i]!=uip[i]):
                mis+=1
        except:
            mis += 1
    return mis


def t_delay(start_time,end_time,userinput):
    t_diff=end_time-start_time
    print("Time Required:",t_diff)

    speed=len(userinput)/t_diff
    return speed

print("SPEED:(words/sec)")
print()
print(t_delay(t1,t2,takeinput))
print()
print("errors:",wrong(str1,takeinput))






