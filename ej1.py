def match(expected_token):
    global pos, current_token
    if current_token == expected_token:
        pos += 1
        current_token = tokens[pos]
    else:
        raise SyntaxError(f"Se esperaba '{expected_token}' pero se encontró '{current_token}'")

def S():
    if current_token == "dos" or current_token in {"cuatro", "seis", "tres"}:
        A()
        B()
        C()
    elif current_token == "uno" or current_token == "cuatro":
        D()
        E()
    else:
        raise SyntaxError("Error en S")

def A():
    if current_token == "dos":
        match("dos")
        B()
        match("tres")
    elif current_token in {"cuatro", "seis", "tres"} or current_token is None:
        pass
    else:
        raise SyntaxError("Error en A")

def B():
    Bp()

def Bp():
    if current_token == "cuatro":
        match("cuatro")
        C()
        match("cinco")
        Bp()
    elif current_token in {"cuatro", "seis", "tres", None}:
        pass
    else:
        raise SyntaxError("Error en B'")

def C():
    if current_token == "seis":
        match("seis")
        A()
        B()
    elif current_token in {"cinco", "tres", None}:
        pass
    else:
        raise SyntaxError("Error en C")

def D():
    if current_token == "uno":
        match("uno")
        A()
        E()
    elif current_token == "cuatro":
        B()
    else:
        raise SyntaxError("Error en D")

def E():
    if current_token == "tres":
        match("tres")
    else:
        raise SyntaxError("Error en E")
    
def parse(input_tokens):
    global tokens, pos, current_token
    tokens = input_tokens + ["$"]
    pos = 0
    current_token = tokens[pos]
    S()
    if current_token != "$":
        raise SyntaxError("Input no completamente consumido")
    print("Cadena aceptada correctamente.")

if __name__ == "__main__":
    prueba = ["dos", "cuatro", "seis", "dos", "tres", "cinco", "tres"]
    parse(prueba)
