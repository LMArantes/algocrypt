import streamlit as st
from utils.gibberish_detector.detector import words_check


def caesar_cipher(plain_text, key):
    encrypted_lines = []

    for line in plain_text.split("\n"):
        encrypted_line = ''.join(
            chr(((ord(char) - 65 + key) % 26) + 65) if char.isupper() else
            chr(((ord(char) - 97 + key) % 26) + 97) if char.islower() else char
            for char in line
        )
        encrypted_lines.append(encrypted_line)

    return "\n".join(encrypted_lines)


def brute_force_caesar(cipher_text):
    results = []
    for key in range(1, 26):
        decrypted_text = caesar_cipher(cipher_text, key)
        score = words_check(decrypted_text)
        results.append((key, decrypted_text, score))

    # Sort results by score (higher is better), and if scores are equal, sort by shift value
    results.sort(key=lambda x: (-x[2], x[0]))

    return results[:5]


st.set_page_config(page_title="Caesar Cipher", page_icon="🔑")

st.title("Caesar Cipher")
st.markdown("---")

st.write("### Encoder and Decoder")

st.text("")
shift = st.slider("Shift:", 1, 25)

text = st.text_area("Enter text to encrypt or decrypt")

if text:
    encrypted_text = caesar_cipher(text, shift)

    st.write("Result:")
    st.code(encrypted_text)

st.text("")
st.markdown("---")
st.write("### Brute Force")

cipher_text = st.text_area("Enter cipher text for brute force analysis")

if cipher_text:
    results = brute_force_caesar(cipher_text)

    st.write("#### **Top 5 Best Matches:**")
    for shift, decrypted_text, score in results:
        st.write(f"**Shift {shift} - Score {score:.2f}:**")
        st.code(decrypted_text)
