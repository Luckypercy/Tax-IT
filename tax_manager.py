def tax_summary(returns, receipts, penalties, submitted):
  print("\n========= TAXIT =========")
  print(f"Returns: {returns}")
  print(f"Receipts: {receipts}")
  print(f"Penalties: {penalties}")
  print(f"Submitted: {submitted}")
  outstanding = returns - submitted
  print(f"Outstanding: {outstanding}")