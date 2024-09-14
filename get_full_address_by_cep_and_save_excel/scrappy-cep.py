import pandas as pd
import requests
import openpyxl

def get_address_by_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        address = response.json()
        if "erro" not in address:
            return address
        else:
            return "CEP not found"
    else:
        return f"Erro na requisição: {response.status_code}"


#Exemplo utilizando uma lista de CEPS
ceps = ["01001-000", "01310-000", "01419-001", "01516-000", "02012-000", "03178-200", "04001-001", "04552-080", "05002-000", "05508-000"]

cps = []
for cep in ceps:
    ret = get_address_by_cep(cep)
    cps.append(ret)
    print(cps)

def save_address_excel(address_list, file_name='full_address.xlsx'):

    if "erro" not in address_list:

        df = pd.DataFrame(address_list)

        df.to_excel(file_name, index=False)


excel = save_address_excel(cps)