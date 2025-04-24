tokens = []   # Lista de tokens de entrada
pos = 0       # Puntero actual

def match(expected):
    global pos
    if pos < len(tokens) and tokens[pos] == expected:
        pos += 1
    else:
        raise SyntaxError(f"Se esperaba '{expected}' en la posición {pos}, pero se encontró '{tokens[pos]}'")

def S():
    global pos
    start = pos

    try:  # S → B uno
        B()
        match('uno')
        return
    except:
        pos = start

    try:  # S → dos C
        match('dos')
        C()
        return
    except:
        pos = start

    try:  # S → ε
        return
    except:
        pos = start

    try:  # S → S tres B C (⚠️ recursión por la izquierda)
        S()
        match('tres')
        B()
        C()
        return
    except:
        pos = start
        raise SyntaxError(f"Error de sintaxis en S, posición {pos}")

def A():
    global pos
    start = pos

    try:  # A → cuatro
        match('cuatro')
        return
    except:
        pos = start

    try:  # A → ε
        return
    except:
        pos = start
        raise SyntaxError(f"Error de sintaxis en A, posición {pos}")

def B():
    global pos
    start = pos

    try:  # B → A cinco C seis
        A()
        match('cinco')
        C()
        match('seis')
        return
    except:
        pos = start

    try:  # B → ε
        return
    except:
        pos = start
        raise SyntaxError(f"Error de sintaxis en B, posición {pos}")

def C():
    global pos
    start = pos

    try:  # C → siete B
        match('siete')
        B()
        return
    except:
        pos = start

    try:  # C → ε
        return
    except:
        pos = start
        raise SyntaxError(f"Error de sintaxis en C, posición {pos}")

tokens = ['dos', 'siete', 'cuatro', 'cinco', 'seis']
pos = 0

try:
    S()
    if pos == len(tokens):
        print("Cadena válida")
    else:
        print("Tokens sobrantes")
except SyntaxError as e:
    print("Error de sintaxis:", e)
