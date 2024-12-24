from django.test import TestCase
from .forms import LoginForm
#from django import forms

class LoginForTest(TestCase):
    def test_loginform(self):
        
        #donnée valide pour le formulaire
        form_data = {
            "user_name" : "name_test",
            "pass_word" : "password_test"
        }

        form = LoginForm(data=form_data)

        #verification de la validation du formulaire
        self.assertTrue(form.is_valid())

    

    def signup(self):
       pass
