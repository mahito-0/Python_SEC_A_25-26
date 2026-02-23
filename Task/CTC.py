def token_needed(total_price: float, token_cost: float = 10.0) -> int:
    if token_cost <= 0:
        raise ValueError("Token cost must be greater than zero.")
    tokens = int(total_price // token_cost)
    if total_price % token_cost > 0:
        tokens += 1
    return tokens

def max_token_for_single_item(token_cost: float = 10.0) -> float:
    if token_cost <= 0:
        raise ValueError("Token cost must be greater than zero.")
    return token_cost - 0.01


def prompt_int(prompt: str, min_val: int = 0, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        if max_val is not None and val > max_val:
            print(f"Input must be less than or equal to {max_val}.")
            continue
        if val < min_val:
            print(f"Input must be greater than or equal to {min_val}.")
            continue
        return val


def prompt_float(prompt: str, min_val: float = 0.0, max_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        if max_val is not None and val > max_val:
            print(f"Input must be less than or equal to {max_val}.")
            continue
        if val < min_val:
            print(f"Input must be greater than or equal to {min_val}.")
            continue
        return val
    

def main() -> None:
    print("Cafeteria Token Checkout")
    num_items = prompt_int("Enter the number of items: ", min_val=1)
    prices = []
    for i in range(num_items):
        price = prompt_float(f"Enter the price of item {i + 1}: ", min_val=0.0)
        prices.append(price)
    total = sum(prices)
    print(f"Total price: {total:.2f}")
    
    tokens = token_needed(total)
    print(f"Number of tokens needed: {tokens}")
    
    max_single_item = max_token_for_single_item()
    print(f"Maximum price for a single item: ${max_single_item:.2f}")
    
    
    
if __name__ == "__main__":
    main()