from fasthtml.common import FastHTML, serve
from jinja2 import Environment, FileSystemLoader
from limpieza import leer_datos_csv

# Inicializar la aplicación
app = FastHTML()
env = Environment(loader=FileSystemLoader('.'))
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
    df = leer_datos_csv(ruta_archivo)  # Leer los datos desde el archivo CSV

    # Generar la tabla HTML a partir de los datos
    columns_list = list(df.columns)
  
    # Crear la página HTML con los estilos de tabla y colo pasteles
    
    list_of_dicts = df.to_dict(orient='records')   

    template = env.get_template('index.html')
    return  template.render({ "registros":list_of_dicts,"columns": list(df.columns)})

# Servir la aplicación
serve()
