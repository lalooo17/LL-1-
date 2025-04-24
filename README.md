# LL-1-
# 📘 Análisis Sintáctico Descendente - Eliminación de Recursividad por la Izquierda, FIRST, FOLLOW y ASDR

Este repositorio contiene un análisis detallado de una gramática libre de contexto. Se realiza la eliminación de recursividad por la izquierda, el cálculo de conjuntos **FIRST**, **FOLLOW**, **PREDICCIÓN**, y una implementación de un **análisis sintáctico descendente recursivo (ASDR)** en Python.

---

## 📚 Gramática original

```txt
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
