#!bin/python3
import time
from database import pass_data
from passlib.hash import pbkdf2_sha256

def encryption_machine():
  import pyfiglet

  banner = pyfiglet.figlet_format("Encryption Machine")
  print(banner)

    #just a variable
  alph = "abcdefghijklmnopqrstuvwxyz"

      #message
  f = input("Enter to encode word=> ")

  rot13 = lambda x: "".join([alph[(alph.find(c) + 13) %len(f)] for c in x])
      
  i = rot13(f)

  print("Output of rot13=>", i)

  a = pyfiglet.figlet_format(i, font='hex')

  print("Encoded text=> ", a)

  #print("Number of letters moved in rot13:",len(f))


#password authentication
try:
  i = input("Please enter password to continue=> ")

  print(pbkdf2_sha256.verify(i, pass_data()))
except:
  print('\n')
  print("An error has occured")

#the .sleep is just there to make it look like the programm is actually doing something that take a second instead of just 
#checking if two values are the same

#initialization loop 
try:
  if pbkdf2_sha256.verify(i, pass_data()) == True:
    time.sleep(1)
    encryption_machine()

  else:
    # time.sleep(1)
    # print("Wrong password")
    time.sleep(1)
    print("Cancelling Process...")
    time.sleep(1)
except:
  print('\n')
  print("An error has occured")
  time.sleep(1)
  print("Cancelling Process...")
  time.sleep(1)