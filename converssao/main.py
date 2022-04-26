import locale

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

valor_formatado = locale.currency(121231.4593681, grouping=True)
print(valor_formatado)
