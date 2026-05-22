receipts = []

def capture_receipt(description, amount):

    receipt = {
        "description": description,
        "amount": amount
    }

    receipts.append(receipt)

    print(f"Receipt captured: {description} (P{amount})")