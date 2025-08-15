# Singleton Pattern: garante que só exista uma instância de uma classe
class ConfigSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.value = kwargs.get('value', None)
        return cls._instance

# Factory Pattern: cria objetos de acordo com um parâmetro
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Au au!"

class Cat(Animal):
    def speak(self):
        return "Miau!"

def animal_factory(tipo):
    if tipo == "dog":
        return Dog()
    elif tipo == "cat":
        return Cat()
    else:
        raise ValueError("Tipo desconhecido")

if __name__ == "__main__":
    # Testando Singleton
    config1 = ConfigSingleton(value=123)
    config2 = ConfigSingleton(value=456)
    print("Singleton value:", config1.value)
    print("Mesma instância?", config1 is config2)

    # Testando Factory
    dog = animal_factory("dog")
    cat = animal_factory("cat")
    print("Dog:", dog.speak())
    print("Cat:", cat.speak())
