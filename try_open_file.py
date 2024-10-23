
with open('hej.txt', 'r', encoding='utf-8') as fil:
    data = fil.read()
    nummer = int(data)    


try:
    f = open('hej.txt')
    print('Vi har läst in filen!')

except FileExistsError as e:
    print(f'Filen existerar inte!! Felmeddelande {e}')

except FileNotFoundError as e:
    print(f'Filen hittades inte as {e}')

else:
    data = f.read()
    nummer = int(data)

finally:
    f.close()
    print('Vi ser till att alltid stänga filen ovasätt vad som går fel ovan!')

