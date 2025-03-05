import streamlit as st


def vigenere_encode(plaintext, key):
    if not key:
        return plaintext

    ciphertext = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('a')
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            new_char = char
        ciphertext += new_char

    return ciphertext


def vigenere_decode(ciphertext, key):
    if not key:
        return ciphertext

    plaintext = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('a')
            if char.islower():
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1  # Only increment for alphabetic characters
        else:
            new_char = char
        plaintext += new_char

    return plaintext


st.set_page_config(page_title="Vigenère Cipher", page_icon="🔑")

st.title("Vigenère Cipher")
st.markdown("---")

st.write("### Encoder and Decoder")

option = st.radio('', ["Encode", "Decode"], index=0, label_visibility="hidden")

text = st.text_area("Enter text")

keyword = st.text_input("Enter keyword")

if text:
    if option == "Encode":
        encrypted_text = vigenere_encode(text, keyword)
        st.write("Result:")
        st.code(encrypted_text)
    elif option == "Decode":
        decrypted_text = vigenere_decode(text, keyword)
        st.write("Result:")
        st.code(decrypted_text)
