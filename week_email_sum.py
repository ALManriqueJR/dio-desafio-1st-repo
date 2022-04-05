""" Filtering the email sum for each day of the week """
week_email = {}

try:
    handle = open(input(r'Insert *.txt file '), 'r', encoding='UTF-8')
except Exception:
    print('Cannot reach file:')
    exit()

for lines in handle:
    words = lines.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    weekd = words[2]
    week_email[weekd] = week_email.get(weekd, 0) + 1
print(week_email)

# Na minha opinião esse formato é melhor,
# pois a única possivel entrada é o input do
# arquivo pelo usuário, de resto é tratamento
# para o resultado ser filtrado.
