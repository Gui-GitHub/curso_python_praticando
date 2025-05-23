# Exemplo didático de Programação Orientada a Objetos (POO) em Python

# Classe base (superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome  # atributo público

    def falar(self):
        # Método a ser sobrescrito pelas subclasses
        print(f"{self.nome} faz um som.")

# Herança: Cachorro e Gato herdam de Animal
class Cachorro(Animal):
    def falar(self):
        print(f"{self.nome} diz: Au Au!")

class Gato(Animal):
    def falar(self):
        print(f"{self.nome} diz: Miau!")

# Encapsulamento: atributo privado
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade  # atributo protegido

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor >= 0:
            self._idade = valor

# Polimorfismo: função que aceita qualquer Animal
def fazer_animal_falar(animal):
    animal.falar()

# Criando objetos
dog = Cachorro("Rex")
cat = Gato("Mimi")
pessoa = Pessoa("João", 25)

# Usando polimorfismo
fazer_animal_falar(dog)
fazer_animal_falar(cat)

# Usando encapsulamento
print(f"{pessoa.nome} tem {pessoa.idade} anos.")
pessoa.idade = 30
print(f"{pessoa.nome} agora tem {pessoa.idade} anos.")
