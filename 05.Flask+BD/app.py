from flask import Flask, render_template, request, redirect, flash
import controlador_juegos

app = Flask(__name__)

@app.route("/")
@app.route("/juegos")
def juegos():
    juegos = controlador_juegos.obtener_juegos()
    return render_template("juegos.html", juegos=juegos)

@app.route("/agregar_juego")
def formulario_agregar_juego():
    return render_template("agregar_juego.html")

@app.route("/guardar_juego", methods=["POST"])
def guardar_juego():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    
    controlador_juegos.insetar_juego(nombre, descripcion, precio)
    
    return redirect("/juegos")
    

@app.route("/editar_juego/<int:id>")
def formulario_editar_juego(id):
    juego = controlador_juegos.obtener_juego_por_id(id)
    return render_template("editar_juego.html", juego=juego)

@app.route("/actualizar_juego/<int:id>", methods=["POST"])
def actualizar_juego(id):
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    
    controlador_juegos.actualizar_juego(id, nombre, descripcion, precio)
    return redirect("/juegos")




@app.route("/eliminar_juego/<int:id>", methods=["GET"])
def eliminar_juego(id):
    try:
        controlador_juegos.eliminar_juego(id)
    except Exception as e:
        print(f"Error al eliminar juego: {e}")
    return redirect("/juegos")

@app.route("/detalles/<int:id>")
def detalles(id):
    juego = controlador_juegos.obtener_juego_por_id(id)
    return render_template("detalles.html",juego=juego)


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)





