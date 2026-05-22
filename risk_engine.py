def tax_risk(status):

    if status.lower() == "outstanding":
        return "High"

    return "Low"
