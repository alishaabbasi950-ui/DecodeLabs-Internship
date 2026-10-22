import math
import secrets
import string

MIN_LEN, MAX_LEN, RECOMMENDED = 8,64,15

def get_length()-> int:
    while True:
        raw = input(f"Password length ({MIN_LEN}-{MAX_LEN}, {RECOMMENDED}+ recommended): ").strip()
        if not raw.isdigit():
            print("Please enter a whole number.")
            continue
        n = int(raw)
        if MIN_LEN <= n <= MAX_LEN:
            return n
        print(f"Length must be between {MIN_LEN} and {MAX_LEN}.")
 
 
def get_symbols_choice() -> bool:
    return input("Include special characters? (y/n): ").strip().lower() == "y"
 
def generate_password(length: int, use_symbols: bool) -> tuple[str, int]:
    pools = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if use_symbols:
        pools.append(string.punctuation)
    pool = "".join(pools)
 
    chars = [secrets.choice(p) for p in pools]                       # >=1 from each class
    chars += [secrets.choice(pool) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)                            # hide the pattern
    return "".join(chars), len(pool)                                 # .join(), not +=

def main() -> None:
    length = get_length()
    use_symbols = get_symbols_choice()
    password, pool_size = generate_password(length, use_symbols)
    entropy = length * math.log2(pool_size)  # upper bound: E = L * log2(R)
 
    print(f"\nPassword : {password}")
    print(f"Entropy  : ~{entropy:.1f} bits (pool size {pool_size})")
    if length < RECOMMENDED:
        print(f"Warning  : below {RECOMMENDED} characters; consider a longer password.")
 
 
if __name__ == "__main__":
    main()
