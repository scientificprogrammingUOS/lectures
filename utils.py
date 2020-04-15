from tqdm import tqdm_notebook
from time import sleep
from IPython.display import display, update_display
import os

def count_down(minutes):
    if not os.environ.get("RUNALL"):
        for j in tqdm_notebook(range(60 * minutes)):
            sleep(1)
    else:
        print(f"You have {minutes} minutes time for the exercise.")
        

# class T:
#     def __init__(self):
#         self.val = 1
        
#     def _repr_html_(self):
#         return "<b>" + str(self.val) + "</b>"
        
# def fancy_countdown():
#     t = T()
#     handle = display(t, display_id=True)
#     for i in range(10):
#         sleep(1)
#         t.val += 1
#         update_display(t, display_id=handle.display_id)
