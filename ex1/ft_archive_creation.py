#!/usr/bin/env python3
"""
Exercise 1 - Archive Creation
Creates 'new_discovery.txt' and writes three preservation entries.
"""

FILENAME = "new_discovery.txt"


def get_lines() -> list[str]:
    """
    Return the exact lines to preserve (already formatted).
    """
    return [
        "{[}ENTRY 001{]} New quantum algorithm discovered",
        "{[}ENTRY 002{]} Efficiency increased by 347%",
        "{[}ENTRY 003{]} Archived by Data Archivist trainee belamiqu",
    ]


def write_archive(filename: str, lines: list[str]) -> None:
    """
    Write lines to file, one per line, always closing the file safely.
    """
    file = open(filename, "w", encoding="utf-8")
    try:
        for line in lines:
            file.write(line + "\n")
    finally:
        file.close()


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {FILENAME}")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")

    lines = get_lines()
    for line in lines:
        print(line)

    write_archive(FILENAME, lines)

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{FILENAME}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
