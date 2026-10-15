import os
from flask import Flask, redirect, render_template_string, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos (usará SQLite por defecto si no hay PostgreSQL configurado)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Definición de una tabla simple para la base de datos
class Visita(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  contador = db.Column(db.Integer, nullable=False)


@app.route("/")
def inicio():
  # Buscar o crear un registro de visitas en la base de datos
  visita = Visita.query.first()
  if not visita:
    visita = Visita(contador=1)
    db.session.add(visita)
  else:
    visita.contador += 1
  db.session.commit()

  # HTML generado por Python que muestra los datos de la base de datos
  html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Flask + Base de Datos</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f0f2f5; text-align: center; padding-top: 50px; }
            .card { background: white; max-width: 500px; margin: 0 auto; padding: 30px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; }
            p { font-size: 18px; color: #555; }
            .badge { background: #3498db; color: white; padding: 5px 10px; border-radius: 5px; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>¡Flask + Base de Datos! 🗄️</h1>
            <p>Esta página web está conectada a una base de datos.</p>
            <p>Número de visitas registradas: <span class="badge">{{ visitas }}</span></p>
        </div>
    </body>
    </html>
    """
  return render_template_string(html_template, visitas=visita.contador)


if __name__ == "__main__":
  with app.app_context():
    db.create_all()  # Crea la base de datos y las tablas automáticamente
  app.run(debug=True)
