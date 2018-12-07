from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import os
# CSR
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

#Generate key
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

directory = "clientCerts"
if not os.path.exists(directory):
    os.makedirs(directory)

with open(os.path.join(directory,"key.pem"),"wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase")
    ))


csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
    # Provide various details about who we are.
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"PL"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"WLKP"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Poznan"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UAM"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mojastrona.com"),
])).add_extension(
    x509.SubjectAlternativeName([
        # Describe what sites we want this certificate for.
        x509.DNSName(u"mojastrona.com"),
        x509.DNSName(u"www.mojastrona.com"),
        x509.DNSName(u"podstrona.mojastrona.com"),
    ]),
    critical=False,
# Sign the CSR with our private key.
).sign(key, hashes.SHA256(), default_backend())
# Write our CSR out to disk.
with open(os.path.join(directory,"csr.pem"), "wb") as f:
    f.write(csr.public_bytes(serialization.Encoding.PEM))



    