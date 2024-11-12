import functs
import settings
from ui_tkinter import *
from functs import *

print('Hi')

functs.downloadandload()
log_if_debbuging('dnlal_done')
functs.do_things_with_variables()

print('Hi again')

if settings.debug == 1:
    # Print the arrays to verify
    print("First parts:", functs.first_send())
    print("Second parts:", functs.second_send())
    print("Third parts:", functs.third_send())
    print("Fourth parts:", functs.fourth_send())

arr = ["Type the word out", "Multiple choice"]
print(arr)
functs.main(multiple_choice("Please select a Mode", arr))