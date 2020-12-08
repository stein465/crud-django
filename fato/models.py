from django.db import models


# Create your models here.te
class Testemunha(models.Model):
    SEXO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Não Binario', 'Não Binario')
    )
    NATURALIDADE_CHOICES = (
        ('Brasileiro', 'Brasileiro'),
        ('Estrangeiro', 'Estrangeiro'),
    )

    COR_PELE_CHOICES = (
        ('Preta', 'Preta'),
        ('Parda', 'Parda'),
        ('Branca', 'Branca')
    )

    nome = models.CharField(max_length= 100)
    cpf = models.IntegerField(max_length=50)
    rg = models.IntegerField(max_length=50)
    nascimento = models.DateField(max_length=50)
    sexo = models.CharField(max_length=100, choices= SEXO_CHOICES)
    naturalidade = models.CharField(max_length=100, choices=NATURALIDADE_CHOICES,)
    cor_pele = models.CharField(max_length=100, choices=COR_PELE_CHOICES)
    fone = models.IntegerField(max_length=50)
    residencia = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Vitima(models.Model):
    SEXO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Não Binario', 'Não Binario')
    )
    NATURALIDADE_CHOICES = (
        ('Brasileiro', 'Brasileiro'),
        ('Estrangeiro', 'Estrangeiro'),
    )

    COR_PELE_CHOICES = (
        ('Preta', 'Preta'),
        ('Parda', 'Parda'),
        ('Branca', 'Branca')
    )

    nome = models.CharField(max_length= 100)
    cpf = models.IntegerField(max_length=50)
    rg = models.IntegerField(max_length=50)
    nascimento = models.DateField(max_length=50)
    sexo = models.CharField(max_length=100, choices= SEXO_CHOICES)
    naturalidade = models.CharField(max_length=100, choices=NATURALIDADE_CHOICES,)
    cor_pele = models.CharField(max_length=100, choices=COR_PELE_CHOICES)
    fone = models.IntegerField(max_length=50)
    residencia = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    SEXO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Não Binario', 'Não Binario')
    )

    COR_PELE_CHOICES = (
        ('Preta', 'Preta'),
        ('Parda', 'Parda'),
        ('Branca', 'Branca')
    )

    nome = models.CharField(max_length= 100)
    cpf = models.IntegerField(blank = True, null = True)
    rg = models.IntegerField(blank = True, null = True)
    sexo = models.CharField(max_length=100, choices= SEXO_CHOICES)
    cor_pele = models.CharField(max_length=100, choices=COR_PELE_CHOICES)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    idade_aparente = models.CharField (max_length=100)

    def __str__(self):
        return self.nome


class Fato(models.Model):
    SEXO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Não Binario', 'Não Binario')
    )

    TURNO_CHOICES = (
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
        ('Noite', 'Noite'),
    )

    relato = models.CharField(max_length=400)
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    local_especifico = models.CharField(max_length=100)
    data = models.DateField(max_length=50)
    turno = models.CharField(max_length=100, choices=TURNO_CHOICES)
    vitima = models.OneToOneField(Vitima, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    testemunha = models.ForeignKey(Testemunha,on_delete= models.CASCADE)
    def __str__(self):
            return self.relato.__str__()