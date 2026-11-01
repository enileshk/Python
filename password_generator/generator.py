
import secrets
import string
import math

# Character sets
ALPHABETS = string.ascii_letters
NUMBERS = string.digits
SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}\\|;:'\",<>./?`~"


def validate_length(letters, numbers, special):
    """Validate password character counts."""

    counts = [letters, numbers, special]

    if any(not isinstance(x, int) or isinstance(x, bool) for x in counts):
        raise TypeError("Character counts must be integers")

    if any(x < 0 for x in counts):
        raise ValueError("Character counts cannot be negative")

    total = sum(counts)

    if total < 8:
        raise ValueError("Password must contain at least 8 characters")

    if total > 128:
        raise ValueError("Password cannot exceed 128 characters")

    return total


def generate_password(letters=8, numbers=4, special=4):
    """Generate a cryptographically secure password."""

    validate_length(letters, numbers, special)

    password = (
        [secrets.choice(ALPHABETS) for _ in range(letters)] +
        [secrets.choice(NUMBERS) for _ in range(numbers)] +
        [secrets.choice(SPECIAL_CHARS) for _ in range(special)]
    )

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def estimate_strength(password):
    """Estimate password strength using entropy and character diversity."""

    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    if len(password) < 8:
        return {
            "strength": "Weak",
            "entropy": 0,
            "message": "Password must contain at least 8 characters."
        }

    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26

    if any(c.isupper() for c in password):
        pool_size += 26

    if any(c.isdigit() for c in password):
        pool_size += 10

    if any(c in SPECIAL_CHARS for c in password):
        pool_size += len(SPECIAL_CHARS)

    if pool_size == 0:
        return {
            "strength": "Weak",
            "entropy": 0,
            "message": "Insufficient character diversity."
        }

    entropy = len(password) * math.log2(pool_size)

    if entropy < 40:
        strength = "Weak"
    elif entropy < 60:
        strength = "Medium"
    elif entropy < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "strength": strength,
        "entropy": round(entropy, 2),
        "message": f"Estimated entropy: {round(entropy, 2)} bits"
    }
