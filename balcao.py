class estagiario:
    def __init__(self, nome, ):
        self.nome = nome
        self.horasOcupadas = 0

    def aumenta_salario(self, valor):
        self.salario += valor

    def mostra_dados(self):
        print("%s " % self.nome + " %d Horas"% self.horasOcupadas)


class grupoEstagiarios:
    def __init__(self):
        self.estagiarios = []

    def adiciona_estagiario(self, estagiario):
        self.estagiarios.append(estagiario)

    def mostra_estagiarios(self):
        for estagiario in self.estagiarios:
            estagiario.mostra_dados()

    def aumenta_horas_estagiario(self,hora, nomeEstagiario):
        for estagiario in self.estagiarios:
            if estagiario.nome == nomeEstagiario:
                estagiario.horasOcupadas += hora
    
def dois_menos_ocupados(grupoCedo, grupoTarde, horario):
    desocupado1 = ''
    desocupado2 = ''
    if horario == '12a13':
        grupoCedo.estagiarios.sort(key=lambda x: x.horasOcupadas)
        grupoCedo.aumenta_horas_estagiario(1, grupoCedo.estagiarios[0].nome)
        grupoCedo.aumenta_horas_estagiario(1, grupoCedo.estagiarios[1].nome)
        return grupoCedo.estagiarios[0:2]
    elif horario == '13a17':
        grupoJuntos = list(grupoCedo.estagiarios)
        for estagiario in grupoTarde.estagiarios:
            grupoJuntos.append(estagiario)
        grupoJuntos.sort(key=lambda x: x.horasOcupadas)
        grupoCedo.aumenta_horas_estagiario(4, grupoJuntos[0].nome)
        grupoCedo.aumenta_horas_estagiario(4, grupoJuntos[1].nome)
        grupoTarde.aumenta_horas_estagiario(4, grupoJuntos[0].nome)
        grupoTarde.aumenta_horas_estagiario(4, grupoJuntos[1].nome)
        return grupoJuntos[0:2]
    elif horario == '17a18':
        grupoTarde.estagiarios.sort(key=lambda x: x.horasOcupadas)
        grupoTarde.aumenta_horas_estagiario(1, grupoTarde.estagiarios[0].nome)
        grupoTarde.aumenta_horas_estagiario(1, grupoTarde.estagiarios[1].nome)
        return grupoTarde.estagiarios[0:2]
    return desocupado1, desocupado2
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

    def mostra_cronograma(self):
        for i in range(0, len(self.horario12a13)):
            print("12:00 às 13:00              13:00 às 17:00                 17:00 às 18:00")
            print("%s e" % self.horario12a13[i][0].nome + " %s" % self.horario12a13[i][1].nome + ' ;              ' +
                  "%s e" % self.horario13a17[i][0].nome + " %s" % self.horario13a17[i][1].nome + ' ;              ' + 
                  "%s e" % self.horario17a18[i][0].nome + " %s" % self.horario17a18[i][1].nome
)


def aumenta_horas(grupo, nomeEstagiario, horas):
    for estagiario in grupo.estagiarios:
        if estagiario.nome == nomeEstagiario:
            estagiario.horasOcupadas += horas

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

    horarios = cronograma()

    quantidade_dias = 10
    for i in range(0,quantidade_dias):
        horarios.adiciona_dupla(dois_menos_ocupados(grupoCedo, grupoTarde, '12a13'), '12a13')
        horarios.adiciona_dupla(dois_menos_ocupados(grupoCedo, grupoTarde, '13a17'), '13a17')
        horarios.adiciona_dupla(dois_menos_ocupados(grupoCedo, grupoTarde, '17a18'), '17a18')

    horarios.mostra_cronograma()
    grupoCedo.mostra_estagiarios()
    grupoTarde.mostra_estagiarios()
if __name__ == "__main__":
    main()