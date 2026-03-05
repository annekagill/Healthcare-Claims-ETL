import requests
import pandas as pd

def extract():
    url = "https://data.cms.gov/data-api/v1/dataset/92396110-2aed-4d63-a6a2-5d6207d46a29/data"
    response = requests.get(url, params={"limit": 1000})
    df = pd.DataFrame(response.json())
    return df