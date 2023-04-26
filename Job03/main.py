class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Le Résultat du nombre1 et du nombre2 est :", resultat)

operation = Operation(12,3)
operation.addition()