#!/usr/bin/env python3
"""
Exercise 3 - Vault Security

Demonstrates secure file handling using the `with` statement (RAII).
"""

READ_FILE = "classified_data.txt"
WRITE_FILE = "security_protocols.txt"


def read_classified(filename: str) -> list[str]:
    """Read classified data using a context manager."""
    with open(filename, "r", encoding="utf-8") as file:
        return [line.rstrip("\n") for line in file]


def write_protocol(filename: str, message: str) -> None:
    """Write security protocol using a context manager."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"{message}\n")


def format_line(line: str) -> str:
    """Format a classified line to match subject output."""
    return line.replace("[", "{[}", 1).replace("]", "{]}", 1)


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    for line in read_classified(READ_FILE):
        print(format_line(line))

    print("\nSECURE PRESERVATION:")
    message = "{[}CLASSIFIED{]} New security protocols archived"
    write_protocol(WRITE_FILE, message)
    print(message)
    print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
