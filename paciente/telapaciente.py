from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QCalendarWidget
import sys 
import mysql.connector

class TelaPaciente (QWidget):
    def __init__(self):
        super().__init__()


        # Tamanho e posição da janela
        self.setGeometry(50,50,300,499)
        self.setFixedWidth(300)
        # Criação das labels para a janela paciente
        self.label_name = QLabel("Nome completo: ")
        self.label_cpf = QLabel("CPF: ")
        self.label_telefone = QLabel("Telefone: ")
        self.label_address = QLabel("Endereço: ")
        self.label_datanascimento = QLabel(" Data de Nascimento: ")
        self.label_dia = QLabel("Dia: ")
        self.label_mes = QLabel("Mês: ")
        self.label_ano = QLabel("Ano: ")
        self.label_confirmacao = QLabel("Confirmação: Aperte o botão e aguarde um instante! ")


        # Criação das Line Edits para os dados do paciente
        self.edit_name = QLineEdit ()
        self.edit_cpf = QLineEdit ()
        self.edit_telefone = QLineEdit ()
        self.edit_address = QLineEdit ()
        self.edit_datanascimento = QLineEdit ()

        # Criação das comboBox para DIA/MÊS/ANO
        self.combo_dia = QComboBox ()
        self.combo_mes = QComboBox ()
        self.combo_ano = QComboBox ()

        # Criar ua estrutura de repetição que vai fazer uma de 1 à 31 e adicionar
        # a caixa(comboBox) do dia
        list_dia = []
        for i in range(1,32):
            list_dia.append(str(i))
        self.combo_dia.addItems(list_dia)

        # Criar ua estrutura de repetição que vai fazer uma de Janeiro à Dezembro e adicionar
        # a caixa(comboBox) do mês
        list_mes = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
        self.combo_mes.addItems(list_mes)

        # Criar ua estrutura de repetição que vai fazer uma de Janeiro à Dezembro e adicionar
        # a caixa(comboBox) do mês
        list_ano = []
        for i in range(1930,2010):
            list_ano.append(str(i))
        self.combo_ano.addItems(list_ano)


        # Criação do Layout Vertical
        self.layout_vertical = QVBoxLayout ()
        self.layout_vertical.addWidget (self.label_name)
        self.layout_vertical.addWidget (self.edit_name)

        self.layout_vertical.addWidget (self.label_cpf)
        self.layout_vertical.addWidget (self.edit_cpf)
        
        self.layout_vertical.addWidget (self.label_telefone)
        self.layout_vertical.addWidget (self.edit_telefone)
    
        self.layout_vertical.addWidget (self.label_address)
        self.layout_vertical.addWidget (self.edit_address)
        
        self.layout_vertical.addWidget(self.label_datanascimento)

        self.label_layout_horizontal = QLabel ()
        self.layout_horizontal = QHBoxLayout ()

        self.layout_horizontal.addWidget(self.label_dia)
        self.layout_horizontal.addWidget(self.combo_dia)

        self.layout_horizontal.addWidget(self.label_mes)
        self.layout_horizontal.addWidget(self.combo_mes)

        self.layout_horizontal.addWidget(self.label_ano)
        self.layout_horizontal.addWidget(self.combo_ano)

        self.label_layout_horizontal.setLayout(self.layout_horizontal)
        self.layout_vertical.addWidget(self.label_layout_horizontal)

        # Criar o botão de cadastro
        self.button_cadastrar = QPushButton("Cadastrar")

        # Chamar uma função vinculado ao botão cadastrar
        self.button_cadastrar.clicked.connect(self.cadastrar)

        # Adicionar o botão ao layout
        self.layout_vertical.addWidget(self.button_cadastrar)

        # Adicionar a label de confirmação abaixo do botão cadastrar
        self.layout_vertical.addWidget(self.label_confirmacao)

        self.setLayout(self.layout_vertical)

    # Criar a funçao cadastrar que será acionada pelo botão 
    # button_cadastrar. Está função cadastra os dados do formulário
    # no banco de dados clinicadb, dentro da tabela paciente
    def cadastrar(self):
        print("Clicou no botão")

        # Para estabelecer a conexão com o banco de dados mysql
        # iremos usar um módulo chamado mysql-connector-python
        # Comando para a instalação a seguir:
        # python -m pip install mysql-connector-python
        conexao = mysql.connector.connect(
            host="127.0.0.1", # ou IP da maquina
            user="root",
            password="",
            database="clinicadb",
            port="3307"
        )

        # Confirgurar um cursos para navegar na tabela
        cursor = conexao.cursor()

        # capturar os dados do formulário para efetuar o cadastro
        name = self.edit_name.text()
        cpf = self.edit_cpf.text()
        telefone = self.edit_telefone.text()
        address = self.edit_address.text()
        datanascimento = f"{self.combo_ano.currentText()}-{self.combo_mes.currentText()}-{self.combo_dia.currentText()}"

        #Vamos criar uma variável que irá guardar o comando 
        # INSERT, que insere os dados do formulário na tabela
        # paciente
        sqlCommand = f"INSERT INTO paciente(nome_paciente,cpf,telefone,endereco,datanascimento) VALUES('{name}','{cpf}','{telefone}','{address}','{datanascimento}')"

        # Vamos executar o comando INSERT para cadastrar os dados 
        # do formulário na tabela paciente, utilizaremos o comando
        # execute
        cursor.execute(sqlCommand)

        # Para confirmar a inserção de dados na tabela paciente,
        # iremos usar o comando commit

        conexao.commit()
        
        # Exibir a mensagem de confirmação após clicar no botão
        # cadastrar

        self.label_confirmacao.setText("Paciente cadastrado!")

        # Limpar as caixas de texto
        self.edit_name.setText("")
        self.edit_cpf.setText("")
        self.edit_telefone.setText("")
        self.edit_address.setText("")


        cursor.close()
        conexao.close()

app = QApplication(sys.argv)
tela = TelaPaciente()
tela.show()
app.exec_()


