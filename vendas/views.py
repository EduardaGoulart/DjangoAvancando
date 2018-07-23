from django.shortcuts import render
from django.views import View
from django.db.models import Max, Avg, Min, Count
from .models import Venda


class DashboardView(View):
    def get(self, request):

        media = Venda.objects.all().aggregate(Avg('valor'))['valor__avg']
        media_desconto = Venda.objects.all().aggregate(Avg('desconto'))['desconto__avg']
        min = Venda.objects.all().aggregate(Min('valor'))['valor__min']
        max = Venda.objects.all().aggregate(Max('valor'))['valor__max']
        n_ped = Venda.objects.all().aggregate(Count('valor'))['valor__count']

        context = {
            'media': media,
            'media_desconto': media_desconto,
            'min': min,
            'max': max,
            'n_ped': n_ped,
        }
        return render(request, 'vendas/dashboard.html', context)