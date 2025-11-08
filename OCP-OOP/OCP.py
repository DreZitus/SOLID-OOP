class contratosClt:
    def salario(self):
        pass

class Estagio:
    def bolsaAuxilio(self):
        pass

class folhaDePagamento:
    
    def __init__(self):
        _saldo: float = 0.0

    def calcular(self, funcionario):
        if isinstance(funcionario, contratosClt):
            self._saldo = funcionario.salario()
        elif isinstance(funcionario, Estagio):
            self._saldo = funcionario.bolsaAuxilio()
        

            

