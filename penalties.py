import datetime

PENALTY_RATE = 500
DAILY_INTEREST_RATE = 0.015


def calculate_penalties(returns):

    today = datetime.date.today()
    penalties = []

    for r in returns:

        due = datetime.datetime.strptime(r["due_date"], "%Y-%m-%d").date()
        days_overdue = (today - due).days

        if days_overdue > 0 and r["status"].lower() != "submitted":

            late_fee = PENALTY_RATE
            interest = round(r["amount"] * DAILY_INTEREST_RATE * days_overdue, 2)
            total = round(late_fee + interest, 2)

            penalties.append({
                "tax_type":    r["tax_type"],
                "due_date":    r["due_date"],
                "days_overdue": days_overdue,
                "late_fee":    late_fee,
                "interest":    interest,
                "total":       total
            })

    return penalties


def show_penalties(returns):

    penalties = calculate_penalties(returns)

    print("\nPENALTIES & LATE FEES")
    print("---------------------------------------------")

    if not penalties:
        print("  No penalties — all returns are on time!")
        return

    grand_total = 0

    for p in penalties:
        print(f"  {p['tax_type']}")
        print(f"    Due Date:     {p['due_date']}")
        print(f"    Days Overdue: {p['days_overdue']}")
        print(f"    Late Fee:     P{p['late_fee']}")
        print(f"    Interest:     P{p['interest']}")
        print(f"    TOTAL OWED:   P{p['total']}")
        print()
        grand_total += p["total"]

    print(f"  GRAND TOTAL PENALTIES: P{round(grand_total, 2)}")
