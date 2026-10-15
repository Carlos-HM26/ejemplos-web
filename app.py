from flask import Flask

app = Flask(__name__)


@app.route("/")
def hola_mundo():
  return "¡Hola! Este es mi WebServer con Flask funcionando correctamente."


if __name__ == "__main__":
  app.run(debug=True)
