from random import randint

def goofitize(text: str):
    text = list(text)
    n_text = []
    for i in text:
        goof_coeff = randint(0,1)
        if goof_coeff == 1:
            n_text.append(i.upper())
        else:
            n_text.append(i.lower())
    return "".join(n_text)
