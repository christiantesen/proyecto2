import pandas as pd

# Función para leer los datos desde un archivo CSV
def leer_datos_csv(ruta_archivo):
    df = pd.read_csv(ruta_archivo, encoding='latin-1')
    df_final = df[['P101', 'P102', 'P103', 'P103A', 'P110F', 'P112A', 'P110C']]
    df_final.head()   
    df_final.rename(columns={'P101':'TIPO_DE_VIVIENDA',
                         'P102':'MATERIAL_PARED_EXTERIOR',
                         'P103':'MATERIAL_PISO',
                         'P103A':'MATERIAL_TECHO',
                         'P110F':'PAGO_SERVICIO_AGUA',
                         'P112A':'ELECTRICO_EXCLUSIVO_COLECTIVO',
                         'P110C':'AGUA_SEMANA',}, inplace=True)
    return df_final


