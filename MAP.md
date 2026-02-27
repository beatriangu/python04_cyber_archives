# 🧭 MAP.md — Python Garden · Cyber Archives
## python04_cyber_archives — Safe I/O & Resilient Programs

This document is my learning and design map.  
It represents how my thinking evolves when designing the interaction between a Python program and the external world.

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
🌱 Core Idea
EXTERNAL WORLD
       |
       v
PROGRAM PROTECTS ITSELF
🟢 ex0 — Ancient Text Recovery
+----------------------+
|        main()        |
+----------------------+
| open()               |
| read()               |
| try / finally        |
| close()              |
+----------------------+

Flow:

FILE  --->  READ  --->  DISPLAY
🟡 ex1 — Archive Creation
+----------------------+
|        main()        |
+----------------------+
| get_data()           |
| open("w")            |
| write()              |
| close()              |
+----------------------+

Flow:

DATA  --->  WRITE  --->  FILE
🔵 ex2 — Stream Management
            USER
               |
               v
            stdin
               |
               v
+----------------------------+
|          PROGRAM           |
+----------------------------+
| stdout  -> messages        |
| stderr  -> alerts          |
+----------------------------+
🟣 ex3 — Vault Security
+------------------------------+
|        with open()           |
+------------------------------+
| acquire resource             |
| use resource                 |
| release automatically        |
+------------------------------+

Principle:

ACQUIRE -> USE -> RELEASE
🔴 ex4 — Crisis Response
+-----------------------------------+
|        crisis_handler()           |
+-----------------------------------+
| try                               |
|   with open()                     |
| except FileNotFoundError          |
| except PermissionError            |
| except Exception                  |
| finally -> system stable          |
+-----------------------------------+

Principle:

CRISIS  !=  SYSTEM FAILURE
🧠 Global Evolution
        +------------------+
        |  External World  |
        +------------------+
                  |
                  v
        +------------------+
        |  ex0: read       |
        +------------------+
                  |
                  v
        +------------------+
        |  ex1: write      |
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
        |  ex4: resilience |
        +------------------+
🎯 Final Objective

Design programs that:

interact with the external world

protect resources

handle errors

never collapse