# models/maquilero.py
from .db import get_connection

mydb = get_connection()

class Maquilero:

    def __init__(self, id_maquilero, nombre, Ape_pat, Ape_mat, Direccion):
        self.id_maquilero = id_maquilero
        self.nombre = nombre
        self.Ape_pat = Ape_pat
        self.Ape_mat = Ape_mat
        self.Direccion = Direccion

    def save(self):
        if self.id_maquilero is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO maquilero(nombre, Ape_pat, Ape_mat, Direccion) VALUES(%s, %s, %s, %s)"
                val = (self.nombre, self.Ape_pat, self.Ape_mat, self.Direccion)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_maquilero = cursor.lastrowid
                return self.id_maquilero
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE maquilero SET nombre=%s, Ape_pat=%s, Ape_mat=%s, Direccion=%s WHERE id_maquilero=%s"
                val = (self.nombre, self.Ape_pat, self.Ape_mat, self.Direccion, self.id_maquilero)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_maquilero
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM maquilero WHERE id_maquilero = { self.id_maquilero }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_maquilero
            
    @staticmethod
    def get(id_maquilero):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre, Ape_pat, Ape_mat, Direccion FROM maquilero WHERE id_maquilero = { id_maquilero }"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                maquilero = Maquilero(id_maquilero, result["nombre"], result["Ape_pat"], result["Ape_mat"], result["Direccion"])
                return maquilero
            return None
        
    @staticmethod
    def get_all():
        maquileros = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_maquilero, nombre, Ape_pat, Ape_mat, Direccion FROM maquilero"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                maquileros.append(Maquilero(item["id_maquilero"], item["nombre"], item["Ape_pat"], item["Ape_mat"], item["Direccion"]))
            return maquileros
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_maquilero) FROM maquilero"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_maquilero } - { self.nombre }"
