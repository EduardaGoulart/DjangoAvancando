from django.shortcuts import render
from django.views import View
from .models import Venda


class DashboardView(View):
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
