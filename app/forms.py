from django import forms
from .models import Vehicle, Brand

class VehicleListForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        exclude = [
            "id", 
            "photo",
        ]

class CreateVehicleForm(forms.ModelForm):

    model = forms.IntegerField(required=True,max_value=9999,min_value=1000,help_text='Year of car produced in 4 digit format. Like 1990 or 2012 etc...')

    def __init__(self, *args, **kwargs):
        super(CreateVehicleForm,self).__init__(*args, **kwargs)
    class Meta:
        model = Vehicle
        exclude = [
            "thumbnail",
        ]

class CreateBrandForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateBrandForm,self).__init__(*args, **kwargs)

    class Meta:
        model = Brand
        exclude = [
            "id",
        ]