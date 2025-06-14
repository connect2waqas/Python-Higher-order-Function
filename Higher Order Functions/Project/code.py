from functools import reduce

# simple input with and invalid transication:

transacation_usd =[200,5000,1000,900,4000,800,"invalid","false"]

# higher order function for validation:
def validate_transactions(transactions,transactions_rule):
    return list(filter(transactions_rule, transactions))

def convert_usd_to_eur(amount_usd):
    try:
        return round(amount_usd * 0.93,2)
    except TypeError:
        return None
    
    # 3. Main Processing with Error Handling
    # validate the transication:

is_valid = lambda x : isinstance(x,(int,float)) and x!=0
valide_transactions = validate_transactions(transacation_usd,is_valid)

transacation_eur =list(map(lambda amt: convert_usd_to_eur(amt),valide_transactions))
transacation_eur = list(filter(None,transacation_eur))

high_value_transactions = list(filter(lambda x: abs(x),valide_transactions))

net_balance_eur = reduce(lambda acc,curr: acc+curr ,transacation_eur,0)

high_risk_flags = list(map(lambda x: 'High Risks' if abs(x) > 2000 else "Normal",valide_transactions))

print("Valid Transactions (USD):", valide_transactions)
print("Converted to EUR:", transacation_eur)
print("High-Value Transactions (>$500 USD):", high_value_transactions)
print("Net Balance (EUR):", net_balance_eur)
print("Risk Flags:", high_risk_flags)


