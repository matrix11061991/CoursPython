# solution exo 1
```python
class Voiture:
    def __init__(self, marque, modele, annee, vitesse_max, nb_portes):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.vitesse_max = vitesse_max
        self.nb_portes = nb_portes
        self.vitesse_courante = 0

    def accelerer(self):
        self.vitesse_courante += 10
        if self.vitesse_courante > self.vitesse_max:
            self.vitesse_courante = self.vitesse_max
        print("La vitesse courante est de " + str(self.vitesse_courante) + " km/h")

    def freiner(self):
        self.vitesse_courante -= 7
        if self.vitesse_courante < 0:
            self.vitesse_courante = 0
        print("La vitesse courante est de " + str(self.vitesse_courante) + " km/h")

    def afficher_infos(self):
        print("Marque : " + self.marque)
        print("Modèle : " + self.modele)
        print("Année : " + str(self.annee))
        print("Vitesse maximale : " + str(self.vitesse_max) + " km/h")
        print("Nombre de portes : " + str(self.nb_portes))

ma_voiture = Voiture("Peugeot", "208", 2020, 180, 5)
ma_voiture.accelerer()
ma_voiture.accelerer()
ma_voiture.accelerer()
ma_voiture.freiner()
ma_voiture.afficher_infos()
```
# solution exo 2
```python
class Form:
    def __init__(self):
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)

    def render(self):
        form = '<form>'
        for field in self.fields:
            form += field.render()
        form += '</form>'
        return form

class TextField:
    def __init__(self, name):
        self.name = name

    def render(self):
        return '<input type="text" name="{}">'.format(self.name)

class PasswordField:
    def __init__(self, name):
        self.name = name

    def render(self):
        return '<input type="password" name="{}">'.format(self.name)

form = Form()
form.add_field(TextField("username"))
form.add_field(PasswordField("surname"))
form.add_field(PasswordField("password"))
print(form.render())
```
