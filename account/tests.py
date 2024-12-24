from django.test import TestCase
from .forms import LoginForm, SignUpForm

#from django import forms

class LoginForTest(TestCase):
    def test_loginform_valid(self):
        
        #donnée valide pour le formulaire
        form_data = {
            "user_name" : "name_test",
            "pass_word" : "password_test"
        }

        form = LoginForm(data=form_data)

        #verification de la validation du formulaire
        self.assertTrue(form.is_valid())

    

    def test_signup_form_valid(self):
        #soumettre

        form_data = {
            "last_name" : "albert",
            "first_name" : "mangua",
            "user_name" : "malbert",
            "pass_word_1" : "12345",
            "pass_word_2" : "12345",
        }

        form = SignUpForm(data=form_data)

        self.assertTrue(form.is_valid())

        #   -last_name
        #   -firstname
        #   -uqer_name
        #   -pass_word_1
        #   -pass_word_2

        #verifier

    
"""
def signup_view(request):

  #checke
  if request.method == "POST":

    form = forms.SignUpForm(request.POST)

    #vericated
    if form.is_valid():

      #recuperation_data
      last_name = form.cleaned_data.get("last_name")
      first_name = form.cleaned_data.get("first_name")
      user_name = form.cleaned_data.get("user_name")
      pass_word_1 = form.cleaned_data.get("pass_word_1")
      pass_word_2 = form.cleaned_data.get("pass_word_2")

      #verificate, if password 1 et 2
      if pass_word_1 != pass_word_2:

        
        form.add_error("pass_word_2", "les deux mots de pass sont different")

      else:
        user = User.objects.create_user(
              last_name=last_name,
              first_name=first_name, 
              username=user_name, 
              password=pass_word_1
          )
        
        user = authenticate(
              username=user_name, 
              password=pass_word_1
              )
      
      login(request, user)
      return redirect('page1')
    
  else:
    form = forms.SignUpForm()

  return render(request, "account_e/signup.html", {"form":form})


"""