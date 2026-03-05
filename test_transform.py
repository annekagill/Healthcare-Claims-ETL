import pandas as pd
from transform import transform

def test_no_null_provider_type():
    df = transform()
    assert df["Provider Type"].isnull().sum() == 0

def test_reimbursement_rate_is_percentage():
    df = transform()
    assert df["Reimbursement Rate"].between(0, 100).all()

def test_total_services_is_numeric():
    df = transform()
    assert pd.api.types.is_numeric_dtype(df["Total Services"])
    assert pd.api.types.is_numeric_dtype(df["Average Submitted Charge"])
    assert pd.api.types.is_numeric_dtype(df["Average Medicare Payment"])
    assert pd.api.types.is_numeric_dtype(df["Reimbursement Rate"])

def test_expected_columns_present():
    df = transform()
    expected = ["Provider Type", "Total Services", 
                "Average Submitted Charge", 
                "Average Medicare Payment", 
                "Reimbursement Rate"]
    for col in expected:
        assert col in df.columns