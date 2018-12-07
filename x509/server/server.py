from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.hazmat.primitives import serialization
import datetime
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

import os


dataCertCA = open(os.path.join("CAserverCerts" ,"CAcertificate.pem"),"rb").read()
dataKeyCA =  open(os.path.join("CAserverCerts" ,"CAkey.pem"),"rb").read()
KEY_CA = serialization.load_pem_private_key(dataKeyCA,b"passphrase",default_backend())
CERT_CA = x509.load_pem_x509_certificate(dataCertCA, default_backend())


os.chdir('..')
pemReqPath = os.path.join("client","clientCerts" ,"csr.pem")
pemReqData =  open(pemReqPath,"rb").read()
CSR = x509.load_pem_x509_csr(pemReqData,default_backend())

issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"NEW YORK"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"NEW YORK"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Certs Authority"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"ca.com"),
])
clientSignedCertificate = x509.CertificateBuilder().subject_name(
  CSR.subject
).issuer_name(
    issuer
).public_key(
    CSR.public_key()
).serial_number(
    x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        # Our certificate will be valid for 10 days
        datetime.datetime.utcnow() + datetime.timedelta(days=10)
).add_extension(

    #  TODO doesnt work
    CSR.extensions
).sign(KEY_CA, hashes.SHA256(), default_backend())

print(clientSignedCertificate)
