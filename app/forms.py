from django.forms import ModelForm
from app.models import Veiculo, Cliente

# Create the form class.
class VeiculoForm(ModelForm):
    class Meta:
       model = Veiculo
       fields = ['modelo', 'marca', 'ano', 'valor', 'cilindradas', 'cavalos']

class ClienteForm(ModelForm):
    class Meta:
       model = Cliente
       fields = ['Nome', 'Pai', 'Mae', 'CPF', 'RG', 'Nasc', 'Endereco']