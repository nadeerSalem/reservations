from django import forms

class CreateReservation(forms.Form):

    date = forms.DateField()
    cena = forms.BooleanField(required=False)
    pranzo = forms.BooleanField(required=False)
    adults = forms.IntegerField(required=True)
    children = forms.IntegerField(required=False)
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    note = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pranzo'].initial = True

        