import datetime
import json
from dataclasses import dataclass, asdict
from typing import Optional
from pathlib import Path


# =========================
# MODELS
# =========================

@dataclass
class TaxReturn:
    return_type: str
    due_date: str
    amount: float
    submitted: bool = False
    submission_date: Optional[str] = None


@dataclass
class Receipt:
    date: str
    amount: float
    tax_type: str
    description: str


@dataclass
class Penalty:
    penalty_type: str
    amount: float
    description: str
    date_identified: str


# =========================
# TAX COMPLIANCE AGENT
# =========================

class TaxComplianceAgent:

    def __init__(self):
        self.file = "tax_data.json"
        self.tax_returns = []
        self.receipts = []
        self.penalties = []
        self.reminder_days = 7

    def save_data(self):
        data = {
            "returns": [asdict(r) for r in self.tax_returns],
            "receipts": [asdict(r) for r in self.receipts],
            "penalties": [asdict(p) for p in self.penalties]
        }
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def add_tax_return(self, return_type, due_date, amount):
        tax = TaxReturn(return_type, due_date, amount)
        self.tax_returns.append(tax)
        print(f"  {return_type} return added (P{amount})")

    def add_receipt(self, amount, tax_type, description):
        receipt = Receipt(str(datetime.date.today()), amount, tax_type, description)
        self.receipts.append(receipt)
        print(f"  Receipt captured: {description} (P{amount})")

    def upcoming_returns(self):
        today = datetime.date.today()
        found = False
        for tax in self.tax_returns:
            due = datetime.datetime.strptime(tax.due_date, "%Y-%m-%d").date()
            days = (due - today).days
            if 0 <= days <= self.reminder_days:
                print(f"  REMINDER: {tax.return_type} due in {days} days ({tax.due_date})")
                found = True
        if not found:
            print("  No upcoming returns in the next 7 days.")

    def detect_late_returns(self):
        today = datetime.date.today()
        for tax in self.tax_returns:
            due = datetime.datetime.strptime(tax.due_date, "%Y-%m-%d").date()
            if today > due and not tax.submitted:
                penalty = Penalty("Late Filing", 500, f"{tax.return_type} overdue", str(today))
                self.penalties.append(penalty)
                print(f"  PENALTY: {tax.return_type} is overdue — P500 penalty added")

    def dashboard(self):
        submitted = sum(x.submitted for x in self.tax_returns)
        outstanding = len(self.tax_returns) - submitted
        print(f"  Returns:     {len(self.tax_returns)}")
        print(f"  Receipts:    {len(self.receipts)}")
        print(f"  Submitted:   {submitted}")
        print(f"  Outstanding: {outstanding}")
        print(f"  Penalties:   {len(self.penalties)}")

    def compliance_report(self):
        today = datetime.date.today()
        submitted = outstanding = overdue = 0
        for tax in self.tax_returns:
            due = datetime.datetime.strptime(tax.due_date, "%Y-%m-%d").date()
            if tax.submitted:
                submitted += 1
                status = "Submitted"
            elif today > due:
                overdue += 1
                status = "OVERDUE"
            else:
                outstanding += 1
                status = "Pending"
            print(f"  {tax.return_type:<6} | Due: {tax.due_date} | P{tax.amount:<8} | {status}")
        print(f"\n  Total: {len(self.tax_returns)} | Submitted: {submitted} | Outstanding: {outstanding} | Overdue: {overdue}")
        print(f"  Penalties: {len(self.penalties)}")


# =========================
# RUN THE PROJECT
# =========================

print("=" * 45)
print("         WELCOME TO TAX-IT")
print("   Botswana AI Tax Compliance Tool")
print("=" * 45)

agent = TaxComplianceAgent()

print("\n[1] ADDING TAX RETURNS")
print("-" * 45)
agent.add_tax_return("VAT",  "2026-05-28", 18000)
agent.add_tax_return("PAYE", "2026-05-30", 12000)
agent.add_tax_return("WHT",  "2026-06-15", 8500)

print("\n[2] CAPTURING RECEIPTS")
print("-" * 45)
agent.add_receipt(5000, "VAT",  "Sales Income")
agent.add_receipt(3000, "PAYE", "Salary Payments")
agent.add_receipt(1500, "WHT",  "Withholding Payment")

print("\n[3] CHECKING REMINDERS")
print("-" * 45)
agent.upcoming_returns()

print("\n[4] DETECTING LATE RETURNS")
print("-" * 45)
agent.detect_late_returns()

print("\n[5] DASHBOARD SUMMARY")
print("-" * 45)
agent.dashboard()

print("\n[6] COMPLIANCE REPORT")
print("-" * 45)
agent.compliance_report()

print("\n[7] QUICK TAX RISK CHECK")
print("-" * 45)
company   = "Lucky's Business"
tax_type  = "VAT"
due_date  = "2026-05-28"
status    = "Outstanding"
risk      = "High" if status.lower() == "outstanding" else "Low"
print(f"  Company:  {company}")
print(f"  Tax Type: {tax_type}")
print(f"  Due Date: {due_date}")
print(f"  Status:   {status}")
print(f"  Risk:     {risk}")

agent.save_data()

print("\n" + "=" * 45)
print("         TAX-IT RUN COMPLETE")
print("=" * 45)
