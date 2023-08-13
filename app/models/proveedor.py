from .db import get_connection

mydb = get_connection()

class Proveedor:

    def __init__(self, id_proveedor, nombre, Ape_pat, Ape_mat, Direccion, id_tela   ):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.Ape_pat = Ape_pat
        self.Ape_mat = Ape_mat
        self.Direccion = Direccion
        self.id_tela = id_tela

    def save(self):
        if self.id_proveedor is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO proveedor(nombre, Ape_pat, Ape_mat, Direccion, id_tela) VALUES(%s, %s, %s, %s, %s)"
                val = (self.nombre, self.Ape_pat, self.Ape_mat, self.Direccion, self.id_tela)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_proveedor = cursor.lastrowid
                return self.id_proveedor
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE proveedor SET nombre=%s, Ape_pat=%s, Ape_mat=%s, Direccion=%s, id_tela=%s WHERE id_proveedor=%s"
                val = (self.nombre, self.Ape_pat, self.Ape_mat, self.Direccion, self.id_tela, self.id_proveedor)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_proveedor
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM proveedor WHERE id_proveedor = { self.id_proveedor }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_proveedor
            
    @staticmethod
    def get(id_proveedor):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre, Ape_pat, Ape_mat, Direccion, id_tela FROM proveedor WHERE id_proveedor = { id_proveedor }"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                proveedor = Proveedor(id_proveedor, result["nombre"], result["Ape_pat"], result["Ape_mat"], result["Direccion"], result["id_tela"])
                return proveedor
            return None
        
    @staticmethod
    def get_all():
        proveedores = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_proveedor, nombre, Ape_pat, Ape_mat, Direccion, id_tela FROM proveedor"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                proveedores.append(Proveedor(item["id_proveedor"], item["nombre"], item["Ape_pat"], item["Ape_mat"], item["Direccion"], item["id_tela"]))
        return proveedores
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_proveedor) FROM proveedor"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_proveedor } - { self.nombre }"
