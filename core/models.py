from django.db import models
from stdimage.models import  StdImageField


class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Cargo(models.Model):
    cargo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

        def __str__(self):
            return self.cargo

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=255)
    biografia = models.TextField('Bio', max_length=1000)
    cargo = models.ForeignKey('core.Cargo', on_delete=models.SET_NULL, null=True )
    foto = StdImageField('Foto', upload_to='equipe',
                         variations= {'thumb': {'width': 600,
                                                'height': 600,
                                                'crop': True}})
    facebook = models.CharField('Face', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Insta', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'


    def __str__(self):
        return self.nome


class Servico(Base):
    imagem = StdImageField('Imagem', upload_to='servicos',
                           variations={'thumb': {'width': 1000,
                                                 'height': 667,
                                                 'crop': True}})
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=500)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome