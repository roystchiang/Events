from django import forms

class newEventForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    map_lon = forms.FloatField()
    map_lat = forms.FloatField()
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)
    description = forms.Textarea()
    picture = forms.FileField()