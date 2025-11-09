from pyautogui import write, press
from time import sleep
amount_of_message = int(input("How many messages?: "))
message = input("What is the message?: ")
print("You have 10 seconds to get ready (put your click thing in the typing bar)")
sleep(10)
for _ in range(amount_of_message):
    write(message)
    press("enter")