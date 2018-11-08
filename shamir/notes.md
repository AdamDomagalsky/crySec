# Crypto

- **Kryptografia** chowanie informacji
- **Kryptoanaliza** odkyrwanie slabosci w alg.
- **Encryption** metoda zamiany _plaintext_ na nieczytelny format
- **Plaintext** czytelny format danych
- **Ciphertext** _plaintext_ po _szyfrowaniu_
- **Decyrption** metoda zamiany _ciphertext_ na _plaintext_
- **Encryption alg.** zbiór regół definiujących jak szyfrujemy i deszyfrujemy dane

## Szyfr(cipher)

### Strong 
> As computing power increases, strong ciphers becomes weaker
- AES
- 3DES
- TwoFish

### Weak
- WEP
- WPA

## Digital Signatures (Async)
> Async encryption using public-key / private-key (PKI)

Hash Alg. > Hashing Value > Sender's Private Key = Singed Document
Singed Message > Sender's Public Key > Hashing Value (then we can check)

#### Entropy - randomness collected by system
#### Confusion -  each char of ciphertext should depend on several parts of the key to make hacker confuse
#### Diffusion - removing patter from ciphertext
#### Obfuscation - intended meaning or intentionally making something difficult to understand (callbacki nic nie robiace zeby zmylic kogos)


# BLOCK vs STREAM - symetric enc. methods
- Block cipher: encrypts in chunks (blocks) of data at time
- Stream cipher: encrypts one bit at a time
