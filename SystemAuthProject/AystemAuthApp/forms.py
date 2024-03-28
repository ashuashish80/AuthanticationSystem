from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']

class profileform(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username', 'date_joined','id']