import hashlib
import hmac

# Simulate modular exponentiation using Python's built-in pow()
g = 3
p = 7
bank_priv = 7
alice_priv = 4

# Compute public keys
bank_public = pow(g, bank_priv, p)
alice_ephpub = pow(g, alice_priv, p)

# Provided hex values
ka = bytes.fromhex("36e693758492789e7b776126536a02eaff4d801db94c43e46e0bd83a67ba9878")
khmac = bytes.fromhex("a7a4ef5a4b36e2b5891c3e0bcfb9e9122cc0f53eec362438f5c8c2f226f571d0")
iv = bytes.fromhex("c2c844b8c39566e7fa98cd003c93561b")
c3 = bytes.fromhex("0afc2340d1e46733a82cc2b2c47e572bb396b39728dc264da3a4472b1502b5e6")

# Concatenate IV and ciphertext
msg = iv + c3

# Compute HMAC
computed_tag = hmac.new(key=khmac, msg=msg, digestmod=hashlib.sha256).digest()

# Provided HMAC tag (to compare against)
provided_tag = bytes.fromhex("9c32040a2c038465c30eef7164d82a0aaebb3a12a9cbae9be2b8eb659ec3c9f3")

# Compare
if hmac.compare_digest(computed_tag, provided_tag):
    print("✅ HMAC is valid.")
else:
    print("❌ HMAC is INVALID!")

# Optional: Print computed tag
print("Computed HMAC tag:", computed_tag.hex())
