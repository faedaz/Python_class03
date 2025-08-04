# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas.
# Uma transação é considerada suspeita se o valor for superior a R$ 10.000 
# ou 
# se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

TRANSACAO = {'valor': 12000, 'hora': 12}

if TRANSACAO.get('valor', 0) > 10000 or TRANSACAO.get('hora', 0) < 9 or TRANSACAO.get('hora', 0) > 18:
    print('Suspect')
else:
    print('Not suspect')