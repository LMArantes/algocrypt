import streamlit as st

# Historical Ciphers
caesar_cipher = st.Page("historical-ciphers/caesar_cipher.py", title="Caesar Cipher")
vigenere_cipher = st.Page("historical-ciphers/vigenere_cipher.py", title="Vigenere Cipher")
transposition_cipher = st.Page("historical-ciphers/transposition_cipher.py", title="Transposition Cipher")
playfair_cipher = st.Page("historical-ciphers/playfair_cipher.py", title="Playfair Cipher")
enigma_machine = st.Page("historical-ciphers/enigma_machine.py", title="Extra: Enigma Machine")


# Cryptographic Hash Functions
md5 = st.Page("cryptographic-hash-functions/md5.py", title="MD5")
sha_1 = st.Page("cryptographic-hash-functions/sha_1.py", title="SHA-1")
sha_2 = st.Page("cryptographic-hash-functions/sha_2.py", title="SHA-2")
sha_3 = st.Page("cryptographic-hash-functions/sha_3.py", title="SHA-3")
blake = st.Page("cryptographic-hash-functions/blake.py", title="BLAKE")

pg = st.navigation(
    {
        "Historical Ciphers": [caesar_cipher, vigenere_cipher, transposition_cipher, playfair_cipher, enigma_machine],
        "Cryptographic Hash Functions: ": []
    }
)

pg.run()
