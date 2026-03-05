import pandas as pd
from extract import extract

def transform():
    df = extract()
    # Keep only the columns we care about and rename them for better readability
    df = df[[
        "Rndrng_Prvdr_Type",
        "Tot_Srvcs",
        "Avg_Sbmtd_Chrg",
        "Avg_Mdcr_Pymt_Amt"
    ]].rename(columns={
        "Rndrng_Prvdr_Type": "Provider Type",
        "Tot_Srvcs": "Total Services",
        "Avg_Sbmtd_Chrg": "Average Submitted Charge",
        "Avg_Mdcr_Pymt_Amt": "Average Medicare Payment"
    })

    # Convert object data types to numeric
    df["Total Services"] = pd.to_numeric(df["Total Services"], errors="coerce")
    df["Average Submitted Charge"] = pd.to_numeric(df["Average Submitted Charge"], errors="coerce")
    df["Average Medicare Payment"] = pd.to_numeric(df["Average Medicare Payment"], errors="coerce") 

    # Calculate the reimbursement rate as a percentage
    df["Reimbursement Rate"] = (df["Average Medicare Payment"] / df["Average Submitted Charge"]) * 100  

    return df


if __name__ == "__main__":
    df = transform()
    print(df.dtypes)
    print("---")
    print(df.head())

