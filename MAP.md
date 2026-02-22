# 🧭 MAP.md — Python Garden · Cyber Archives
## python04_cyber_archives — Safe I/O & Resilient Programs

Este documento es mi mapa de aprendizaje y diseño.  
Representa cómo evoluciona mi forma de pensar la interacción entre un programa Python y el mundo exterior.

---

## 📁 Project Structure

```text
python04_cyber_archives
|
+-- ex0
+-- ex1
+-- ex2
+-- ex3
+-- ex4
+-- tools
+-- README.md
+-- MAP.md
+-- .gitignore
```

---

## 🌱 Idea central

```text
MUNDO EXTERIOR
       |
       v
PROGRAMA SE PROTEGE
```

---

## 🟢 ex0 — Ancient Text Recovery

```text
+----------------------+
|        main()        |
+----------------------+
| open()               |
| read()               |
| try / finally        |
| close()              |
+----------------------+
```

Flujo:

```text
ARCHIVO  --->  LEER  --->  MOSTRAR
```

---

## 🟡 ex1 — Archive Creation

```text
+----------------------+
|        main()        |
+----------------------+
| get_data()           |
| open("w")            |
| write()              |
| close()              |
+----------------------+
```

Flujo:

```text
DATOS  --->  ESCRIBIR  --->  ARCHIVO
```

---

## 🔵 ex2 — Stream Management

```text
            USUARIO
               |
               v
            stdin
               |
               v
+----------------------------+
|          PROGRAMA          |
+----------------------------+
| stdout  -> mensajes        |
| stderr  -> alertas         |
+----------------------------+
```

---

## 🟣 ex3 — Vault Security

```text
+------------------------------+
|        with open()           |
+------------------------------+
| adquirir recurso             |
| usar recurso                 |
| liberar automáticamente      |
+------------------------------+
```

Principio:

```text
ADQUIRIR -> USAR -> LIBERAR
```

---

## 🔴 ex4 — Crisis Response

```text
+-----------------------------------+
|        crisis_handler()           |
+-----------------------------------+
| try                               |
|   with open()                     |
| except FileNotFoundError          |
| except PermissionError            |
| except Exception                  |
| finally -> sistema estable        |
+-----------------------------------+
```

Principio:

```text
CRISIS  !=  CAÍDA DEL SISTEMA
```

---

## 🧠 Evolución Global

```text
        +------------------+
        |  Mundo exterior  |
        +------------------+
                  |
                  v
        +------------------+
        |  ex0: leer       |
        +------------------+
                  |
                  v
        +------------------+
        |  ex1: escribir   |
        +------------------+
                  |
                  v
        +------------------+
        |  ex2: streams    |
        +------------------+
                  |
                  v
        +------------------+
        |  ex3: with       |
        +------------------+
                  |
                  v
        +------------------+
        |  ex4: resiliencia|
        +------------------+
```

---

## 🎯 Objetivo final

Diseñar programas que:

- interactúan con el mundo exterior
- protegen recursos
- gestionan errores
- nunca colapsan

