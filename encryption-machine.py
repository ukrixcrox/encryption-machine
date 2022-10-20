#!/usr/bin/python3
import time
from rich.progress import track
from rich import print
import pyfiglet

banner = pyfiglet.figlet_format("Encryption Machine")
print(banner)

def encryption_machine():

  f = input("Enter to encode word=> ")

  rot13 = lambda x: x.translate(str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"))
  i = rot13(f)

  #print("Output of rot13=>", i)
  a = i.encode("utf-8")

  print(f"[blue]Encoded text=> {a.hex()} [/blue]")

#initialization loop
try:
  while True:
    encryption_machine()
except KeyboardInterrupt:
  print("\n[red]Stopping Programm[/red]")

except:
    print('\n')
    print("An error has occured")
    time.sleep(1)
    print("Cancelling Process...")
    time.sleep(1)
    exit(0)