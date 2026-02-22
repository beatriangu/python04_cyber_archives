# Python Module 04 – Frequently Asked Questions (FAQ)

This document contains common questions and concise answers related to **Python Module 04 – Cyber Archives**.

It is intended as a **personal support document** to reinforce understanding and to prepare clear explanations for evaluation.

---

## ❓ What is I/O in Python?

**I/O (Input / Output)** refers to any interaction between the program and the external world.

Examples include:

* Reading from or writing to files
* Receiving input from the user (`stdin`)
* Displaying output or alerts (`stdout`, `stderr`)

I/O operations are inherently unreliable and must always be handled carefully.

---

## ❓ Why is I/O considered dangerous?

Because the program does not control the external environment:

* Files may not exist
* Permissions may be missing
* Data may be corrupted

For this reason, I/O must be isolated, protected, and never allowed to crash the program.

---

## ❓ What is a stream?

A **stream** is a sequential flow of data processed as it arrives or is produced.

In this module, the main streams are:

* `stdin`  → input stream
* `stdout` → standard output stream
* `stderr` → error and alert stream

Streams allow programs to communicate continuously without loading all data into memory.

---

## ❓ Why use `input()` and `print()` instead of `sys.stdin` and `sys.stdout` directly?

Because:

* `input()` reads from `sys.stdin` internally
* `print()` writes to `sys.stdout` internally

They are higher-level, clearer abstractions that are fully aligned with the subject requirements.

`sys.stderr` is used explicitly to demonstrate channel separation.

---

## ❓ What is RAII and how is it applied here?

**RAII (Resource Acquisition Is Initialization)** is a principle where:

* A resource is acquired when entering a scope
* It is automatically released when leaving that scope

In Python, this is implemented using the `with` statement.

This guarantees that files are always closed, even if an error occurs.

---

## ❓ Why use `with` instead of `try / finally`?

Both are valid, but:

* `try / finally` requires manual cleanup
* `with` guarantees automatic and safer resource handling

The module intentionally progresses from manual cleanup (ex0, ex1) to automatic cleanup (ex3).

---

## ❓ Why does the program not crash in Exercise 4?

Because all file access is wrapped inside `try / except` blocks.

Each error scenario is handled explicitly, allowing the program to:

* Respond appropriately
* Maintain system stability
* Continue execution

This simulates real-world resilient systems.

---

## ❓ Why are generated `.txt` files not included in the repository?

Because they are **artifacts**, not source code.

They can be recreated at any time using the subject-provided data generator, and therefore are not part of the delivery.

---

## ❓ What is the role of `main()` in these exercises?

`main()` acts as the **orchestrator**:

* It defines the execution flow
* It coordinates function calls
* It avoids performing low-level logic or I/O directly

This improves readability, structure, and explainability.

---

## ❓ What is the main learning outcome of this module?

To move from writing scripts that "work" to building programs that are:

* Safe
* Predictable
* Resilient
* Easy to explain and maintain

---

## 📌 Final Note

This FAQ is not part of the required submission.

It exists to consolidate understanding and to support confident explanations during evaluation.

**Author:** Bea
