#this microbit code should display a happy face if you press button a but a sad face if you press b
#BUt there is an error! Can you solve it?
from microbit import*
while True:
  if button_a.is_pressed():
    display.show(Image.HAPPY)
    sleep (3000)
    display.clear()
  if button-b.is_pressed():
    display.show(Image.SAD)
    sleep (3000)
    display.clear()
