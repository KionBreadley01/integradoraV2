from .db import get_connection

mydb = get_connection()

class Producto:

    def __init__(self, id_producto, nombre_producto, tipo_tela, talla):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.tipo_tela = tipo_tela
        self.talla = talla

    def save(self):
        if self.id_producto is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO producto(nombre_producto, tipo_tela, talla) VALUES(%s, %s, %s)"
                val = (self.nombre_producto, self.tipo_tela, self.talla)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_producto = cursor.lastrowid
                return self.id_producto
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE producto SET nombre_producto=%s, tipo_tela=%s, talla=%s WHERE id_producto=%s"
                val = (self.nombre_producto, self.tipo_tela, self.talla, self.id_producto)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_producto
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM producto WHERE id_producto = { self.id_producto }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_producto
            
    @staticmethod
    def get(id_producto):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre_producto, tipo_tela, talla FROM producto WHERE id_producto = { id_producto }"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                producto = Producto(id_producto, result["nombre_producto"], result["tipo_tela"], result["talla"])
                return producto
            return None
        
    @staticmethod
    def get_all():
        productos = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_producto, nombre_producto, tipo_tela, talla FROM producto"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                productos.append(Producto(item["id_producto"], item["nombre_producto"], item["tipo_tela"], item["talla"]))
        return productos
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_producto) FROM producto"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_producto } - { self.nombre_producto }"
