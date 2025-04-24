tokens = ['dos', 'cuatro', 'tres', 'cuatro', 'tres', 'uno']
pos = 0

def match(t):
    global pos
    if pos < len(tokens) and tokens[pos] == t:
        pos += 1
    else:
        raise SyntaxError(f"Se esperaba '{t}' pero se encontró '{tokens[pos] if pos < len(tokens) else 'EOF'}'")

def S():
    A()
    B()
    C()
    Sp()

def Sp():
    if pos < len(tokens) and tokens[pos] == 'uno':
        match('uno')
        Sp()
    else:
        pass  # ε

def A():
    if pos < len(tokens) and tokens[pos] == 'dos':
        match('dos')
        B()
        C()
    else:
        pass  # ε

def B():
    global pos
    current_pos = pos
    try:
        C()
        match('tres')
    except SyntaxError:
        pos = current_pos  # backtrack
        pass  # ε


def C():
    if pos < len(tokens) and tokens[pos] == 'cuatro':
        match('cuatro')
        B()
    else:
        pass  # ε

try:
    S()
    if pos == len(tokens):
        print("✅ Cadena válida")
    else:
        print("❌ Tokens sobrantes en la posición", pos, "→", tokens[pos:])
except SyntaxError as e:
    print("❌ Error:", e)
