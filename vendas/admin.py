from django.contrib import admin
from .action import nfe_emitida, nfe_nao_emitida
from .models import Venda, ItensDoPedido


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('total',)
    list_filter = ('pessoa__doc', 'desconto')

    # Pega o ID da pessoa e permite buscar na lista de pessoas
    # raw_id_fields = ("pessoa",)

    autocomplete_fields = ('pessoa',)
    list_display = ('id', 'pessoa', 'total', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]

    # Organiza a seleção dos valores
    # filter_horizontal = ['produtos']

    # def total(self, obj):
    #    return obj.get_total()

    # total.short_description = 'Total'


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItensDoPedido)
