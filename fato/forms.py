from django import forms
from .models import Fato, Vitima, Autor, Testemunha


class FatoForm(forms.ModelForm):
    class Meta:
        model = Fato
        fields=['relato', 'logradouro', 'bairro', 'local_especifico', 'data', 'turno', 'vitima', 'autor', 'testemunha']

        widgets = {
            'relato': forms.Textarea(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'local_especifico': forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control'}),
            'turno': forms.Select(attrs={'class': 'form-control'}),
            'vitima': forms.Select(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'testemunha': forms.Select(attrs={'class': 'form-control'}),

        }

class VitimaForm(forms.ModelForm):
    class Meta:
        model = Vitima
        fields=['nome', 'cpf', 'rg', 'nascimento', 'sexo', 'naturalidade', 'cor_pele', 'fone', 'residencia', 'bairro']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'naturalidade': forms.Select(attrs={'class': 'form-control'}),
            'cor_pele': forms.Select(attrs={'class': 'form-control'}),
            'fone': forms.TextInput(attrs={'class': 'form-control'}),
            'residencia': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),

        }

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields=['nome', 'cpf', 'rg', 'sexo', 'cor_pele', 'bairro', 'idade_aparente']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'cor_pele': forms.Select(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'idade_aparente': forms.TextInput(attrs={'class': 'form-control'}),
        }



class TestemunhaForm(forms.ModelForm):
    class Meta:
        model = Testemunha
        fields=['nome', 'cpf', 'rg', 'nascimento', 'sexo', 'naturalidade', 'cor_pele', 'fone', 'residencia', 'bairro']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'naturalidade': forms.Select(attrs={'class': 'form-control'}),
            'cor_pele': forms.Select(attrs={'class': 'form-control'}),
            'fone': forms.TextInput(attrs={'class': 'form-control'}),
            'residencia': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
        }