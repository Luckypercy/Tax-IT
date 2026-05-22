returns = []

def add_return(tax_type, amount, due_date, status):
    tax_return = {
        "tax_type": tax_type,
        "amount": amount,
        "due_date": due_date,
        "status": status
    }

    returns.append(tax_return)

    print(f"{tax_type} return added (P{amount})")


def show_returns():
    print("\nCOMPLIANCE REPORT")
    print("---------------------------------------------")

    for r in returns:
        print(f"{r['tax_type']} | Due: {r['due_date']} | P{r['amount']} | {r['status']}")