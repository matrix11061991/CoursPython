## Les étapes suivantes a suivre pour créer un formulaire avec Django:

1. Créez un nouveau projet Django en utilisant la commande django-admin startproject <nom-du-projet> dans votre terminal.

2. Créez une nouvelle application Django en utilisant la commande python manage.py startapp <nom-de-l-application>.

3. Dans le fichier models.py de votre application, créez une classe pour le modèle de données que vous souhaitez stocker dans votre formulaire. Par exemple, si vous voulez stocker des informations sur les utilisateurs, vous pouvez créer une classe User avec des champs pour le nom, l'adresse e-mail, etc.

4. Créez un formulaire Django en créant une classe de formulaire dans un nouveau fichier forms.py dans votre application. Cette classe doit hériter de django.forms.Form et définir les champs de formulaire en utilisant les widgets appropriés. Par exemple, si vous voulez un champ de texte pour le nom, vous pouvez utiliser forms.CharField.

5. Dans le fichier views.py de votre application, créez une fonction de vue qui affiche le formulaire. Dans cette fonction, créez une instance de votre formulaire et passez-la au contexte de rendu pour affichage dans un modèle de rendu.

6. Dans le fichier urls.py de votre application, créez une nouvelle URL pour afficher le formulaire. Cette URL doit correspondre à la fonction de vue créée précédemment.

7. Enfin, créez un modèle de rendu qui affiche le formulaire dans votre template HTML. Vous pouvez utiliser les balises de modèle Django pour afficher les champs de formulaire et les messages d'erreur.


### Dans `model.py`
```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
```
### Dans  `forms.py` :
```python
from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email')
```
### Dans  `views.py` :
```python
from django.shortcuts import render
from .forms import UserForm

def user_signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            # For example, save it to the database
            User.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email']
            )
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})
```
### Dans  `urls.py` :
```python
from django.urls import path
from .views import user_signup

urlpatterns = [
    path('signup/', user_signup, name='user_signup'),
]
```
### Dans  `signup.html` :
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign up</button>
</form>
```


