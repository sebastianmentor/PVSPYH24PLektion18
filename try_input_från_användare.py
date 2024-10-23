while True:
    print('1. Skriv in ett tal: ')
    print('2. Skriv in tilltalsnamn och ålder: ')
    print('3. Avsluta')

    meny_val = input('Ange val: ')

    if meny_val == '1':
        try: 
            # float -> 4 , 3.0, -2, -3.1 -0, ...
            tal = float(input('Ange ett reelt tal: '))
  
        except ValueError as e:
            print('Ogiltligt tal!')
            print(f'Programmet gav det här felet {e}')

        else:
            print(f'Du skrev in {tal} som är ett giltligt tal')

    
    elif meny_val == '2':
        namn_och_ålder = input('Ange namn och ålder på samma rad med mellanslag: ')
        namn_och_ålder = namn_och_ålder.split(' ')
        # try:
        #     namn, ålder = namn_och_ålder.split(' ')
        #     ålder = int(ålder)
        # except ValueError as e:
        #     print(e)
        # else:
        #     if ålder >= 0:
        #         print(f'Ditt namn är {namn} och du är {ålder} år gammal')
        #     else:
        #         print('Inte giltlig ålder')

        if not len(namn_och_ålder) == 2:
            print('Mer än bara namn och ålder!')

        else:
            namn = namn_och_ålder[0]
            ålder = namn_och_ålder[1]

            if not ålder.isdigit():
                print('Inte en giltlig ålder')

            elif int(ålder)>=0:
                print(f'Ditt namn är {namn} och du är {ålder} år gammal')

            else:
                print(f'Måste ha en positiv ålder!')


            # try:
            #     ålder = int(ålder)
            # except ValueError as e:
            #     print('Inte en giltlig ålder')
            # else:
            #     if ålder >= 0:
            #         print(f'Ditt namn är {namn} och du är {ålder} år gammal')
            #     else:
            #         print(f'Måste ha en positiv ålder!')


    elif meny_val == '3':
        break

    else:
        print('Ogiltligt val')
        