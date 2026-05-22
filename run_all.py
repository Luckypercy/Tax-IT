import datetime
import io
import sys

from returns import add_return, show_returns, returns
from receipts import capture_receipt, receipts
from dashboard import dashboard_summary
from penalties import show_penalties
from unallocated_receipts import add_unallocated_receipt, show_unallocated_receipts
from risk_engine import tax_risk


# =========================
# EXPORT HELPER
# =========================

def export_report(content: str):
    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"taxit_report_{today}.txt"
    with open(filename, "w") as f:
        f.write(content)
    print(f"\n  Report saved to: {filename}")


# =========================
# CAPTURE OUTPUT
# =========================

buffer = io.StringIO()
tee = sys.stdout


class Tee(io.TextIOBase):
    def write(self, msg):
        tee.write(msg)
        buffer.write(msg)
        return len(msg)
    def flush(self):
        tee.flush()


sys.stdout = Tee()


# =========================
# RUN ALL
# =========================

print("=" * 50)
print("           WELCOME TO TAX-IT")
print("    Botswana AI Tax Compliance Tool")
print(f"    Report Date: {datetime.date.today()}")
print("=" * 50)


print("\n[1] TAX RETURNS")
print("-" * 50)
add_return("VAT",  18000, "2026-05-28", "Pending")
add_return("PAYE", 12000, "2026-05-30", "Pending")
add_return("WHT",  19000, "2026-05-30", "Pending")
add_return("CIT",  25000, "2026-04-30", "Pending")


print("\n[2] RECEIPTS")
print("-" * 50)
capture_receipt("Sales Income",    5000)
capture_receipt("Salary Payments", 3000)
capture_receipt("WHT Payments",    18000)


print("\n[3] UNALLOCATED RECEIPTS")
print("-" * 50)
add_unallocated_receipt("VAT",  2500, "Payment received without submitted return")
add_unallocated_receipt("PAYE", 1800, "Payment exceeds submitted liability")
add_unallocated_receipt("WHT",  3200, "No matching return found for this period")
show_unallocated_receipts()


print("\n[4] DASHBOARD SUMMARY")
print("-" * 50)
dashboard_summary(returns, receipts)


print("\n[5] COMPLIANCE REPORT")
print("-" * 50)
show_returns()


print("\n[6] PENALTIES & LATE FEES")
print("-" * 50)
show_penalties(returns)


print("\n[7] QUICK TAX RISK CHECK")
print("-" * 50)
company  = "Lucky's Business"
tax_type = "VAT"
due_date = "2026-05-28"
status   = "Outstanding"
risk     = tax_risk(status)
print(f"  Company:  {company}")
print(f"  Tax Type: {tax_type}")
print(f"  Due Date: {due_date}")
print(f"  Status:   {status}")
print(f"  Risk:     {risk}")


print("\n" + "=" * 50)
print("          TAX-IT RUN COMPLETE")
print("=" * 50)


sys.stdout = tee
export_report(buffer.getvalue())
