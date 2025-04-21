import streamlit as st
from cryptography.fernet import Fernet
import os
import io
import base64

# --- Utility Functions ---
def generate_key():
    return Fernet.generate_key()

def save_file(file_data, filename):
    with open(filename, 'wb') as f:
        f.write(file_data)

def load_file(file):
    return file.read()

def encrypt_file(file_data, key):
    fernet = Fernet(key)
    return fernet.encrypt(file_data)

def decrypt_file(file_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(file_data)

def is_valid_fernet_key(key_str):
    try:
        key_bytes = key_str.encode()
        decoded = base64.urlsafe_b64decode(key_bytes)
        return len(decoded) == 32
    except:
        return False

# --- Streamlit App ---
st.set_page_config(page_title="File Encryption & Decryption", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: #ffffff;
        }
        .main {
            background-color: #1e222a;
            color: #ffffff;
            padding: 20px;
            border-radius: 12px;
        }
        .stTextInput>div>div>input {
            background-color: #262730;
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔐 File Encryption & Decryption App")

option = st.sidebar.radio("Select Operation", ("Encrypt File", "Decrypt File"))

file_types = st.sidebar.multiselect("Allowed File Types", ["txt", "pdf", "jpg", "png", "docx", "xlsx"], default=["txt", "pdf"])

if option == "Encrypt File":
    st.header("Encrypt a File")
    uploaded_file = st.file_uploader("Upload file to encrypt", type=file_types if file_types else None)

    key_type = st.radio("Key Type", ("Auto-generate Key", "Enter Custom Key"))

    custom_key_input = None
    if key_type == "Enter Custom Key":
        custom_key_input = st.text_input("Enter your 32-byte Base64-encoded key")

    if uploaded_file:
        if key_type == "Enter Custom Key":
            if not is_valid_fernet_key(custom_key_input):
                st.error("Invalid key. Must be a valid Base64-encoded 32-byte string.")
            else:
                key = custom_key_input.encode()
        else:
            key = generate_key()

        if key_type == "Auto-generate Key" or is_valid_fernet_key(custom_key_input):
            file_data = load_file(uploaded_file)
            encrypted_data = encrypt_file(file_data, key)

            st.success("File encrypted successfully!")
            st.download_button("⬇ Download Encrypted File", encrypted_data, file_name=f"encrypted_{uploaded_file.name}")

            st.text_input("Encryption Key (Keep it safe for decryption)", value=key.decode(), disabled=True)

            key_txt = io.BytesIO()
            key_txt.write(key)
            key_txt.seek(0)
            st.download_button("⬇ Download Key as .txt", key_txt, file_name="encryption_key.txt", mime="text/plain")

elif option == "Decrypt File":
    st.header("Decrypt a File")
    uploaded_file = st.file_uploader("Upload file to decrypt", type=file_types if file_types else None)
    user_key = st.text_input("Enter Encryption Key")

    if uploaded_file and user_key:
        try:
            file_data = load_file(uploaded_file)
            decrypted_data = decrypt_file(file_data, user_key.encode())

            st.success("File decrypted successfully!")
            st.download_button("⬇ Download Decrypted File", decrypted_data, file_name=f"decrypted_{uploaded_file.name}")
        except Exception as e:
            st.error("Decryption failed. Check your key or file integrity.")
