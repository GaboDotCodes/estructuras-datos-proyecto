import json
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def getJsonFromFile():
  Tk().withdraw()
  filename = askopenfilename(filetypes=[("JSON files", ".json")])
  with open(filename, 'r') as f:
    data = json.load(f)
  return data