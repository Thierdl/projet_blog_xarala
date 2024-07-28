from django import forms

class LoginForm(forms.Form):
  user_name = forms.CharField(label="user name",
                              widget=forms.TextInput(
                                attrs={
                                  "class" : "form-control"
                                }
                              ))
  
  pass_word = forms.PasswordInput(label="pass word",
                                  widget=forms.passwordInput(
                                    attrs={
                                      "class" : "form-controls"
                                    }
                                  )
  )