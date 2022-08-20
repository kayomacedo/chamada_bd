import sqlite3


class Banco_de_Dados():


    def __init__(self):
        
        # criar banco de dados

        self.con = sqlite3.connect('bds/dados.db')

        self.cur = self.con.cursor()

        # Criar Tabela 

        self.cur.execute("create table if not exists usuarios (id integer primary key autoincrement, nome text  not null, senha text not null, dataregistro DATETIME DEFAULT(datetime('now','localtime')))")

        self.con.commit()

        # inserir dados 

    def inserir (self,nome,senha):
        self.nome = nome
        self.senha = senha
            
            
        self.cur.execute("insert into usuarios(nome,senha) values ('{}','{}')".format(str(nome),str(senha)))
        self.con.commit()

    def consultar(self):
        self.contatos = []
        
        for linha in self.cur.execute("select * from usuarios"):
            #print(linha)
            #print('Nome =' ,linha[1])
            self.contatos.append((f'{linha[0]}', f'{linha[1]}', f'{linha[2]}'))

        return self.contatos


Banco_de_Dados().consultar()









