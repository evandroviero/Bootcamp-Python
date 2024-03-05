import psycopg2

class BancoDeDadosPost:
    def __init__(self, host, port, banco, user, senha) -> None:
        self.host = host
        self.porta = port
        self.banco = banco
        self.usuario = user
        self.senha = senha
        self.conexao = None

    def conectar(self):
        self.conexao == psycopg2(
            host = self.host,
            port = self.porta,
            database = self.banco,
            user = self.usuario,
            password = self.senha
        )