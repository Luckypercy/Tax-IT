print("TAX COMPLIANCE REPORT")

company = input("Company name: ")
tax_type = input("Tax type (VAT/PAYE/WHT/CIT): ")
due_date = input("Due date: ")
status = input("Status: ")

risk = "Low"

if status.lower() == "outstanding":
    risk = "High"

print("\n--- REPORT ---")
print("Company:", company)
print("Tax Type:", tax_type)
print("Due Date:", due_date)
print("Status:", status)
print("Risk:", risk)