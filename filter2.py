countries = ["", "Argentina", "", "Brazil", "Chile", "", "", "Colombia", ""]

res = list(filter(None, countries))

print(res)
# >>> ['Argentina', 'Brazil', 'Chile', 'Colombia']
