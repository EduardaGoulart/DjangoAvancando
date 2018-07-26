from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Venda


class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Não possui permissão para acessar esta página')

        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        media = Venda.objects.media()
        media_desconto = Venda.objects.media_desconto()
        min = Venda.objects.min()
        max = Venda.objects.max()
        n_ped = Venda.objects.n_ped()
        nfe_emitida = Venda.objects.nfe_emitida()

        context = {
            'media': media,
            'media_desconto': media_desconto,
            'min': min,
            'max': max,
            'n_ped': n_ped,
            'nfe_emitida': nfe_emitida,
        }
        return render(request, 'vendas/dashboard.html', context)
