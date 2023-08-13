# models/tipo_tela.py
from .db import get_connection

mydb = get_connection()

class TipoTela:

    def __init__(self, id_tela, nombre_tela, precio):
        self.id_tela = id_tela
        self.nombre_tela = nombre_tela
        self.precio = precio

    def save(self):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO tipo_tela(id_tela, nombre_tela, precio) VALUES(%s, %s, %s)"
            val = (self.id_tela, self.nombre_tela, self.precio)
            cursor.execute(sql, val)
            mydb.commit()
            
    def update(self):
        with mydb.cursor() as cursor:
            sql = "UPDATE tipo_tela SET nombre_tela = %s, precio = %s WHERE id_tela = %s"
            val = (self.nombre_tela, self.precio, self.id_tela)
            cursor.execute(sql, val)
            mydb.commit()
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = "DELETE FROM tipo_tela WHERE id_tela = %s"
            val = (self.id_tela,)
            cursor.execute(sql, val)
            mydb.commit()
            
    @staticmethod
    def get(id_tela):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT id_tela, nombre_tela, precio FROM tipo_tela WHERE id_tela = %s"
            val = (id_tela,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            tela = TipoTela(result["id_tela"], result["nombre_tela"], result["precio"])
            return tela
        
    @staticmethod
    def get_all():
        telas = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT id_tela, nombre_tela, precio FROM tipo_tela"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                telas.append(TipoTela(item["id_tela"], item["nombre_tela"], item["precio"]))
            return telas
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = "SELECT COUNT(id_tela) FROM tipo_tela"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{self.id_tela} - {self.nombre_tela}"
