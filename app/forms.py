from django import forms
from django.core import validators

def validate_name(value):
    if not value[0].isupper():
        raise forms.ValidationError('Name should start with Capital Letter')

def validate_length(value):
    if len(value)<5:
        raise forms.ValidationError('Length Is Too Short')

def validate_age(value):
    if value<18:
        raise forms.ValidationError('Age Should Be Greater Than 18')

class Student_Form(forms.Form):
    name = forms.CharField(max_length=20, validators=[validate_name,validate_length])
    age = forms.IntegerField(validators=[validate_age])
    email = forms.EmailField()
    conform_email = forms.EmailField()

    phone = forms.CharField(max_length=10, min_length=10, validators = [validators.RegexValidator('[6-9]\d{9}')])

    bot_cleaner = forms.CharField(max_length=50, widget=forms.HiddenInput, required=False)




    ##  clean() is used for validating multiple column
    def clean(self):
        email = self.cleaned_data['email']
        conform_email = self.cleaned_data['conform_email']
        if email != conform_email:
            raise forms.ValidationError("Email Mis-matching")

    def clean_bot_cleaner(self):
        bot_cleaner = self.cleaned_data['bot_cleaner']
        if len(bot_cleaner)>0:
            raise forms.ValidationError("Bot Detected")

