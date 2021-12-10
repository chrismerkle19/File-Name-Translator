import os
from os.path import exists
from pathlib import Path
from deep_translator import GoogleTranslator

print(
    "Do you want to translate the name of all files in this directory? \n(This may break programs that rely on the files being renamed)\n\n *CAN NOT UNDO! MAKE A BACKUP!* \n (y/n)\n")

check = input("Continue? (y/n):\n")

if check == ("y" or "Y"):

    entries = os.listdir(os.getcwd())

    for entry in entries:
        directory = Path(entry).parent
        file = Path(entry).name
        filename = Path(entry).stem
        extension = Path(entry).suffix
        translated = GoogleTranslator(source='auto', target='en').translate(filename)
        file_translated = (translated + extension)

        if not exists(file_translated):
            os.rename(entry, file_translated)
            print("Translated", entry, "to", file_translated)
        else:
            print("Skipping", entry, "(Might already be in English)")
            continue
    print("\n\n\nDone.")
else:
    exit()
