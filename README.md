# LL-1-
Integrantes:
  - Eduardo Hincapie
  - Josh Lopez
  - Miguel Suarez
  - Alejandra Vargas

# 📘 Análisis Sintáctico Descendente - Eliminación de Recursividad por la Izquierda, FIRST, FOLLOW y ASDR

Este repositorio contiene un análisis detallado de una gramática libre de contexto. Se realiza la eliminación de recursividad por la izquierda, el cálculo de conjuntos **FIRST**, **FOLLOW**, **PREDICCIÓN**, y una implementación de un **análisis sintáctico descendente recursivo (ASDR)** en Python.

---
## Ejercicio 1
## 📚 Gramática original


S → A B C  
S → D E  
A → dos B tres  
A → ε  
B → B cuatro C cinco  
B → ε  
C → seis A B  
C → ε  
D → uno A E  
D → B  
E → tres


## 🔁 Eliminación de recursividad por la izquierda
Se elimina la recursividad por la izquierda de la producción B → B cuatro C cinco, reescribiéndola como:

B → cuatro C cinco B | ε

La gramática resultante es:

S → A B C | D E  
A → dos B tres | ε  
B → cuatro C cinco B | ε  
C → seis A B | ε  
D → uno A E | B  
E → tres



---

## 🔤 Conjuntos FIRST

| No terminal | FIRST |
|-------------|--------|
| S           | {dos, uno, cuatro, seis, tres, ε} |
| A           | {dos, ε} |
| B           | {ε} |
| B'          | {cuatro, ε} |
| C           | {seis, ε} |
| D           | {uno, cuatro, ε} |
| E           | {tres} |

---

## 📍 Conjuntos FOLLOW

| No terminal | FOLLOW |
|-------------|--------|
| S           | {$} |
| A           | {cuatro, seis, tres} |
| B           | {cuatro, seis, tres} |
| B'          | {cuatro, seis, tres} |
| C           | {cinco} |
| D           | {tres} |
| E           | {$} |

---

## 🎯 Conjuntos de Predicción (PRED)

| Regla                      | PRED |
|---------------------------|------|
| A → dos B tres            | {dos} |
| A → ε                     | {cuatro, seis, tres} |
| B → B'                    | {cuatro, ε} |
| B' → cuatro C cinco B'    | {cuatro} |
| B' → ε                    | {cuatro, seis, tres} |
| C → seis A B              | {seis} |
| C → ε                     | {cinco} |
| D → uno A E               | {uno} |
| D → B                     | {tres} |
| E → tres                  | {tres} |

---

## ✅ ¿Es LL(1)?

Sí, la gramática es **LL(1)**, ya que los conjuntos de predicción (**PRED**) de las producciones de cada no terminal son disjuntos, cumpliendo la condición necesaria para ser analizada por un parser descendente predictivo.
---

## Ejercicio 2

## 📚 Gramática Original

S → B uno  
S → dos C  
S → ε  
S → S tres B C  
A → cuatro  
A → ε  
B → A cinco C seis  
B → ε  
C → siete B  
C → ε

## 🔢 Conjuntos FIRST

| No Terminal | FIRST                    |
|-------------|--------------------------|
| A           | { cuatro, ε }            |
| B           | { cuatro, cinco, ε }     |
| C           | { siete, ε }             |
| S           | { cuatro, cinco, uno, dos, ε } |

---

## 📍 Conjuntos FOLLOW

| No Terminal | FOLLOW                      |
|-------------|-----------------------------|
| S           | { $, tres }                 |
| A           | { cinco }                   |
| B           | { uno, siete, $, tres }     |
| C           | { seis, $, tres }           |

---

## 🔮 Conjuntos PREDICT (por producción)

### Para `S`:
- `S → B uno` → { cuatro, cinco, uno }
- `S → dos C` → { dos }
- `S → ε` → { $, tres }
- `S → S tres B C` → { cuatro, cinco, uno, dos, ε } ❌ (conflicto, recursiva a izquierda)

### Para `A`:
- `A → cuatro` → { cuatro }
- `A → ε` → { cinco }

### Para `B`:
- `B → A cinco C seis` → { cuatro, cinco }
- `B → ε` → { uno, siete, $, tres }

### Para `C`:
- `C → siete B` → { siete }
- `C → ε` → { seis, $, tres }

---

## ⚠️ ¿Es esta gramática LL(1)?

**No.**  
Existen **conflictos** en los conjuntos `PREDICT` del símbolo `S`, y además contiene **recursión por la izquierda** en la producción `S → S tres B C`, lo cual **viola los requisitos de una gramática LL(1)**.

---

## Ejercico 3

## 📌 Gramática original

S → A B C  
S → S uno  
A → dos B C  
A → ε  
B → C tres  
B → ε  
C → cuatro B  
C → ε

## ✂️ Eliminación de recursividad por la izquierda

Para el símbolo `S`, hay recursión por la izquierda directa:

S → S uno | A B C

Reescribimos con un nuevo símbolo S':
S  → A B C S'
S' → uno S' | ε

La gramática transformada queda:
S  → A B C S'
S' → uno S' | ε
A  → dos B C | ε
B  → C tres | ε
C  → cuatro B | ε

## 🔢 Conjuntos FIRST

| No Terminal | FIRST              |
|-------------|--------------------|
| S           | { dos, ε, cuatro } |
| S'          | { uno, ε }         |
| A           | { dos, ε }         |
| B           | { cuatro, ε }      |
| C           | { cuatro, ε }      |

---

## 📍 Conjuntos FOLLOW

| No Terminal | FOLLOW               |
|-------------|----------------------|
| S           | { $ }                |
| S'          | { $ }                |
| A           | { cuatro, $ }        |
| B           | { cuatro, $ }        |
| C           | { cuatro, tres, $ }  |

---

## 🔮 Conjuntos PREDICT

### Para `S`:
- `S → A B C S'` → { dos, cuatro, ε }

### Para `S'`:
- `S' → uno S'` → { uno }
- `S' → ε` → { $ }

### Para `A`:
- `A → dos B C` → { dos }
- `A → ε` → { cuatro, $ }

### Para `B`:
- `B → C tres` → { cuatro }
- `B → ε` → { cuatro, $ }

### Para `C`:
- `C → cuatro B` → { cuatro }
- `C → ε` → { cuatro, tres, $ }

---

## ⚖️ ¿Es esta gramática LL(1)?

✅ **Sí.**

- Cada conjunto `PREDICT` de una producción por símbolo es **disjunto**.
- No hay **recursión por la izquierda** ni ambigüedad.

**Por lo tanto, esta gramática es LL(1).**
