def devide(a, b):
    return a/b


print('Räkna ut vad a/b blir:')
a = input("Ange a: ")
b = input("Ange b: ")

try:
    a = float(a)
    b = float(b)
    value = devide(a,b)
    devide(a, devide)

except ValueError as e:
    print(f"Gick inte att konverter till tal i datorn. felmeddelande: {e}")

except TypeError as e:
    print(f"Något har gått riktigt galet!! {e}")

except ZeroDivisionError as e:
    print(f"Du skrev 0 för b, går inte att dela med noll!!!")
