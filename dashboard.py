def dashboard_summary(returns, receipts):

    submitted = 0
    outstanding = 0

    for r in returns:

        if r["status"].lower() == "submitted":
            submitted += 1
        else:
            outstanding += 1

    print("\nDASHBOARD SUMMARY")
    print("---------------------------------------------")
    print(f"Returns:     {len(returns)}")
    print(f"Receipts:    {len(receipts)}")
    print(f"Submitted:   {submitted}")
    print(f"Outstanding: {outstanding}")
