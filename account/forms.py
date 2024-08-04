from django import forms

class LoginForm(forms.Form):
  user_name = forms.CharField(label="User Name",
                              widget=forms.TextInput(
                                attrs={
                                  "class":"form-control"
                                }
                              ))
  
  pass_word = forms.CharField(label="Pass Word",
                                  widget=forms.PasswordInput(
                                    attrs={
                                      "class":"form-controls"
                                    }
                                  ))



class SignUpForm(forms.Form):
  last_name = forms.CharField(label="Last Name",
                         widget=forms.TextInput(
                           attrs={
                             "class":"form-control"
                           }
                         ))
  
  first_name = forms.CharField(label="First Name",
                              widget=forms.TextInput(
                                attrs={
                                  "class":"form-control"
                                }
                              ))
                            
  user_name = forms.CharField(label="User Name",
                              widget=forms.TextInput(
                                attrs={
                                  "class":"form-control"
                                }
                              ))
  
  """
  email = forms.CharField(label="Email",
                          widget=forms.EmailInput(
                            atrrs={
                              "class":"form-control"
                            }
                          ))
  """

  pass_word_1= forms.CharField(label="Pass Word",
                              widget=forms.PasswordInput(
                                attrs={
                                  "class":"form-control"
                                }
                              ))
  
  pass_word_2 = forms.CharField(label="Confirmed Pass Word",
                                    widget=forms.PasswordInput(
                                      attrs={
                                        "class":"form-control"
                                      }
                                    ))
  

  
  