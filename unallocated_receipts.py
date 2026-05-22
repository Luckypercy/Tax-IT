unallocated_receipts = []

def add_unallocated_receipt(tax_type, amount, reason):

    receipt = {
        "tax_type": tax_type,
        "amount": amount,
        "reason": reason
    }

    unallocated_receipts.append(receipt)

    print(f"Unallocated receipt detected: {tax_type} (P{amount})")


def show_unallocated_receipts():

    print("\nUNALLOCATED RECEIPTS")
    print("---------------------------------------------")

    if len(unallocated_receipts) == 0:
        print("No unallocated receipts found")
        return

    for r in unallocated_receipts:

        print(
            f"{r['tax_type']} | "
            f"P{r['amount']} | "
            f"{r['reason']}"
        )