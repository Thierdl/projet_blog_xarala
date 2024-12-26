from django.test import TestCase
from .forms import LoginForm, SignUpForm

#from django import forms

class LoginForTest(TestCase): #creation class de test
    def test_loginform_valid(self):
        form_data = {
            "user_name" : "name_test",
            "pass_word" : "password_test"
        }

        form = LoginForm(data=form_data) #

        #verification de la validation du formulaire
        self.assertTrue(form.is_valid())

    

    def test_signup_form_valid(self):
    
        form_data = {
            "last_name" : "albert",
            "first_name" : "mangua",
            "user_name" : "malbert",
                }
        form = SignUpForm(data=form_data)
        
        self.assertFalse(form.is_valid())


