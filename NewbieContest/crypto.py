#!/usr/bin/python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests>=2.34.2",
# ]
# ///
"""Decipher the encrypted message from the Newbie Contest challenge."""

import requests

CHALL_URL = "https://www.newbiecontest.org/epreuves/prog/prog5.php"
ANS_URL = "https://www.newbiecontest.org/epreuves/prog/verifpr5.php?solution="


def decipher(encrypted, shift):
    """Reinventing the emperor's wheel."""
    start = ord("a")
    decrypted = ""
    for char in encrypted:
        decrypted += chr(((ord(char) - start - shift) % 26) + start)
    return decrypted


with requests.Session() as s:
    myCookies = {"MY-PRECIOUS-COOKIES-GET-YOURS"}

    chall = s.get(CHALL_URL, cookies=myCookies)
    exp = chall.content.decode("ascii").split(" ")
    crypt = exp[6].replace("'", "")
    key = int(exp[-1].replace("'", ""))
    print("encrypted: ", crypt, " key: ", key)
    solution = decipher(crypt, key)  # MINUSKEY
    print("decoded: ", solution)
    print(s.get(ANS_URL + str(solution), cookies=myCookies).text)
