# How to convert a Pandas DataFrame to a Markdown Table

import pandas as pd

df = pd.DataFrame({
    'first_name': ['Alice', 'Bobby', 'Carl'],
    'salary': [175.1, 180.2, 190.3],
    'experience': [10, 15, 20]
})

markdown_table = df.to_markdown()

print(markdown_table)
