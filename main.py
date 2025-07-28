def montar_prompt(dados_extraidos: dict) -> str:
    prompt = f"""
    Analise os seguintes dados extraídos de um relatório de crédito Serasa e retorne um resumo claro e direto:
    
    Serasa Score: {dados_extraidos.get('Serasa Score')}
    Anotações Negativas: {dados_extraidos.get('Anotacoes Negativas')}
    Renda Estimada: {dados_extraidos.get('Renda Estimada')}
    Capacidade de pagamento: {dados_extraidos.get('Capacidade de pagamento')}
    Comprometimento de renda: {dados_extraidos.get('Comprometimento de renda')}
    Histórico de Pagamento: {dados_extraidos.get('Histórico de Pagamento')}
    Recomenda: {dados_extraidos.get('Recomenda')}
    Limite mensal sugerido: {dados_extraidos.get('Limite mensal sugerido')}
    
    Explique se o cliente tem perfil bom para crédito e destaque os pontos positivos e negativos.
    """
    return prompt
