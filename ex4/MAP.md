🧭 MAPA VISUAL DEL MÓDULO (ex0 → ex4)

Piensa el módulo como una evolución controlada del contacto con el mundo exterior.

🟢 EX0 — Ancient Text Recovery

👉 Primer contacto con I/O + control manual

Arquitectura
main()
 ├─ logs (print)
 ├─ read_ancient_text()
 │    ├─ open()
 │    ├─ readlines()
 │    └─ finally: close()
 ├─ formateo de líneas
 └─ cierre limpio

Idea clave
ARCHIVO ──▶ leer ──▶ mostrar


Introduces FileNotFoundError

Introduces finally

Aprendes que I/O puede fallar

Aprendes que hay que cerrar recursos

🟡 EX1 — Archive Creation

👉 Escritura segura + separación de datos

Arquitectura
main()
 ├─ get_lines()        ← datos puros
 ├─ preview (print)
 ├─ write_archive()
 │    ├─ open("w")
 │    ├─ write()
 │    └─ finally: close()
 └─ confirmación

Idea clave
datos ──▶ escribir ──▶ archivo


Separas qué se escribe de cómo se escribe

Sigues cerrando recursos manualmente

Introduces la idea de output controlado

🔵 EX2 — Stream Management

👉 Canales de comunicación (streams)

Arquitectura
Usuario
  │
  ▼
stdin (input)
  │
  ▼
programa
  │
  ├─ stdout (print)
  └─ stderr (sys.stderr.write)

Idea clave
ENTRADA ≠ SALIDA ≠ ALERTA


Aprendes que hay tres flujos distintos

No todo es “print”

Un programa serio no mezcla mensajes

🟣 EX3 — Vault Security

👉 RAII real con with

Arquitectura
main()
 ├─ read_classified()     ← with open("r")
 ├─ format_line()         ← lógica pura
 ├─ write_protocol()      ← with open("w")
 └─ logs de seguridad

Idea clave
adquirir ──▶ usar ──▶ liberar (automático)


with garantiza cierre incluso si algo falla

Ya no dependes de finally

Esto es nivel profesional

🔴 EX4 — Crisis Response

👉 El mundo real: errores múltiples + sistema estable

Arquitectura
main()
 ├─ crisis_handler("lost_archive.txt")
 ├─ crisis_handler("classified_vault.txt")
 ├─ crisis_handler("standard_archive.txt")
 └─ cierre global

Dentro de crisis_handler
try:
   with open():
      SUCCESS
except FileNotFoundError:
      RESPONSE not found
except PermissionError:
      RESPONSE deny access
except Exception:
      RESPONSE unexpected
finally:
      STATUS estable

Idea clave
CRISIS ≠ CAÍDA DEL SISTEMA


El error no rompe el programa

Cada crisis tiene respuesta

El sistema siempre termina estable

🧠 MAPA GLOBAL (TODO EL MÓDULO JUNTO)
        ┌──────────┐
        │  Mundo   │
        │ exterior │
        └────┬─────┘
             │
             ▼
      ┌───────────────┐
      │ ex0: leer      │  ← I/O básico
      └───────────────┘
             │
             ▼
      ┌───────────────┐
      │ ex1: escribir  │  ← output controlado
      └───────────────┘
             │
             ▼
      ┌───────────────┐
      │ ex2: streams   │  ← canales separados
      └───────────────┘
             │
             ▼
      ┌───────────────┐
      │ ex3: with      │  ← RAII / seguridad
      └───────────────┘
             │
             ▼
      ┌───────────────┐
      │ ex4: crisis    │  ← resiliencia real
      └───────────────┘



“El módulo progresa desde operaciones básicas de entrada/salida hasta un sistema resiliente que gestiona errores reales sin comprometer la estabilidad, usando s