""" Filtering the email sum for each day of the week """
week_email = {}

try:
    with open(input(r'Insert *.txt file '), 'r', encoding='UTF-8') as handle:
        for lines in handle:
            lines.rstrip()
            words = lines.split()
            if len(words) == 0 or words[0] != 'From':
                continue
            weekd = words[2]
            if weekd not in week_email:
                week_email[weekd] = 1
            else:
                week_email[weekd] += 1
    print(week_email)
except Exception:
    print('Cannot reach file:')
    exit()

# Creio que o acumulo de instrução em bloco try:
# acaba sendo uma má prática, visto que na ocorrência
# de erros ele ignora completamente o restante do código...
