from datetime import datetime, timedelta

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = None
        self.__cpf = None
        self.__telefone = None
        self.__nascimento = None
        self.setNome(nome)
        self.setCpf(cpf)
        self.setTelefone(telefone)
        self.setNascimento(nascimento)
    
    def setNome(self, nome):
        if nome != '': self.__nome = nome
        else: raise ValueError('Nome inválido')
    def setCpf(self, cpf):
        if len(cpf) == 11: self.__cpf = cpf
        else: raise ValueError('O CPF deve conter 11 caracteres')
    def setTelefone(self, telefone):
        if telefone != '': self.__telefone = telefone
        else: raise ValueError('Telefone inválido.')
    def setNascimento(self, nascimento):
        if nascimento < datetime.today(): self.__nascimento = nascimento
        else: raise ValueError('Você não pode nascer no futuro')

    def idade(self):
        dias = (datetime.today() - self.__nascimento).days
        anos = dias // 365
        dias = dias % 365
        meses = dias // 30
        dias = dias % 30
        return f'Você tem {anos} anos, {meses} meses e {dias} dias de vida!!'
    
    def __str__(self):
        return f'{self.__nome} | cpf: {self.__cpf} | telefone: {self.__telefone} | nascimento: {self.__nascimento}'

class UI:
    def menu():
        print('\n0 - Encerrar | 1 - novo paciente | 2 - mostrar idade | 3 - mostrar dados')
        op = int(input('Escolha uma das opções: '))
        return op

    def main():
        op = -1
        paciente = None
        while op != 0:
            op = UI.menu()
            if op == 1: paciente = UI.novoPaciente()
            elif op == 2: UI.mostrarIdade(paciente)
            elif op == 3: UI.mostrarDados(paciente)

    def novoPaciente():
        nome = input('Nome: ')
        cpf = input('CPF: ')
        telefone = input('Telefone: ')
        ano = int(input('Ano de nascimento: '))
        mes = int(input('Mês de nascimento: '))
        dia = int(input('Dia de nascimento: '))
        nascimento = datetime(ano, mes, dia)
        return Paciente(nome, cpf, telefone, nascimento)

    def mostrarIdade(paciente):
        print(paciente.idade())
    
    def mostrarDados(paciente):
        print(paciente)

UI.main()