from returns import add_return, show_returns, returns
from receipts import capture_receipt, receipts
from dashboard import dashboard_summary
from risk_engine import tax_risk


print("=============================================")
print("         WELCOME TO TaxIT")
print("=============================================")


# ADD RETURNS
add_return("VAT", 18000, "2026-05-28", "Pending")
add_return("PAYE", 12000, "2026-05-30", "Pending")
add_return("WHT", 19000, "2026-05-30", "Pending")


# CAPTURE RECEIPTS
capture_receipt("Sales Income", 5000)
capture_receipt("Salary Payments", 3000)
capture_receipt("WHT Payments", 18000)


# SHOW DASHBOARD
dashboard_summary(returns, receipts)


# SHOW REPORT
show_returns()


# RISK CHECK
risk = tax_risk("Outstanding")

print("\nQUICK TAX RISK CHECK")
print("---------------------------------------------")
print("Risk:", risk)