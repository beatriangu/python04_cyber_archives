# 🧭 MAP.md — Python Garden · Cyber Archives
## python04_cyber_archives — Safe I/O & Resilient Programs

Este documento es mi mapa de aprendizaje y diseño.  
Representa cómo evoluciona mi forma de pensar la interacción entre un programa Python y el mundo exterior.

---

## 📁 Project Structure

```text
python04_cyber_archives/
|
+-- ex0/
+-- ex1/
+-- ex2/
+-- ex3/
+-- ex4/
+-- tools/
+-- README.md
+-- MAP.md
+-- .gitignore
🌱 Idea central
MUNDO EXTERIOR
       |
       v
PROGRAMA SE PROTEGE
🟢 ex0 — Ancient Text Recovery
+----------------------+
|        main()        |
+----------------------+
| open()               |
| read()               |
| try / finally        |
| close()              |
+----------------------+

Flujo:

ARCHIVO  --->  LEER  --->  MOSTRAR
🟡 ex1 — Archive Creation
+----------------------+
|        main()        |
+----------------------+
| get_data()           |
| open("w")            |
| write()              |
| close()              |
+----------------------+

Flujo:

DATOS  --->  ESCRIBIR  --->  ARCHIVO
🔵 ex2 — Stream Management
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
🟣 ex3 — Vault Security
+------------------------------+
|        with open()           |
+------------------------------+
| adquirir recurso             |
| usar recurso                 |
| liberar automáticamente      |
+------------------------------+

Principio:

ADQUIRIR -> USAR -> LIBERAR
🔴 ex4 — Crisis Response
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

Principio:

CRISIS  !=  CAÍDA DEL SISTEMA
🧠 Evolución Global
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
🎯 Objetivo final

Diseñar programas que:

interactúan con el mundo exterior

protegen recursos

gestionan errores

nunca colapsan




