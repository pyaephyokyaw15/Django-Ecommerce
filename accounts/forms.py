from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from image_uploader_widget.widgets import ImageUploaderWidget
from .models import Account

class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name')


class ProfileForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'profile_picture')

        widgets = {
            'profile_picture': ImageUploaderWidget(),
        }