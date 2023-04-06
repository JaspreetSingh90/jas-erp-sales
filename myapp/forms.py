from django import forms

class customer_form(forms.Form):
    name = forms.CharField(widget = forms.TextInput)
    email = forms.CharField(widget = forms.TextInput)
    phone = forms.CharField(widget = forms.TextInput)
    address = forms.CharField(widget = forms.Textarea)


class order_form(forms.Form):
    customer = forms.IntegerField(widget = forms.TextInput)
    items = forms.CharField(widget = forms.Textarea)
    totalamount = forms.CharField(widget = forms.TextInput)
    orderdate = forms.DateField(widget = forms.DateInput)


