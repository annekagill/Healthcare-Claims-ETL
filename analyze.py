import sqlite3
import pandas as pd

conn = sqlite3.connect("medicare.db")

# Question 1: Which provider types bill the most services?
q1 = """
SELECT "Provider Type", 
       SUM("Total Services") AS total_services
FROM medicare_claims
GROUP BY "Provider Type"
ORDER BY total_services DESC
LIMIT 10
"""

# Question 2: Which provider types have the highest reimbursement rate?
q2 = """
SELECT "Provider Type",
       ROUND(AVG("Reimbursement Rate"), 2) AS avg_reimbursement_rate
FROM medicare_claims
GROUP BY "Provider Type"
ORDER BY avg_reimbursement_rate DESC
LIMIT 10
"""

print("Top 10 Provider Types by Total Services Billed:")
print("---")
print(pd.read_sql(q1, conn))
print()
print("Top 10 Provider Types by Reimbursement Rate:")
print("---")
print(pd.read_sql(q2, conn))

# Follow-up Question: For the top billers, what is their reimbursement rate?
q3 = """
SELECT "Provider Type",
       SUM("Total Services") AS total_services,
       ROUND(AVG("Reimbursement Rate"), 2) AS avg_reimbursement_rate
FROM medicare_claims
GROUP BY "Provider Type"
ORDER BY total_services DESC
LIMIT 10
"""

print("Top Billers with their Reimbursement Rates:")
print("---")
print(pd.read_sql(q3, conn))

conn.close()