from django import forms

from .models import Product, ProductImg

from tempus_dominus.widgets import DatePicker


class ProductForm(forms.ModelForm):
    product_id = forms.CharField(required=False)
    product_type = forms.CharField(required=False)
    brand = forms.CharField(required=False)
    description = forms.CharField(required=False)
    sale_price = forms.FloatField(required=False)
    purchase_price = forms.FloatField(required=False)
    last_purchase = forms.DateField(
        required=False,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            }),
    )
    quantity = forms.IntegerField(required=False)
    obs = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Product
        fields = [
            'product_id',
            'product_type',
            'brand',
            'description',
            'sale_price',
            'purchase_price',
            'last_purchase',
            'quantity',
            'obs',
            'image',
        ]

class ProductImgForm(forms.ModelForm):
    class Meta:
        model = ProductImg
        fields = ['image', ]
