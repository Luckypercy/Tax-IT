import datetime
import json
from dataclasses import dataclass, asdict
from typing import List, Optional
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

        self.load_data()


    # =========================
    # DATA STORAGE
    # =========================

    def save_data(self):

        data = {

            "returns":[asdict(r) for r in self.tax_returns],

            "receipts":[asdict(r) for r in self.receipts],

            "penalties":[asdict(p) for p in self.penalties]

        }

        with open(self.file,"w") as f:

            json.dump(data,f,indent=4)


    def load_data(self):

        if not Path(self.file).exists():
            return

        with open(self.file,"r") as f:

            data=json.load(f)

        self.tax_returns=[TaxReturn(**r) for r in data["returns"]]

        self.receipts=[Receipt(**r) for r in data["receipts"]]

        self.penalties=[Penalty(**p) for p in data["penalties"]]


    # =========================
    # RETURNS
    # =========================

    def add_tax_return(

        self,
        return_type,
        due_date,
        amount

    ):

        tax=TaxReturn(

            return_type,
            due_date,
            amount

        )

        self.tax_returns.append(tax)

        self.save_data()

        print(f"{return_type} return added")


    def submit_return(

        self,
        return_type

    ):

        today=str(datetime.date.today())

        for tax in self.tax_returns:

            if tax.return_type==return_type:

                tax.submitted=True

                tax.submission_date=today

                print(
                    f"{return_type} submitted"
                )

        self.save_data()


    # =========================
    # RECEIPTS
    # =========================

    def add_receipt(

        self,
        amount,
        tax_type,
        description

    ):

        receipt=Receipt(

            str(datetime.date.today()),
            amount,
            tax_type,
            description

        )

        self.receipts.append(receipt)

        self.save_data()

        print("Receipt captured")


    # =========================
    # REMINDERS
    # =========================

    def upcoming_returns(self):

        today=datetime.date.today()

        print("\nUpcoming Returns")

        for tax in self.tax_returns:

            due=datetime.datetime.strptime(
                tax.due_date,
                "%Y-%m-%d"
            ).date()

            days=(due-today).days

            if 0<=days<=self.reminder_days:

                print(

                    f"{tax.return_type} due in {days} days"

                )


    # =========================
    # LATE RETURNS
    # =========================

    def detect_late_returns(self):

        today=datetime.date.today()

        for tax in self.tax_returns:

            due=datetime.datetime.strptime(

                tax.due_date,
                "%Y-%m-%d"

            ).date()

            if today>due and not tax.submitted:

                penalty=Penalty(

                    "Late Filing",

                    500,

                    f"{tax.return_type} overdue",

                    str(today)

                )

                self.penalties.append(
                    penalty
                )

        self.save_data()


    # =========================
    # DASHBOARD
    # =========================

    def dashboard(self):

        print("\n========== TAX-IT ==========")

        print(
            f"Returns: {len(self.tax_returns)}"
        )

        print(
            f"Receipts: {len(self.receipts)}"
        )

        print(
            f"Penalties: {len(self.penalties)}"
        )

        submitted=sum(
            x.submitted
            for x in self.tax_returns
        )

        print(
            f"Submitted: {submitted}"
        )

        print("============================")


# =========================
# RUN APP
# =========================

agent=TaxComplianceAgent()

agent.add_tax_return(
    "VAT",
    "2026-05-28",
    18000
)

agent.add_receipt(
    5000,
    "VAT",
    "Sales Income"
)

agent.upcoming_returns()

agent.detect_late_returns()

agent.dashboard()


# =========================
# COMPLIANCE REPORT
# =========================

def generate_compliance_report(self):

    print("\n========== TAX COMPLIANCE REPORT ==========")

    total_returns = len(self.tax_returns)

    submitted = 0
    outstanding = 0
    overdue = 0

    today = datetime.date.today()

    for tax in self.tax_returns:

        due = datetime.datetime.strptime(
            tax.due_date,
            "%Y-%m-%d"
        ).date()

        status = ""

        if tax.submitted:

            submitted += 1
            status = "Submitted"

        elif today > due:

            overdue += 1
            status = "OVERDUE"

        else:

            outstanding += 1
            status = "Pending"


        print(
            f"""
Tax Type: {tax.return_type}
Due Date: {tax.due_date}
Amount: P{tax.amount}
Status: {status}
--------------------------
"""
        )

    print("\nSUMMARY")

    print(f"Total Returns: {total_returns}")
    print(f"Submitted: {submitted}")
    print(f"Outstanding: {outstanding}")
    print(f"Overdue: {overdue}")

    print(
        f"Penalties Identified: {len(self.penalties)}"
    )

    print("==========================================")
