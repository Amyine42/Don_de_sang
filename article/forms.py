from django import forms
from django.core.exceptions import ValidationError

class SurveyForm(forms.Form):
    name = forms.CharField(max_length=30)
    fname = forms.CharField(max_length=30)
    age = forms.DateField()
    phone_number = forms.CharField(max_length=20)
    gender_choices = (
        ("male", 'Male'),
        ("female", 'Female'),
    )
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    blood_type_choices = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("autre", "?"),
    )
    blood_type = forms.ChoiceField(
        choices=blood_type_choices, widget=forms.RadioSelect)
    yes_no_choices = (
        ('oui', 'Oui'),
        ('non', 'Non'),
    )
    blood_donation = forms.ChoiceField(
        choices=yes_no_choices, widget=forms.RadioSelect)
    second_question = forms.ChoiceField(
        choices=yes_no_choices, widget=forms.RadioSelect)
    third_question = forms.ChoiceField(
        choices=yes_no_choices, widget=forms.RadioSelect)
    fourth_question = forms.ChoiceField(
        choices=yes_no_choices, widget=forms.RadioSelect)
    fifth_question = forms.ChoiceField(
        choices=yes_no_choices, widget=forms.RadioSelect)
    sixth_question = forms.ChoiceField(
        choices=yes_no_choices, widget=forms.RadioSelect)
    seventh_question = forms.ChoiceField(
        choices=yes_no_choices, widget=forms.RadioSelect)

    # add clean_<fieldname>() method to clean and validate form fields, for example :
    def clean_name(self):
         name = self.cleaned_data.get('name')
         if not name:
             raise forms.ValidationError("nom manquant")
         return name
    def clean_fname(self):
         fname = self.cleaned_data.get('fname')
         if not fname:
             raise forms.ValidationError("prenom manquant")
         return fname
    def clean_age(self):
         age = self.cleaned_data.get('age')
         if not age:
             raise forms.ValidationError("age manquant")
         return age
    def clean_phone(self):
         phone_number = self.cleaned_data.get('phone_number')
         if not phone_number:
             raise forms.ValidationError("telephone manquant")
         return phone_number
    def clean_gender(self):
         gender = self.cleaned_data.get('gender')
         if not gender:
             raise forms.ValidationError("specifier le sexe")
         return gender