from django.forms import ModelForm
from .models import Abnormal


class AbnormalForm(ModelForm):
    class Meta:
        model = Abnormal
        fields = ['description', 'karyotype', 'broken_site', 'fragile_site', 'abnormal_type', 'chromosome', 'image']
