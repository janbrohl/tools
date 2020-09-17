'''
Skript, das im Ordner ORDNER alle txt Dateien *.txt öffnet und für jede Zeile darin einen qr Code 
*_01.png, *_02.png, ... erstellt
'''

import qrcode
import pathlib

ORDNER = r".\demo"
ordner_pfad = pathlib.Path(ORDNER)

for pfad in ordner_pfad.glob('*.txt'):
    stem = pfad.stem  # stem von "a.txt" ist "a"
    with pfad.open(
            'rt',
            encoding='utf-8-sig') as f:  # In Notepad speichern als Unicode
        zeilennummer = 0
        for zeile in f:
            zeilennummer += 1
            bild_pfad = pfad.with_name(f'{stem}_{zeilennummer:02}.png')
            img = qrcode.make(zeile.strip())
            img.save(bild_pfad)
