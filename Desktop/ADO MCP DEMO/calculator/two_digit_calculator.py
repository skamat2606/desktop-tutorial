"""Three-Digit Calculator — Python CLI version."""

MAX_DIGITS = 3


def get_number(prompt: str) -> float:
    """Ask the user for a number with at most 3 digits."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("  ⚠  Invalid input. Please enter a number.")
            continue

        # Check the digit count (ignore minus sign and decimal point)
        int_part = str(int(abs(value)))
        if len(int_part) > MAX_DIGITS:
            print(f"  ⚠  Max {MAX_DIGITS} digits per number (−999 to 999).")
            continue

        if abs(value) > 999:
            print(f"  ⚠  Number must be between −999 and 999.")
            continue

        return value


def get_operator() -> str:
    """Ask the user for an operator."""
    valid = {"+", "-", "*", "/"}
    while True:
        op = input("Enter operator (+, -, *, /): ").strip()
        if op in valid:
            return op
        print("  ⚠  Invalid operator. Choose +, -, *, or /.")


def format_number(n: float) -> str:
    """Format a number: show as int if whole, otherwise up to 6 decimals."""
    if n == int(n):
        return str(int(n))
    return f"{n:.6g}"


def calculate(a: float, op: str, b: float) -> float | None:
    """Perform the calculation. Returns None on error."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            print("  ⚠  Cannot divide by zero.")
            return None
        return a / b


def main():
    op_symbols = {"+": "+", "-": "−", "*": "×", "/": "÷"}

    print("=" * 36)
    print("   🔢  3-Digit Calculator  🔢")
    print("=" * 36)
    print("Each number must be between −999 and 999.")
    print("Type 'q' to quit.\n")

    while True:
        # First operand
        raw = input("First number (or 'q' to quit): ").strip()
        if raw.lower() == "q":
            print("Goodbye!")
            break
        try:
            a = float(raw)
        except ValueError:
            print("  ⚠  Invalid input.\n")
            continue
        if abs(a) > 999 or len(str(int(abs(a)))) > MAX_DIGITS:
            print(f"  ⚠  Number must be between −999 and 999.\n")
            continue

        # Operator
        op = get_operator()

        # Second operand
        b = get_number("Second number: ")

        # Calculate
        result = calculate(a, op, b)
        if result is not None:
            result = round(result, 10)  # avoid floating-point noise
            symbol = op_symbols.get(op, op)
            print(f"\n  {format_number(a)} {symbol} {format_number(b)} = {format_number(result)}\n")


if __name__ == "__main__":
    main()
