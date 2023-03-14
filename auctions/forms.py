from django.forms import ModelForm
from .models import Product


class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['owner', 'vote', 'target_date']


    def __init__(self, *args, **kwargs):
        super(ProductForms, self).__init__(*args, **kwargs)

        # for key, value in self.fields.items():
        #     value.widget.attrs.update({'class': 'input'})

        self.fields['title'].widget.attrs.update({'class': 'input'})
