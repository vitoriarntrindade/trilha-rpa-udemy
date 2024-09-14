import requests
import pandas as pd


def get_data_by_cnpj(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"

    response = requests.get(url=url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar dados do CNPJ: {response.status_code}")
        return None


def save_data_to_excel(company_data, file_name="company_data.xlsx"):
    if company_data:
        sanitize = sanitize_nested_data(company_data)

        df = pd.DataFrame([sanitize])

        df.to_excel(file_name, index=False)



def sanitize_nested_data(data):
    if "atividade_principal" in data:
        data["atividade_principal"] = "; ".join([ativ['text'] for ativ in data['atividade_principal']])

    if "atividades_secundarias" in data:
        data["atividades_secundarias"] = "; ".join([ativ['text'] for ativ in data['atividades_secundarias']])

    if "qsa" in data:
        data['qsa'] = "; ".join([f'{q["nome"]} ({q.get("qual", "")})' for q in data['qsa']])

    if 'billing' in data:
        data['billing'] = str(data['billing'])

    if 'extra'  in data:
        data['extra'] = str(data['extra'])

    return data

# Testando com o CNPJ existente (Petrobras)
company_test = get_data_by_cnpj("33000167000101")

# Salvando os dados no arquivo Excel
save_data_to_excel(company_test)