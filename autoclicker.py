from pyautogui import click
from time import sleep
time_gap = float(input("What is the time gap between each click?: "))
print("Get ready for the clicker to activate in 10 secs")
sleep(10)
while True:
    sleep(time_gap)
    click()