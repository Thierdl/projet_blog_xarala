from django.shortcuts import render, redirect
from .import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import  User


#LOGIN_FUNCTION
def login_view(request):

  #create_formuler
  form = forms.LoginForm(request.POST or None)

  #vericated
  if form.is_valid():

    #recuperetion
    user_name = form.cleaned_data.get("username")
    pass_word = form.cleaned_data.get("pass_word")

    #authenticate
    user = authenticate(username=user_name, password=pass_word)

    if user is not None:
      
      #Cconnexion
      login(request, user)
      return redirect("page1")
      
    # render _html 
  return render(request, "account_e/login.html", {"form":form})


#SIGNUP_FUNCTION
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