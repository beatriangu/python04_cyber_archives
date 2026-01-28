#!/usr/bin/env python3
"""
Exercise 2 - Stream Management
Handles standard and alert communication channels.
"""

import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    print()
    print(
        f"{{[}}STANDARD{{]}} Archive status from {archivist_id}: "
        f"{status_report}"
    )

    sys.stderr.write(
        "{[}ALERT{]} System diagnostic: Communication channels verified\n"
    )

    print("{[}STANDARD{]} Data transmission complete\n")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()

