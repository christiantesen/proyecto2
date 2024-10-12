import pandas as pd

# Función para leer los datos desde un archivo CSV
def leer_datos_csv(ruta_archivo):
    df = pd.read_csv(ruta_archivo, encoding='latin-1')
    df_final = df[['DOMINIO', 'P101', 'P102', 'P103', 'P103A', 'P110F', 'P112A', 'P110C', 'P110C2', 'P110C3']]
    df_final.head() 
    df_final.replace("", pd.NA, inplace=True)  
    df_final.replace(" ", pd.NA, inplace=True) 
    df_final.drop(columns=['P110C2', 'P110C3'], inplace=True)
    df_final.rename(columns={
                         'P101':'TIPO_DE_VIVIENDA',
                         'P102':'MATERIAL_PARED_EXTERIOR',
                         'P103':'MATERIAL_PISO',
                         'P103A':'MATERIAL_TECHO',
                         'P110F':'PAGO_SERVICIO_AGUA',
                         'P112A':'ELECTRICO_EXCLUSIVO_COLECTIVO',
                         'P110C':'AGUA_SEMANA'}, inplace=True)
    mode_values = df_final.mode().iloc[0]
    df_final.fillna(mode_values, inplace=True)
    df_final.head()
    return df_final


