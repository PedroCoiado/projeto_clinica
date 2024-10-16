from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout
import sys
import mysql.connector

class TelaAgendamento(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(50,50,700,900)
        self.setWindowTitle("Tela de Agendamento")
        self.setContentsMargins(0,0,0,0)
        
        self.label_paciente = QLabel("Selecione o paciente:")
        self.label_medico = QLabel("Selecione o médico:")
        self.label_especialidade = QLabel("Selecione a especialidade:")
        self.label_data_atendimento = QLabel("Data do atendimento:")
        self.label_horario_atendimento = QLabel("Horário do atendimento:")
        self.label_observacao = QLabel("Observação:")
        self.label_confirmacao = QLabel("CONFIRMAÇÃO")

        self.label_dia = QLabel("Dia:")
        self.label_mes = QLabel("Mês:")
        self.label_ano = QLabel("Ano:")
        
        self.label_hora = QLabel("Hora:")
        self.label_minuto = QLabel("Minuto:")
        
        # ---------- declaração das combobox ---------------------
        self.combo_paciente = QComboBox()
        self.combo_medico = QComboBox()
        self.combo_especialidade = QComboBox()
        lista_especialidades = ["Cardiologia","Oncologia","Dermatologia","Neurologia"]
        self.combo_especialidade.addItems(lista_especialidades)

        

        self.combo_dia = QComboBox()
        lst_dia = [ ]
        for i in range (1,32):
            lst_dia.append(str(i))
        self.combo_dia.addItems(lst_dia)

        self.combo_mes = QComboBox()
        lst_mes = [ ]
        for sr in range (1,13):
            lst_mes.append(str(i))
        self.combo_mes.addItems(lst_mes)

        self.combo_ano = QComboBox()
        lst_ano = [ ]
        for i in range (1900,2025):
            lst_ano.append(str(i))
        self.combo_ano.addItems(lst_ano)
        
        self.combo_hora = QComboBox()
        lst_hora = [ ]
        for i in range (6,22):
            lst_hora.append(str(i))
        self.combo_hora.addItems(lst_hora)

        self.combo_minuto = QComboBox()
        lst_min = ["00","15","30","45"]
        self.combo_minuto.addItems(lst_min)
        
        # ----- declaração do botao
        self.button_cadastrar = QPushButton("Cadastrar")
        
        # ----- declaração da line edit para a observação
        self.edit_observacao = QLineEdit()
        
        # --- declaração do layout vertical para todos os controles
        self.layout_vertical_global = QVBoxLayout()
        self.layout_vertical_global.addWidget(self.label_paciente)
        self.layout_vertical_global.addWidget(self.combo_paciente)
        
        self.layout_vertical_global.addWidget(self.label_medico)
        self.layout_vertical_global.addWidget(self.combo_medico)
        
        self.layout_vertical_global.addWidget(self.label_especialidade)
        self.layout_vertical_global.addWidget(self.combo_especialidade)
        #----------------------------------------------------------
               
        self.label_horizontal = QLabel()
        self.layout_horizontal = QHBoxLayout()
        
        self.label_horizontal_data = QLabel()
        self.label_horizontal_data.setStyleSheet("QLabel{padding:0px}")
       
       
        self.layout_vertical_data = QVBoxLayout()
        self.layout_vertical_data.addWidget(self.label_data_atendimento)
        self.label_horizontal_data.setLayout(self.layout_vertical_data)
        
        self.label_controles_data = QLabel()
        self.layout_controles_horizontal_data = QHBoxLayout()
        
        self.layout_controles_horizontal_data.addWidget(self.label_dia)
        self.layout_controles_horizontal_data.addWidget(self.combo_dia)
        
        self.layout_controles_horizontal_data.addWidget(self.label_mes)
        self.layout_controles_horizontal_data.addWidget(self.combo_mes)
        
        self.layout_controles_horizontal_data.addWidget(self.label_ano)
        self.layout_controles_horizontal_data.addWidget(self.combo_ano)
        self.label_controles_data.setLayout(self.layout_controles_horizontal_data)
        self.layout_vertical_data.addWidget(self.label_controles_data)
        
        
        
        
        self.label_horizontal_hora = QLabel()
        self.label_horizontal_hora.setStyleSheet("QLabel{background-color:green;padding:px}")
        
        
        
        self.layout_vertical_hora = QVBoxLayout()
        self.layout_vertical_hora.addWidget(self.label_horario_atendimento)
        self.label_horizontal_hora.setLayout(self.layout_vertical_hora)
        
        self.label_controles_hora = QLabel()
        self.layout_controles_horizontal_hora = QHBoxLayout()
        
        self.layout_controles_horizontal_hora.addWidget(self.label_hora)
        self.layout_controles_horizontal_hora.addWidget(self.combo_hora)
        
        self.layout_controles_horizontal_hora.addWidget(self.label_minuto)
        self.layout_controles_horizontal_hora.addWidget(self.combo_minuto)
        
        
        self.label_controles_hora.setLayout(self.layout_controles_horizontal_hora)
        self.layout_vertical_hora.addWidget(self.label_controles_hora)
        
        # adicionar as labels horizontais data e hora no 
        # layout horizontal
        self.layout_horizontal.addWidget(self.label_horizontal_data)
        self.layout_horizontal.addWidget(self.label_horizontal_hora)
        
        
        
        # adicionar a label o layout horizontal
        self.label_horizontal.setLayout(self.layout_horizontal)
        

        

        
        self.layout_vertical_global.addWidget(self.label_horizontal)
        
        # -------------------------------------------------------------

        self.layout_vertical_global.addWidget(self.button_cadastrar)

        self.carregarPacientes()

        self.carregarMedicos()
        self.button_cadastrar.clicked.connect(self.cadastrarAgendamento)
        self.layout_vertical_global.addWidget(self.label_observacao)
        self.layout_vertical_global.addWidget(self.edit_observacao)

        self.layout_vertical_global.addWidget(self.label_confirmacao)

        self.setLayout(self.layout_vertical_global)

    def cadastrarAgendamento(self):
        idpac = self.combo_paciente.currentData()
        idmed = self.combo_medico.currentData()
        especialidade = self.combo_especialidade.currentText()
        dataagendamento = f"{self.combo_ano.currentText()}-{self.combo_mes.currentText()}-{self.combo_dia.currentText()}"
        horario = f"{self.combo_ano.currentText()}:{self.combo_minuto.currentText()}"
        observacao = self.edit_observacao.text()
       

        sqlCommand = f"INSERT INTO agendamento(idpaciente,idmedico,especialidade, dataatendimento,horaatendimento,observacao)VALUES({idpac},{idmed},'{especialidade}','{dataagendamento}','{horario}','{observacao}')"
        conexao = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password ="",
            database ="clinicadb",
            port ="3307"
        )    
        cursor = conexao.cursor()
        cursor.execute(sqlCommand)
        conexao.commit()
        cursor.close()
        conexao.close()
        self.label_confirmacao.setText("Agendamento realizado!")

    def carregarPacientes(self):
        conexao = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password ="",
            database ="clinicadb",
            port ="3307"

        )
        cursor = conexao.cursor()
        sqlCommand = "SELECT idpaciente, nome_paciente FROM paciente"
        cursor.execute(sqlCommand)
        for pac in cursor:
            self.combo_paciente.addItem(pac[1],pac[0])

        conexao.commit()
        cursor.close()
        conexao.close()

    def carregarMedicos(self):
        conexao = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password ="",
            database ="clinicadb",
            port ="3307"

        )
        cursor = conexao.cursor()
        sqlCommand = "SELECT idmedico, nomemedico FROM medico"
        cursor.execute(sqlCommand)
        for med in cursor:
            self.combo_medico.addItem(med[1],med[0])

        conexao.commit()
        cursor.close()
        conexao.close()

app = QApplication(sys.argv)
janela = TelaAgendamento()
janela.show()
app.exec_()

