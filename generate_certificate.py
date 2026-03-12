import qrcode
import json

BASE_URL = "https://yourusername.github.io/verisecure-certificates/verify.html?id="

with open("certificates.json") as f:
    certificates = json.load(f)

for cert_id in certificates:

    verification_url = BASE_URL + cert_id

    img = qrcode.make(verification_url)

    img.save(f"qr_codes/{cert_id}.png")

    print(f"QR generated for {cert_id}")