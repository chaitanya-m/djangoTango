from django import forms
from inputform.models import UserName, UserEmail

class UserNameForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter your name.")
	email = forms.CharField(max_length=128, help_text="Please enter your email.")
	picfile = forms.FileField(
        label='Select a file',
        help_text='max. 10 megabytes'
    )
	class Meta:
		model = UserName

class UserEmailForm(forms.ModelForm):
	email = forms.CharField(max_length=128, help_text="Please enter your email.")

	class Meta:
		model = UserEmail
		fields = ('email',)
