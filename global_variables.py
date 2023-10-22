METRO_LINES = [f'IDFM:C0{id}' for id in range(1371, 1387)] # 1371 corresponds to Metro 1, 1372 to Metro 2, etc., and 1386 to Metro 14, 1387 to 3B, 1388 to 7B

COLOURS_METRO_LINES = {
    'IDFM:C01371': 'beige',
    'IDFM:C01372': 'darkblue',
    'IDFM:C01373': 'green',
    'IDFM:C01374': 'purple',
    'IDFM:C01375': 'orange',
    'IDFM:C01376': 'lightgreen',
    'IDFM:C01377': 'pink',
    'IDFM:C01378': 'white',
    'IDFM:C01379': 'black',
    'IDFM:C01380': 'darkgreen',
    'IDFM:C01381': 'darkred',
    'IDFM:C01382': 'darkpurple',
    'IDFM:C01383': 'darkgreen',
    'IDFM:C01384': 'lightblue',
    'IDFM:C01385': 'darkpurple',
    'IDFM:C01386': 'cadetblue',
    'IDFM:C01387': 'lightgreen',
}

# Work around hex values.
# COLOURS_METRO_LINES = {
#     'IDFM:C01371': '',
# ...
# }