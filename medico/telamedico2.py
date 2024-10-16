from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout
import sys
import mysql.connector

class TelaMedico(QWidget):
    def __init__(self):
        super().__init__()
        
        # Tamanho e posição da janela
        self.setGeometry(50,50,300,500)        
        self.setFixedWidth(300)
        # Criação das labels para a janela Medico
        self.label_nome = QLabel("Nome Completo:")
        self.label_crm = QLabel("CRM:")
        self.label_telefone = QLabel("Telefone:")
        self.label_endereco = QLabel("Endereço:")
        self.label_especialidade = QLabel("Especialidade:")
        self.label_confirmacao = QLabel("")
        
        #Criação das line edits para os dados do Medico
        self.edit_nome = QLineEdit()
        self.edit_crm = QLineEdit()
        self.edit_telefone = QLineEdit()
        self.edit_endereco = QLineEdit()
        
        
        self.combo_especialidade = QComboBox()


        
        # Criar uma estrutura de repetição que vai 
        # fazer uma contagem de 1 a 31 e adicionar
        # a caixa(combobox) do dia
        list_especialidade = ["Cardiologia","Dermatologia","Neurologia","Endocrinologia","Ortopedia"]
        self.combo_especialidade.addItems(list_especialidade)
               
        
        #Criação do layout vertical
        self.layout_vertical = QVBoxLayout()
        self.layout_vertical.addWidget(self.label_nome)
        self.layout_vertical.addWidget(self.edit_nome)
        
        self.layout_vertical.addWidget(self.label_crm)
        self.layout_vertical.addWidget(self.edit_crm)
        
        self.layout_vertical.addWidget(self.label_telefone)
        self.layout_vertical.addWidget(self.edit_telefone)
        
        self.layout_vertical.addWidget(self.label_endereco)
        self.layout_vertical.addWidget(self.edit_endereco)
        
        self.layout_vertical.addWidget(self.label_especialidade)
        
        self.layout_vertical.addWidget(self.combo_especialidade)
        


        
        #criar o botão de cadastro
        self.button_cadastrar = QPushButton("Cadastrar")
        
        #chamar uma função vinculada ao botão cadastrar
        self.button_cadastrar.clicked.connect(self.cadastrar)
        
        # adicionar o botao ao layout
        self.layout_vertical.addWidget(self.button_cadastrar)
        
        # Adicionar a label de confirmação abaixo do 
        #botão cadastrar
        self.layout_vertical.addWidget(self.label_confirmacao)
        
        self.setLayout(self.layout_vertical)
        
    # Criar a função cadastrar que será acionada pelo botão
    # button_cadastrar. Esta função cadastra os dados do 
    # formulário no banco de dados clinicadb , dentro da 
    # tabela Medico
    def cadastrar(self):
        #para estabelecer a conexao com o banco de dados mysql
        #iremos usar um módulo chamado mysql-connector-python
        #a instalação é:
        #python -m pip install mysql-connector-python
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="clinicadb",
            port="3307"
        )
        
        #configurar um cursor para navegar na tabela
        cursor = conexao.cursor()
        
        # capturar os dados do formulário para efetuar 
        # o cadastro
        nome = self.edit_nome.text()
        crm = self.edit_crm.text()
        telefone = self.edit_telefone.text()
        endereco = self.edit_endereco.text()
        #especialidadelabel_especialidade = f"{self.combo_ano.currentText()}-{self.combo_mes.currentText()}-{self.combo_especialidade.currentText()}"
        
        # vamos criar uma variável que irá guardar o comando 
        # INSERT INTO, que insere os dados do formulário na tabela
        # Medico
        sqlCommand = f"INSERT INTO Medico(nomeMedico,crm,telefone,endereco,especialidade)VALUES('{nome}','{crm}','{telefone}','{endereco}','{self.combo_especialidade.currentText()}')"
   
        #Vamos executar o comando de INSERT  para cadastrar os dados
        #do formulário na tabela Medico. Utilizaremos o comando
        #execute
        cursor.execute(sqlCommand)
        

        
        #Para confirmar a inserção de dados na tabela
        #Medico, iremos usar o comando commit
        conexao.commit()
        
        #Exibir a mensagem de confirmação após clicar no botão
        #cadastrar
        self.label_confirmacao.setText("Medico cadastrado!")    
        
        #Limpar as caixas de texto
        self.edit_nome.setText("")
        self.edit_crm.setText("")
        self.edit_telefone.setText("")
        self.edit_endereco.setText("")
                
        cursor.close()
        conexao.close()
        
        
        
        
app = QApplication(sys.argv)
tela = TelaMedico()
tela.show()
app.exec_()
