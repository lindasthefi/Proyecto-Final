from flask import Flask, render_template, request, redirect, url_for
from db import db
from usuario import usuario
class Programa:

    def __init__(self):
        self.app=Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///basedatos2.sqlite3"

        db.init_app(self.app)
        

        self.app.add_url_rule('/', view_func=self.buscarTodos)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET", "POST"])

        #Iniciar el servisor
        with self.app.app_context():
            db.create_all()
        self.app.run(debug=True)



    def mostrarTodos(self):
        return render_template('mostrarTodos.html', usurios2=usuario.query.all())


    def agregar(self):
        #VERIFICAR I DEBE ENVIAR EL FORMUALRIO OPROCESAR
        if request.method=="POST":
            #crear un objeto con los valores del formulario
            nombre=request.form['nombre']
            coordenadas=request.form['coordenadas']
            descripcion=request.form['descripcion']

            miUsuario=usuario(nombre, coordenadas, descripcion)

            #guardar un objeto en la base de datos
            db.session.add(miUsuario)
            db.session.commit()

            return redirect(url_for('mostrarTodos'))

        return render_template('baseDatos.html')
    

miPrograma=Programa()

