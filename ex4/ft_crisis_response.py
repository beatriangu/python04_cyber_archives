#!/usr/bin/env python3
"""
Exercise 4 - Crisis Response

Handles archive access crises using try/except with the `with` protocol.
"""

from __future__ import annotations


def crisis_handler(filename: str, routine: bool = False) -> None:
    prefix = "ROUTINE ACCESS" if routine else "CRISIS ALERT"
    status_ok = "STATUS: Normal operations resumed"
    status_crisis = "STATUS: Crisis handled, system stable"
    status_security = "STATUS: Crisis handled, security maintained"

    print(f"{prefix}: Attempting access to '{filename}'...")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read().strip()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print(status_ok)
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print(status_crisis)
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print(status_security)
    except Exception:
        print("RESPONSE: Unexpected system anomaly")
        print(status_crisis)


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt")
    print()
    crisis_handler("classified_vault.txt")
    print()
    crisis_handler("standard_archive.txt", routine=True)

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
