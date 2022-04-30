from django.forms import ModelForm, inlineformset_factory
from .models import Abnormal, Reference


class AbnormalForm(ModelForm):
    class Meta:
        model = Abnormal
        fields = ['description', 'karyotype', 'broken_site', 'fragile_site', 'abnormal_type', 'chromosome', 'image']


class ReferenceForm(ModelForm):
    class Meta:
        model = Reference
        fields = ['pmid', 'title', 'abstract', 'pdf']



