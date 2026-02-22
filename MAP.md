
# 🧭 MAP.md — Python Garden · Cyber Archives
## python04_cyber_archives — Safe I/O & Resilient Programs

Este documento es mi mapa de aprendizaje y diseño.  
Representa cómo evoluciona mi forma de pensar la interacción entre un programa Python y el mundo exterior: archivos, streams y errores reales.

---

## 📁 Project Structure

```text
python04_cyber_archives/
├── ex0/
├── ex1/
├── ex2/
├── ex3/
├── ex4/
├── tools/
├── README.md
├── MAP.md
└── .gitignore
🌱 Idea central

El mundo exterior es inestable.
El programa debe protegerse y seguir funcionando.

🟢 ex0 — Ancient Text Recovery
main()
├─ open()
├─ read()
├─ finally → close()
└─ print()

Aprendo:

FileNotFoundError

try / finally

Recursos deben cerrarse siempre

🟡 ex1 — Archive Creation
main()
├─ get_data()
├─ open("w")
├─ write()
└─ finally → close()

Aprendo:

Separar datos de persistencia

Control de escritura

🔵 ex2 — Stream Management
stdin  → entrada
stdout → mensajes normales
stderr → alertas

Aprendo:

Tres canales distintos

No mezclar mensajes

🟣 ex3 — Vault Security
with open("r") as f:
    ...

with open("w") as f:
    ...

Aprendo:

RAII

Cierre automático

🔴 ex4 — Crisis Response
try:
    with open():
        SUCCESS
except FileNotFoundError:
    not found
except PermissionError:
    access denied
except Exception:
    unexpected
finally:
    system stable

Aprendo:

Resiliencia real

El sistema nunca cae

🧠 Evolución global
Mundo exterior
      ↓
ex0 → leer
      ↓
ex1 → escribir
      ↓
ex2 → separar streams
      ↓
ex3 → with (seguridad automática)
      ↓
ex4 → resiliencia completa
🎯 Objetivo final

Ser capaz de explicar:

qué puede fallar

cómo se protege el programa

cómo se liberan recursos

por qué el sistema sigue vivo pase lo que pase


---

