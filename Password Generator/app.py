
import streamlit as st

from password_generator import generate_password, estimate_strength

st.title("🔐 Password Generator")

# User inputs
letters = st.number_input("Number of letters", value=8)
numbers = st.number_input("Number of numbers", value=4)
special = st.number_input("Number of special characters",value=4)
total=int(letters)+int(numbers)+int(special)
if letters<0 or numbers<0 or special<0:
    st.error(f"Input number should not be negative.")

st.write("Total password length:", letters + numbers + special)

# Generate password
if st.button("Generate Password"):
    if 8 <= total <= 128:
        try:
            password = generate_password(
                letters,
                numbers,
                special
            )

            result = estimate_strength(password)

            st.subheader("Generated Password")
            st.code(password)

            st.write("Password Strength:", result["strength"])
            st.write(result["message"])

        except (ValueError, TypeError) as e:
            st.error(e)
    else:
        st.error(f"Password should be between 8 and 128 characters, current total length:{total}")

