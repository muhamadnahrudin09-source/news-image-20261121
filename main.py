import os
import shutil
from pathlib import Path

def main():
    script_dir = Path(__file__).resolve().parent
    src = script_dir / "entry.png"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"

    if src.exists():
        shutil.copy2(src, dst)
        size = dst.stat().st_size
        print(f"Copied {src} to {dst}, size: {size} bytes")
    else:
        fallback = script_dir / "ENTRY_PLACEHOLDER_NOTE"
        if fallback.exists():
            shutil.copy2(fallback, dst)
            size = dst.stat().st_size
            print(f"Copied placeholder note to {dst}, size: {size} bytes")
        else:
            raise FileNotFoundError("entry.png not found in repo root.")

if __name__ == "__main__":
    main()
