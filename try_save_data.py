
info = ['namn', 'ålder', 'längd']

try:
    f = open('save.txt')
    print('Vi har läst in filen!')

except FileNotFoundError as e:
    print('Filen hittades inte!')
    print('Skriver nuvarande data till krasch.txt')
    
    with open('krasch.txt', 'w', encoding='utf-8') as f:
        f.write(str(info))

else:
    f.write(info)