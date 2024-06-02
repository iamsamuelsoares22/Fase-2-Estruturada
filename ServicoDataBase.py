import mysql.connector
from mysql.connector import Error

# ----------- Iniciar/Encerrar conexão ----------- #
def iniciarConexao(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

    

def encerrarConexao(con):
    con.close()


# ----------- Consultas ----------- #
def insertManifestacao(con, manifestacao, tipo):
    cursor = con.cursor()
    sql = "INSERT INTO manifestacoes (manifestacao, tipos) VALUES (%s, %s)"
    valores = (manifestacao, tipo)
    cursor.execute(sql, valores)
    con.commit()
    
    cursor.close()
    
    
    
def selectManifestacoes(con):
    cursor = con.cursor()
    sql = "SELECT * FROM manifestacoes"
    cursor.execute(sql)
    
    print("\nTodas as manifestações:\n\n")
    print(f"{'|Id':<5} {'|Manifestação':<30} {'|Tipo':<10}")
    print("-"*44)
    for (id, manifestacao, tipo) in cursor:
        print(f"{'|'+str(id):<5} {'|'+manifestacao:<30} {'|'+tipo:<10}")
        
    cursor.close()
    
def selectManifestacoesTipos(con, tipo):
    cursor = con.cursor()
    sql = f"SELECT * FROM manifestacoes WHERE tipos = '{tipo}'"
    cursor.execute(sql)
    
    print(f"\nTodas as manifestações com o tipo '{tipo}':\n\n")
    print(f"{'|Id':<5} {'|Manifestação':<30} {'|Tipo':<10}")
    print("-"*44)
    for (id, manifestacao, tipo) in cursor:
        print(f"{'|'+str(id):<5} {'|'+manifestacao:<30} {'|'+tipo:<10}")    
        
    cursor.close()
    
def selectManifestacaoID(con, codigo):
    cursor = con.cursor()
    sql = f"SELECT * FROM manifestacoes WHERE ID = '{codigo}'"
    cursor.execute(sql)
    manifestacao = cursor.fetchall()
    
    cursor.close()
        
    return manifestacao

def deleteManifestacao(con, codigo):
    cursor = con.cursor()
    sql = f"DELETE FROM manifestacoes WHERE ID = '{codigo}'"
    cursor.execute(sql)
    con.commit()
    
    cursor.close()
    
    
        