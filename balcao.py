class estagiario:
    def __init__(self, nome, ):
        self.nome = nome
        self.horasOcupadas = 0

    def aumenta_salario(self, valor):
        self.salario += valor

    def mostra_dados(self):
        print("Nome: %s" % self.nome)
        print("Horas Ocupadas: %d" % self.horasOcupadas)

class grupoEstagiarios:
    def __init__(self):
        self.estagiarios = []

    def adiciona_estagiario(self, estagiario):
        self.estagiarios.append(estagiario)

    def mostra_estagiarios(self):
        for estagiario in self.estagiarios:
            estagiario.mostra_dados()

class cronograma:
    def __init__(self):
        self.horario12a13 = []
        self.horario13a17 = []
        self.horario17a18 = []

    def adiciona_dupla(self, dupla, horario):
        if horario =='12a13':
            self.horario12a13.append(dupla)
        elif horario == '13a17':
            self.horario13a17.append(dupla)
        elif horario == '17a18':
            self.horario17a18.append(dupla)

        self.horas += horas

    def mostra_horas(self):
        print("Horas: %d" % self.horas)

def main():
    estagiario1 = estagiario("Joao")
    estagiario2 = estagiario("Maria")
    estagiario3 = estagiario("Jose")

    grupoCedo = grupoEstagiarios()
    grupoCedo.adiciona_estagiario(estagiario1)
    grupoCedo.adiciona_estagiario(estagiario2)
    grupoCedo.adiciona_estagiario(estagiario3)

    estagiario4 = estagiario("Henrique")
    estagiario5 = estagiario("Vivian")
    estagiario6 = estagiario("Mirian")

    grupoTarde = grupoEstagiarios()
    grupoTarde.adiciona_estagiario(estagiario4)
    grupoTarde.adiciona_estagiario(estagiario5)
    grupoTarde.adiciona_estagiario(estagiario6)



if __name__ == "__main__":
    main()