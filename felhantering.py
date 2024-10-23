try:
    x = int(input("Skriv ett tal: "))
    result = 10 / 0
except ValueError:
    print("Ogiltigt värde!")
except ZeroDivisionError:
    print("Division med noll!")
except Exception as e:
    print(f"Annat fel: {e}")

print("Programmet fortsätter här.")
