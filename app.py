from fasthtml.common import FastHTML, serve
from flask import Flask, render_template, send_from_directory,url_for
from jinja2 import Environment, FileSystemLoader
from limpieza import leer_datos_csv
import os

# Inicializar la aplicación
app = Flask(__name__)
env = Environment(loader=FileSystemLoader('templates'))
env.globals['url_for'] = url_for  # Registrar url_for manualmente

# Función para convertir el DataFrame a HTML
def generar_tabla_html(df):
    filas = ""
    encabezados = "".join([f"<th>{col}</th>" for col in df.columns])
    for _, fila in df.iterrows():
        filas += "<tr>" + "".join([f"<td>{dato}</td>" for dato in fila]) + "</tr>"
    return f"<table class='table'><thead><tr>{encabezados}</tr></thead><tbody>{filas}</tbody></table>"

# Definir la ruta principal
@app.get('/')
def home():
    # Ruta del archivo CSV que quieres leer
    ruta_archivo = 'Enaho01-2020-100.csv'
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"El archivo {ruta_archivo} no existe.")
    df = leer_datos_csv(ruta_archivo)  # Leer los datos desde el archivo CSV
    # Crear la página HTML con los estilos de tabla y colo pasteles
    list_of_dicts = df.to_dict(orient='records')   
    template = env.get_template('index.html')
    return  template.render({ "registros":list_of_dicts,"columns": list(df.columns)})

# Nueva ruta para la página de gráficos
@app.get('/graficos')
def graficos():
    template = env.get_template('graficos.html')
    return template.render()

if __name__ == '__main__':
    app.run(debug=True)