from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


# Proteja a classe `Employee` para não ser instânciada diretamente:
# Torne obrigatório a implementação dos métodos da classe `Employee`,
# implemente-os se for necessários.
# -----------------------------------------------------------------
# Protejido implementando o "from abc import ABC, abstractmethod"
# implementando o (ABC) de classe Abstrata no Employee e o @abstratctmethod
# e tornado obrigatorio implementar os metodos, definindo na classe Employee

class Employee(ABC):
    # Padronize uma carga horária de 8 horas para todos os funcionários.
    # -------------------------------------------------------------------------
    # Setado uma variavel global da clase Employee com carga horária padrão
    # de 8 horas
    _workload = 8

    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    @abstractmethod
    def calc_bonus(self):
        pass

    @abstractmethod
    def get_hours(self):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)

        # Proteja o atributo `department` da classe `Manager`
        # para que seja acessado somente através do método `get_department`
        # -------------------------------------------------------------------
        # Protejido colocando o "_" antes do nome departament no
        # self._departament
        self._departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return super()._workload

    # Faça a correção dos métodos para que a herança funcione corretamente.
    # ------------------------------------------------------------------------
    # Corrigido nome dos metodos de department para departament
    def get_departament(self):
        return self._departament.name

    # Implementado método set_departament e corrido de set_department
    # para set_departament
    def set_departament(self, name):
        self._departament = name


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('sellers', 2)

        # Proteja o atributo `sales` da classe `Seller` para que não seja
        # acessado diretamente, crie um método chamado `get_sales` para
        # retornar o valor do atributo e `put_sales` para acrescentar
        # valores a esse atributo, lembrando que as vendas são acumulativas
        # ---------------------------------------------------------------------
        # Implementado o "_" antes da self._sales
        self._sales = 0

    # Criado métodos put_sales e implementado para retornar o que ele tem
    # mais o valor da nova venda, de forma cumulativa
    def put_sales(self, sales):
        self._sales = self._sales + sales

    # Criado métodos get_sales
    def get_sales(self):
        return self._sales

    # O cálculo do metodo `calc_bonus` do Vendedor dever ser calculado pelo
    # total de suas vendas vezes 0.15
    # -------------------------------------------------------------------------
    # Retornado o valor do calculo do total * 0.15
    def calc_bonus(self):
        return self._sales * 0.15

    def get_hours(self):
        return super()._workload

    # Implementado método get_departament e corrido de get_department
    # para get_departament
    def get_departament(self):
        return self._departament.name

    # Implementado método set_departament e corrido de set_department
    # para set_departament
    def set_departament(self, name):
        self._departament = name
