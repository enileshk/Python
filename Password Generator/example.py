from password_generator import (
    generate_password,
    estimate_strength
)

# Generate password
password = generate_password(8, 6, 4)

print("Password:", password)

# Estimate strength
result = estimate_strength(password)

print("Strength:", result["strength"])
print("Message:", result["message"])
