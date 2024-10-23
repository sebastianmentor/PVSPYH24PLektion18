def kontrollera_längden_på_namnet(namn:str) -> int:
    längd = len(namn)
    if längd < 2: raise ValueError('Ett namn måste ha minst två bokstäver!')
    
    return len(namn)