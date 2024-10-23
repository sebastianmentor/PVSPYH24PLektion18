class OmyndigError(Exception):
    """Ett fel om åldern är mellan 0 och 17"""
    pass

def köp_på_systembolaget(ålder: int) -> str:
    if 0<= ålder <= 17:
        raise OmyndigError('Åldern är omyndig')
    
    return 'Välkommen! Bara att börja handla'


def kontrollera_ålder(ålder: int):
    # if not isinstance(ålder, int): 
    #     raise TypeError('En ålder måste vara av typen int!!')
    if ålder<0:
        raise ValueError('Åldern får inte vara negativ!')
    else:
        print('Du har en korrekt ålder!')


# kontrollera_ålder('-6')
# tal = '-5'

# try:
#     kontrollera_ålder(tal)
# except ValueError as e:
#     print(f'Felaktig ålder! {e}')

# except TypeError as e:
#     print(f'Felaktig typ skickad till kontrollera_ålder(), ska vara av typ int men var av typ {type(tal)}')
#     print(e)


try:
    köp_på_systembolaget(10)
except OmyndigError as e:
    print('Vänligen lämna systembolaget då du inte har åldern inne!')
    print(e)

