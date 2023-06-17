from django import forms
class CreateNewList(forms.Form):
    name = forms.CharField(label="New List", max_length=200)
    check = forms.BooleanField()
