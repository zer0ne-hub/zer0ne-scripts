#!/usr/bin/python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests>=2.34.2",
# ]
# ///
"""Solve the equation from the Newbie Contest challenge."""

import requests

CHALL_URL = "https://www.newbiecontest.org/epreuves/prog/prog4.php"
ANS_URL = "https://www.newbiecontest.org/epreuves/prog/verifpr4.php?solution="

with requests.Session() as s:
    myCookies = {"THESE COOKIES ARE MINE"}

    chall = s.get(CHALL_URL, cookies=myCookies)
    eq = chall.content.decode("ascii").split(" ")[0].strip()
    clean_eq = eq.replace("racine", "math.sqrt").replace("&sup2;", "**2")
    print(clean_eq)
    solution = eval(clean_eq)  # Rare cases of eval usability: CTF context
    print(int(solution))
    print(s.get(ANS_URL + str(solution), cookies=myCookies).text)
