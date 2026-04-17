def calculate_bid(bid_text):
    subtotal = 0.0
    fee_percent = 0.0
    deposit = 0.0
    
    lines = bid_text.split('\n')
    
    for line in lines:
        if line == "":
            continue            
        if "->" in line:
            parts = line.split(" ")
            hours = float(parts[2])
            
            rate_string = parts[5]
            rate_clean = ""
            for char in rate_string:
                if char != "$" and char != "/" and char != "h" and char != "r":
                    rate_clean = rate_clean + char
            
            rate = float(rate_clean)
            subtotal = subtotal + (hours * rate)
            
        elif "FEE:" in line:
            parts = line.split(" ")
            fee_string = parts[1]
            fee_clean = ""
            for char in fee_string:
                if char != "%":
                    fee_clean = fee_clean + char
            fee_percent = float(fee_clean)
            
        elif "DEPOSIT:" in line:
            parts = line.split(" ")
            dep_string = parts[1]
            dep_clean = ""
            for char in dep_string:
                if char != "$":
                    dep_clean = dep_clean + char
            deposit = float(dep_clean)

    remaining_balance = subtotal - deposit
    fee_multiplier = fee_percent / 100
    grand_total = remaining_balance * (1 + fee_multiplier)
    
    final_string = "$" + str(round(grand_total, 2))
    
    return final_string

# Test Case 1: Standard bid
bid1 = """Framing -> 10 hrs at $50.00/hr
Wiring -> 5 hrs at $80.00/hr
FEE: 10%
DEPOSIT: $100.00"""
print(calculate_bid(bid1))

bid2 = """Plumbing -> 2 hrs at $100.00/hr
Cleanup -> 1 hrs at $20.00/hr
FEE: 5%"""
print(calculate_bid(bid2))

bid3 = """Painting -> 4 hrs at $25.00/hr
Sanding -> 2 hrs at $15.00/hr
DEPOSIT: $30.00
FEE: 0%"""
print(calculate_bid(bid3))
