#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pwntools>=4.15.0",
# ]
# ///
"""Decode the flag from the racecar challenge."""

from pwn import p32  # [no-member]

FLAG = "0x7b4254480x5f7968770x5f6431640x34735f310x745f33760x665" \
    "f33680x5f67346c0x745f6e300x355f33680x6b6334740x7d213f"
decoded_flag = []
for element in FLAG.split("0x")[1:]:
    decoded_flag.append(p32(int("0x" + element, 16)))
    print(b"".join(decoded_flag))
