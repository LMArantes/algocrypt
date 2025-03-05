import streamlit as st


# Historical Ciphers
caesar_cipher = st.Page("pages/historical-ciphers/caesar_cipher.py", title="Caesar Cipher")
vigenere_cipher = st.Page("pages/historical-ciphers/vigenere_cipher.py", title="Vigenère Cipher")
transposition_cipher = st.Page("pages/historical-ciphers/transposition_cipher.py", title="Transposition Cipher")
playfair_cipher = st.Page("pages/historical-ciphers/playfair_cipher.py", title="Playfair Cipher")
enigma_machine = st.Page("pages/historical-ciphers/enigma_machine.py", title="Extra: Enigma Machine")


# Cryptographic Hash Functions
md5 = st.Page("pages/cryptographic-hash-functions/md5.py", title="MD5")
sha_1 = st.Page("pages/cryptographic-hash-functions/sha_1.py", title="SHA-1")
sha_2 = st.Page("pages/cryptographic-hash-functions/sha_2.py", title="SHA-2")
sha_3 = st.Page("pages/cryptographic-hash-functions/sha_3.py", title="SHA-3")
blake = st.Page("pages/cryptographic-hash-functions/blake.py", title="BLAKE")


# Modern Symmetric-Key Algorithms (Block Ciphers)
des = st.Page("pages/modern-symmetric-key-algorithms/block-ciphers/data_encryption_standard.py", title="DES")
triple_des = st.Page("pages/modern-symmetric-key-algorithms/block-ciphers/triple_des.py", title="3DES")
aes = st.Page("pages/modern-symmetric-key-algorithms/block-ciphers/advanced_encryption_standard.py", title="AES")
blowfish = st.Page("pages/modern-symmetric-key-algorithms/block-ciphers/blowfish.py", title="Blowfish")
twofish = st.Page("pages/modern-symmetric-key-algorithms/block-ciphers/twofish.py", title="Twofish")
rc6 = st.Page("pages/modern-symmetric-key-algorithms/block-ciphers/r6.py", title="RC6")


# Modern Symmetric-Key Algorithms (Stream Ciphers)
rc4 = st.Page("pages/modern-symmetric-key-algorithms/stream-ciphers/rc4.py", title="RC4")
chacha20 = st.Page("pages/modern-symmetric-key-algorithms/stream-ciphers/chacha20.py", title="ChaCha20")
salsa20 = st.Page("pages/modern-symmetric-key-algorithms/stream-ciphers/salsa20.py", title="Salsa20")


# Asymmetric Encryption (Public-key cryptography)
rsa = st.Page("pages/asymmetric-encryption/rivest_shamir_adleman.py", title="RSA")
dh = st.Page("pages/asymmetric-encryption/diffie_hellman.py", title="Diffie-Hellman (DH)")
ecc = st.Page("pages/asymmetric-encryption/elliptic_curve_cryptography.py", title="Elliptic Curve Cryptography (ECC)")
elgamal = st.Page("pages/asymmetric-encryption/elgamal.py", title="ElGamal")


pg = st.navigation(
    {
        "Historical Ciphers": [caesar_cipher, vigenere_cipher, transposition_cipher, playfair_cipher, enigma_machine],
        "Cryptographic Hash Functions": [md5, sha_1, sha_2, sha_3, blake],
        "Block Ciphers": [des, triple_des, aes, blowfish, twofish, rc6],
        "Stream Ciphers": [rc4, chacha20, salsa20],
        "Public-key Cryptography": [rsa, dh, ecc, elgamal]
    }
)

pg.run()
