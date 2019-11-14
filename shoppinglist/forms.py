from django import forms

class ItemBuy(forms.Form):
    status = (
            (0, '未購入'),
            (1, '購入済')
            )
    item_id = forms.IntegerField(label='ID')
    item_status = forms.ChoiceField(label='STATUS',widget=forms.Select, choices=status)