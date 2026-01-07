import sys
from pathlib import Path

try:
    import qrcode
except ImportError:
    print("Missing dependency: qrcode. Install with: pip install qrcode[pil]")
    raise

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_qr.py <URL>")
        sys.exit(1)

    url = sys.argv[1].strip()
    img = qrcode.make(url)
    out = Path(__file__).parent / "qr-code.png"
    img.save(out)
    print(f"Saved: {out} (URL: {url})")

if __name__ == "__main__":
    main()
