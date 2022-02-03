from django.views.generic import TemplateView, DetailView
from .models import Funcionario, Servico


class IndexView(TemplateView):
    template_name = 'index.html'

    #sobreescrevendo o  método de obtenção do contexto
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['servicos'] = Servico.objects.order_by('?').all()
        return context


class DetalharServicoView(DetailView):
    template_name = 'detalhe_servico.html'
    model = Servico