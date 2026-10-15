import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la conexión a PostgreSQL
# (Reemplaza 'usuario', 'contraseña', 'localhost:5432' y 'mi_base_de_datos' con tus datos reales)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://usuario:contraseña@localhost:5432/mi_base_de_datos"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Ejemplo de una tabla (Modelo) para la base de datos
class Registro(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  mensaje = db.Column(db.String(200), nullable=False)

  def __repr__(self):
    return f"<Registro {self.mensaje}>"


@app.route("/")
def home():
  return (
      "¡Hola! Mi servidor Flask con PostgreSQL está configurado correctamente."
  )


if __name__ == "__main__":
  with app.app_context():
    db.create_all()  # Crea las tablas en la base de datos si no existen
  app.run(debug=True)
