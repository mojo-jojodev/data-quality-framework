import pandas as pd
import pandera as pa
from pandera import Column, Check, DataFrameSchema

# Define strict DataFrame expectations
abillity_schema = DataFrameSchema({
    "Account_ID": Column(str, Check.str_matches(r"^[A-Z]+-\d+$")),
    "Billing_SKU": Column(str, Check.isin(["AB-VOIP", "AB-FIBER", "AB-LIC"])),
    "MRC": Column(float, Check.greater_than_or_equal_to(0.0)),
    "Status": Column(str, Check.isin(["ACTIVE", "PENDING"]))
})

if __name__ == "__main__":
    # Valid Data
    df_valid = pd.DataFrame({
        "Account_ID": ["ONEC-100", "ONEC-101"],
        "Billing_SKU": ["AB-VOIP", "AB-FIBER"],
        "MRC": [19.99, 149.99],
        "Status": ["ACTIVE", "PENDING"]
    })
    
    validated_df = abillity_schema.validate(df_valid)
    print("DataFrame passed quality checks.")
