#!/usr/bin/env python3
"""
Exercise 0 - Ancient Text Recovery
Reads the file 'ancient_fragment.txt' and prints its contents.
Handles missing file gracefully.
"""

FILENAME = "ancient_fragment.txt"


def read_ancient_text(filename: str) -> list[str] | None:
    try:
        file = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        return None

    try:
        return file.readlines()
    finally:
        file.close()


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {FILENAME}")

    lines = read_ancient_text(FILENAME)
    if lines is None:
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    print("Connection established...\n")
    print("RECOVERED DATA:")

    for line in lines:
        clean = line.strip()
        clean = clean.replace("[", "{[}", 1).replace("]", "{]}", 1)
        print(clean)

    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()



