from django.forms import ModelForm
from .models import Contratos

class ContratosForm(ModelForm):
  class Meta:
    model = Contratos
    fields = '__all__'