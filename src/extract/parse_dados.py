# src/extract/parse_dados.py

import re

def parse_dados(texto: str) -> dict:
    dados = {}

    # Função auxiliar pra encontrar valor após a palavra-chave
    def extrair_valor(chave, texto):
        # Busca a linha que contém a chave
        pattern = rf"{chave}[:\s]*([^\n\r]*)"
        match = re.search(pattern, texto, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return None

    # Extraindo cada campo
    dados['Serasa Score'] = extrair_valor("Serasa Score", texto)
    dados['Anotacoes Negativas'] = extrair_valor("Anotações Negativas", texto)
    dados['Renda Estimada'] = extrair_valor("Renda Estimada", texto)
    dados['Capacidade de pagamento'] = extrair_valor("Capacidade de pagamento", texto)
    dados['Comprometimento de renda'] = extrair_valor("Comprometimento de renda", texto)
    dados['Histórico de Pagamento'] = extrair_valor("Histórico de Pagamento", texto)
    dados['Recomenda'] = extrair_valor("Recomenda", texto)
    dados['Limite mensal sugerido'] = extrair_valor("Limite mensal sugerido", texto)

    # Opcional: converter valores numéricos onde fizer sentido
    def to_float(valor):
        if not valor:
            return None
        valor = valor.replace(".", "").replace(",", ".")
        try:
            return float(valor)
        except:
            return None

    dados['Serasa Score'] = int(dados['Serasa Score']) if dados['Serasa Score'] and dados['Serasa Score'].isdigit() else None
    dados['Renda Estimada'] = to_float(dados['Renda Estimada'])
    dados['Capacidade de pagamento'] = to_float(dados['Capacidade de pagamento'])
    dados['Comprometimento de renda'] = to_float(dados['Comprometimento de renda'])
    dados['Limite mensal sugerido'] = to_float(dados['Limite mensal sugerido'])

    return dados
