# models/entrada_tela.py

from .db import get_connection

mydb = get_connection()

class EntradaTela:

    def __init__(self, id_entrada, id_proveedor, id_tela, tela, metros, fecha_entrada):
        self.id_entrada = id_entrada
        self.id_proveedor = id_proveedor
        self.id_tela = id_tela
        self.tela = tela
        self.metros = metros
        self.fecha_entrada = fecha_entrada

    def save(self):
        if self.id_entrada is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO entrada_tela(id_proveedor, id_tela, tela, metros, fecha_entrada) VALUES(%s, %s, %s, %s, %s)"
                val = (self.id_proveedor, self.id_tela, self.tela, self.metros, self.fecha_entrada)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_entrada = cursor.lastrowid
                return self.id_entrada
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE entrada_tela SET id_proveedor = %s, id_tela = %s, tela = %s, metros = %s, fecha_entrada = %s WHERE id_entrada = %s"
                val = (self.id_proveedor, self.id_tela, self.tela, self.metros, self.fecha_entrada, self.id_entrada)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_entrada
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM entrada_tela WHERE id_entrada = {self.id_entrada}"
            cursor.execute(sql)
            mydb.commit()
            return self.id_entrada
            
    @staticmethod
    def get(id_entrada):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_entrada, id_proveedor, id_tela, tela, metros, fecha_entrada FROM entrada_tela WHERE id_entrada = {id_entrada}"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return EntradaTela(
                    id_entrada=result["id_entrada"],
                    id_proveedor=result["id_proveedor"],
                    id_tela=result["id_tela"],
                    tela=result["tela"],
                    metros=result["metros"],
                    fecha_entrada=result["fecha_entrada"]
                )
            return None
        
    @staticmethod
    def get_all():
        entradas = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_entrada, id_proveedor, id_tela, tela, metros, fecha_entrada FROM entrada_tela"
            cursor.execute(sql)
            result = cursor.fetchall()
            for entrada in result:
                entradas.append(
                    EntradaTela(
                        id_entrada=entrada["id_entrada"],
                        id_proveedor=entrada["id_proveedor"],
                        id_tela=entrada["id_tela"],
                        tela=entrada["tela"],
                        metros=entrada["metros"],
                        fecha_entrada=entrada["fecha_entrada"]
                    )
                )
        return entradas
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_entrada) FROM entrada_tela"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{self.id_entrada} - {self.tela}"
