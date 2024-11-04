import oracledb

def create_connection():
    connection = oracledb.connect(
        user="seu_usuario",
        password="sua_senha",
        dsn="localhost/orcl"  # ajuste o DSN conforme necessário
    )
    return connection
