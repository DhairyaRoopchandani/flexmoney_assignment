from django import forms

gender_choice=[('M', 'Male'),
                      ('F', 'Female'),
]
batch=[
        ('M1' , '6-7 AM'),
        ('M2' , '7-8 AM'),
        ('M3' , '8-9 AM'),
        ('N1' , '5-6 PM')
]


class member(forms.Form):
    
    name=forms.CharField(widget=forms.Textarea(attrs={'rows':1}))
    email=forms.EmailField()
    phone_no=forms.CharField(widget=forms.Textarea(attrs={'rows':1}))
    gender =forms.ChoiceField(choices=gender_choice)
    schedule_preference=forms.ChoiceField(choices=batch)
    age=forms.IntegerField(min_value=18,max_value=65)
    date=forms.DateField()

class Sform(forms.Form):
    name=forms.CharField(widget=forms.Textarea(attrs={'rows':1}))
    

class Payment(forms.Form):
    name=forms.CharField(widget=forms.Textarea(attrs={'rows':1}))
    upi_id=forms.CharField(widget=forms.Textarea(attrs={'rows':1}))
    amount=forms.IntegerField()
    date=forms.DateField()





