
x = bytes.fromhex(
    "96F84D3EB56CCD93896FEBB962858726"
    "5601F3EB77981F1DFDFC4C2744A3C265"
    "3881161FF0A0"
)

for key in [bytes.fromhex("DEAD"), bytes.fromhex("DEADDEAD"), b"DEAD"]:
    y = bytes(b ^ key[i % len(key)] for i, b in enumerate(x))
    print(f"\nkey = {key!r}")
    print(y.hex())
    print(y)
