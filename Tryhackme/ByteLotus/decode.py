# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "scapy>=2.7.0",
# ]
# ///
import base64
import re
import sys

from scapy.all import TCP, Raw, rdpcap

KEY = b"H0t3lSt@ff0NlyK3epS3cr3t!"
COOKIE_RE = re.compile(rb"hotel_sess_state=([A-Za-z0-9+/=]+)")


def xor(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def decode_cookie(b64_bytes: bytes) -> str:
    encrypted = base64.b64decode(b64_bytes)
    return xor(encrypted, KEY).decode("utf-8", errors="replace")


def extract_keystrokes(pcap_path: str) -> str:
    packets = rdpcap(pcap_path)
    hits = []
    for pkt in packets:
        if pkt.haslayer(TCP) and pkt.haslayer(Raw):
            payload = bytes(pkt[Raw].load)
            match = COOKIE_RE.search(payload)
            if match:
                hits.append((pkt.time, match.group(1)))

    hits.sort(key=lambda x: x[0])
    return "".join(decode_cookie(b64) for _, b64 in hits)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 decode_pcap.py <capture.pcapng>")
        sys.exit(1)

    result = extract_keystrokes(sys.argv[1])
    print(result)
