import pandas as pd
import os



path_files = r"C:\Users\Usuário\Downloads\Docs"

list_files = os.listdir(path_files)

df = pd.DataFrame()

for file in list_files:
    if file.endswith('.xlsx'):
        path = os.path.join(path_files, file)

        data = pd.read_excel(path)

        df = pd.concat([df, data], ignore_index=True)

df.to_excel(os.path.join(path_files, 'mergin_files.xlsx'), index=False)
