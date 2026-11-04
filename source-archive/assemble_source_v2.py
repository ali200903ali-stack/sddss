#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import tarfile
from pathlib import Path

EXPECTED_SHA256 = "f8166c30624ec4f3751edb250ffd9ceb17c2d653f2c448c62baa1aaef8b6ad9c"
PART_COUNT = 9

root = Path(__file__).resolve().parent
parts = [root / f"NineSoft-Source-XZ.part{i:02d}.b64" for i in range(PART_COUNT)]
missing = [p.name for p in parts if not p.exists()]
if missing:
    raise SystemExit(f"Missing source parts: {', '.join(missing)}")

# GitHub/text transports may wrap or insert harmless whitespace in Base64.
# Remove every whitespace character, then use strict validation for all others.
payload = "".join(
    "".join(part.read_text(encoding="utf-8").split()) for part in parts
)
archive_bytes = base64.b64decode(payload, validate=True)
actual_sha256 = hashlib.sha256(archive_bytes).hexdigest()
if actual_sha256 != EXPECTED_SHA256:
    raise SystemExit(
        f"Checksum mismatch: expected {EXPECTED_SHA256}, got {actual_sha256}"
    )

archive_path = root / "NineSoft-Source-for-GitHub.tar.xz"
archive_path.write_bytes(archive_bytes)
destination = root / "NineSoft-System-Ready"
destination.mkdir(parents=True, exist_ok=True)

with tarfile.open(archive_path, "r:xz") as archive:
    destination_root = destination.resolve()
    for member in archive.getmembers():
        target = (destination / member.name).resolve()
        if target != destination_root and destination_root not in target.parents:
            raise SystemExit(f"Unsafe archive path: {member.name}")
    archive.extractall(destination)

print(f"Verified SHA-256: {actual_sha256}")
print(f"Extracted source to: {destination}")
print("Next steps:")
print("  cd source-archive/NineSoft-System-Ready/NineSoft-System-Ready")
print("  python scripts/init_db.py --db data/ninesoft.db")
print("  python scripts/verify_system.py --db data/ninesoft.db")
print("  ./start.sh  # Windows: start.bat")
