# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pycryptodome>=3.23.0",
# ]
# ///
"""Broadcast RSA attack"""
from math import gcd

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse

pub1 = RSA.import_key(open("pub1.pem", "rb").read())
pub2 = RSA.import_key(open("pub2.pem", "rb").read())

p = gcd(pub1.n, pub2.n)

q = pub1.n // p
phi = (p - 1) * (q - 1)
d = inverse(pub1.e, phi)

priv = RSA.construct((pub1.n, pub1.e, d, p, q))
flag = PKCS1_OAEP.new(priv).decrypt(open("flag.enc", "rb").read())

print(flag.decode())
