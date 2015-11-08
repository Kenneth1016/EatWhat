from django import forms

class CreateOrderMainForm(forms.Form):
    orderDate = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'orderDate'}))
    restaurant = forms.CharField(max_length=10, widget=forms.HiddenInput())
    memo = forms.CharField(max_length=200, required=False, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                        'rows': '3'}))
    orderDueDate = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'orderDueDate'}))