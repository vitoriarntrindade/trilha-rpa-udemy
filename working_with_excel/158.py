import pandas as pd
import os

path = r"C:\Users\Usuário\Downloads\Docs"
files = os.listdir(path)
merged_data = pd.DataFrame()

for file in files:
    if file.endswith('.xlsx'):
        data = pd.read_excel(os.path.join(path, file))
        merged_data = pd.concat([merged_data, data], ignore_index=True)

merged_data.to_excel(os.path.join(path, 'merged_files.xlsx'), index=False)
