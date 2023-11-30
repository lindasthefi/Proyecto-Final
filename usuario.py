from db import db

class usuario(db.Model):
    #nombre de tabla
    __tablename__="usuario"

    #conjunto de atributos
    #Llave primaria
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    coordenadas=db.Column(db.String(50))
    descripcion=db.Column(db.String(500))
    
    #método constructor
    def __init__(self, nombre, coordenadas,descripcion):
        self.nombre=nombre
        self.coordenadas=coordenadas
        self.decripcion=descripcion