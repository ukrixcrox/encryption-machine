#!/usr/bin/python3
import time
from database import pass_data
from passlib.hash import pbkdf2_sha256
from rich.progress import track
import pyfiglet

def encryption_machine():

  banner = pyfiglet.figlet_format("Encryption Machine")
  print(banner)

    #just a variable
  alph = "abcdefghijklmnopqrstuvwxyz"

  f = input("Enter to encode word=> ")

 # rot13 = lambda x: "".join([alph[(alph.find(c) + 13) %len(f)] for c in x])
  rot13 = lambda x: x.translate(str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"))
  i = rot13(f)

  for _ in track(range(50), description="Encrypting..."):
      time.sleep(0.02)

  print("Output of rot13=>", i)

  a = i.encode("utf-8")

  print("Encoded text=> ",a.hex())
  print("Activate the Error handling")

#password authentication
try:
  i = input("Please enter password to continue=> ")
  print()
 # print(pbkdf2_sha256.verify(i, pass_data()))
except:
   print('\n')
   print("An error has occured")
   exit(0)

#the .sleep is just there to make it look like the programm is actually doing something that take a second instead of just
#checking if two values are the same
#initialization loop
try:
  if pbkdf2_sha256.verify(i, pass_data()) == True:
    print("Correct")
    print("Starting Process...")
    time.sleep(1)
    encryption_machine()

  else:
    print("Incorrect")
    time.sleep(1)
    print("Cancelling Process...")
    time.sleep(1)
except:
    print('\n')
    print("An error has occured")
    time.sleep(1)
    print("Cancelling Process...")
    time.sleep(1)
    exit(0)
