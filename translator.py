import os
from os.path import exists
from pathlib import Path
from deep_translator import GoogleTranslator


filepath = input("Enter Path of the file(s) to translate:\n")
directory = Path(filepath).parent
file = Path(filepath).name
filename = Path(filepath).stem
extension = Path(filepath).suffix
translated = GoogleTranslator(source='auto', target='en').translate(filename)


if not exists(filepath):
    print("File does not exist. Check inout and try again.")
else:
    newname = (translated + extension)
    if not exists(newname):
       os.rename(filepath, newname)
    else:
        print("File with specified name already exists, choose another name.\n")