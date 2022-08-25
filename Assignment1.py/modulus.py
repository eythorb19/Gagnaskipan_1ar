def modulus(a,b):
    """Calculates the modulus of two integers a,b."""
    if a-b == b:
        return 0
    elif a-b <b:
        return a-b
    else:
        return modulus(a-b,b)

if __name__ == "__main__":
    pass

sick = modulus(14,3)

print(sick)

# modulus(13, 4) == 1
# ■ modulus(12, 3) == 0
# ■ modulus(14, 3) == 2