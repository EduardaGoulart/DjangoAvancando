from django.shortcuts import render
from django.views import View
from django.db.models import Sum, F, FloatField, Max, Avg
from .models import Venda


class DashboardView(View):
    def get(self, request):
        media = Venda.objects.all().aggregate(Avg('valor'))['valor__avg']
        context = {
            'media': media,
        }
        return render(request, 'vendas/dashboard.html', context)