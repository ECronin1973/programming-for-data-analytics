import os

filename = "../data/access.log.txt"

if not os.path.exists(filename):
    print(f"File not found: {filename}")
else:
    print(f"File exists: {os.path.exists(filename)}")
    print(f"File size: {os.path.getsize(filename)} bytes")

    # Try reading with different methods
    print("\n--- Using read() ---")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"Content length: {len(content)}")
        print(f"First 200 chars: {repr(content[:200])}")

    print("\n--- Using readlines() ---")
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"Number of lines: {len(lines)}")
        if lines:
            print(f"First line: {lines[0]}")
