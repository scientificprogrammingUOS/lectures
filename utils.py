from tqdm import tqdm_notebook
from time import sleep
from IPython.display import display, update_display

def count_down(minutes):
    
    for j in tqdm_notebook(range(60 * minutes), bar_format=None):
        sleep(1)
        

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