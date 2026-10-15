from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
  # Todo este diseño HTML está siendo generado y controlado por Python
  return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Página Web en Python</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #eef2f3; text-align: center; padding-top: 50px; }
            h1 { color: #2c3e50; }
            p { font-size: 18px; color: #555; }
            .card { background: white; max-width: 500px; margin: 0 auto; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>¡Hola, profe! 👋</h1>
            <p>Esta página web está programada y ejecutada con <strong>Python y Flask</strong>.</p>
            <p>Proyecto subido exitosamente a GitHub.</p>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
  app.run(debug=True)
