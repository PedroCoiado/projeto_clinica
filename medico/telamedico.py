#from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QCalendarWidget
# import sys 
# import mysql.connector

#class TelaMedico (QWidget):
    #def __init__(self):
        super().__init__()

       # self.setGeometry(50,50,3000,499)
        #self.setFixedWidth(300)
        # Criação das labels para a janela telamedico
        #self.label_name = QLabel("Nome Completo")
        #self.label_crm = QLabel("CRM: ")
        #self.label_telefone = QLabel("Telefone: ")
        #self.label_address = QLabel("Endereço: ")
        #self.label_especialiade = QLabel ("Especialidade: ")
        #self.label_datacadastro = QLabel("Médico cadastrado dia: 25/12/2012")
        #self.label_confirmacao = QLabel("Confirmação: Aperte o botão e aguarde um instante! ")

        # Criação das Line Edits para os dados do Médico
        #self.edit_name = QLineEdit ()
        #self.edit_crm = QLineEdit ()
        #self.edit_telefone = QLineEdit ()
        #self.edit_address = QLineEdit ()
        #self.edit_especialidade = QLineEdit ()
        #self.edit_datacadastro = QLineEdit ()

        # Criação do Layout Vertical
        #self.layout_vertical = QVBoxLayout ()
        #self.layout_vertical.addWidget (self.label_name)
        #self.layout_vertical.addWidget (self.edit_name)

        #self.layout_vertical.addWidget (self.label_crm)
        #self.layout_vertical.addWidget (self.edit_crm)

        #self.layout_vertical.addWidget (self.label_telefone)
        #self.layout_vertical.addWidget (self.edit_telefone)
    
        #self.layout_vertical.addWidget (self.label_address)
        #self.layout_vertical.addWidget (self.edit_address)
        
        #self.layout_vertical.addWidget(self.label_datacadastro)

        # Criar o botão de cadastro
        #self.button_cadastrar = QPushButton("Cadastrar")

        # Chamar uma função vinculado ao botão cadastrar
        #self.button_cadastrar.clicked.connect(self.cadastrar)

        # Adicionar o botão ao layout
        #self.layout_vertical.addWidget(self.button_cadastrar)

        # Adicionar a label de confirmação abaixo do botão cadastrar
        #self.layout_vertical.addWidget(self.label_confirmacao)

        #self.setLayout(self.layout_vertical)


    #def cadastrar(self):
        print("Clicou no botão")



        #conexao = mysql.connector.connect(
            #host="127.0.0.1", # ou IP da maquina
            #user="root",
            #password="",
            #database="clinicadb",
            #port="3307"
        #)

        #cursor = conexao.cursor()
        
        #name = self.edit_name.text()
        #crm = self.edit_crm.text()
        #telefone = self.edit_telefone.text()
        #address = self.edit_address.text()
        #datacadastro = self.edit_datacadastro.text()

        #sqlCommand = f"INSERT INTO medico(nomemedico,crm,telefone,endereco,especialidade) VALUES('{name}','{crm}','{telefone}','{address}','{datacadastro}')"


        #conexao.commit()
        
        

        #self.label_confirmacao.setText("Paciente cadastrado!")

        #self.edit_name.setText("")
        #self.edit_crm.setText("")
        #self.edit_telefone.setText("")
        #self.edit_address.setText("")
        #datacadastro = self.edit_datacadastro.setText("")


        #cursor.close()
        #conexao.close()

#app = QApplication(sys.argv)
#tela = TelaMedico()
#tela.show()
#app.exec_()
