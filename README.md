# LL-1-
# 📘 Análisis Sintáctico Descendente - Eliminación de Recursividad por la Izquierda, FIRST, FOLLOW y ASDR

Este repositorio contiene un análisis detallado de una gramática libre de contexto. Se realiza la eliminación de recursividad por la izquierda, el cálculo de conjuntos **FIRST**, **FOLLOW**, **PREDICCIÓN**, y una implementación de un **análisis sintáctico descendente recursivo (ASDR)** en Python.

---

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
