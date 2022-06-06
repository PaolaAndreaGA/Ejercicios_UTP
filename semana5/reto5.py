import pandas as pd


# ruta file csv
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'


def listaPeliculas(rutaFileCsv: str) -> str:
    if rutaFileCsv.split('.')[-1] == 'csv?raw=true':
        try:
            file_csv = pd.read_csv(rutaFileCsv)
            sub_group_movies = file_csv[['Country', 'Language', 'Gross Earnings']]
            gain_country_lang = sub_group_movies.pivot_table(index=['Country', 'Language'])
            return gain_country_lang.head(10)
        except:
            print('Error al leer el archivo de datos.')
    else:
        print("Extensión inválida.")
    return

print(listaPeliculas(rutaFileCsv))