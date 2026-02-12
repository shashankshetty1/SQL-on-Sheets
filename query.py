import duckdb
import pandas as pd

con = duckdb.connect()

df = con.execute("""
                 

SELECT 
    COUNT(*) AS discovery_count,
    SUM(TOTAL_AMOUNT) AS discovery_total_amount
FROM read_csv_auto('data.csv')
WHERE STAGE_NAME = '3 Discovery';

//Shetty




                 
                 
""").fetchdf()

print(df.to_string(index=False))
