# Dados de exemplo (vetor de faturamento diário de um ano)
faturamento_diario = [1000, 0, 1200, 1500, 0, 800, 0, 0, 1100, 1300, 0, 0, 0, 1600] # Exemplo simplificado

# Função que processa o faturamento
def analisar_faturamento(faturamento_diario):
    # Filtrando dias com faturamento (excluindo zeros)
    dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]

    if len(dias_com_faturamento) == 0:
        print("Nenhum dia com faturamento registrado.")
        return

    # Menor e maior valor de faturamento
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)

    # Média anual (excluindo dias sem faturamento)
    media_anual = sum(dias_com_faturamento) / len(dias_com_faturamento)

    # Número de dias com faturamento superior à média
    dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_anual)

    # Resultados
    print(f"Menor valor de faturamento: {menor_faturamento}")
    print(f"Maior valor de faturamento: {maior_faturamento}")
    print(f"Número de dias com faturamento superior à média anual: {dias_acima_da_media}")

# Chamando a função para análise
analisar_faturamento(faturamento_diario)
