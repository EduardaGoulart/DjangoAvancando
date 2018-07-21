from django.contrib import admin
from .models import Person, Documento, Venda, Produto
from .action import nfe_emitida, nfe_nao_emitida


class PersonAdmin(admin.ModelAdmin):

    # Exibindo valores de forma organizada
    fieldsets = (
        ("Dados pessoais", {'fields': ('first_name', 'last_name', 'doc')}),
        ("Dados complementares", {
            'classes': ('collapse',), # oculta os dados
            'fields': ('age', 'salary', 'bio', 'photo')
        })
    )
    # Campos exibidos no admin
    # fields = 'first_name', 'last_name', ('age', 'salary'), 'bio', 'photo', 'doc',)

    # Exibe todos os campos, exceto os que estão nesta lista
    # exclude = ['bio', ]

    # Exibe um grid com os campos selecionados. O primeiro field é o link
    list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'tem_foto', 'doc',)

    # Filtra em categorias os dados do banco
    list_filter = ('age', 'salary',)

    search_fields = ('id', 'first_name',)

    def tem_foto(self, obj):
        if obj.photo:
            return "Possui"
        return "Não Possui"

    tem_foto.short_description = 'Possui foto'


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('total',)
    list_filter = ('pessoa__doc', 'desconto')

    # Pega o ID da pessoa e permite buscar na lista de pessoas
    # raw_id_fields = ("pessoa",)

    autocomplete_fields = ('pessoa', 'produtos')
    list_display = ('id', 'pessoa', 'total', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]

    # Organiza a seleção dos valores
    # filter_horizontal = ['produtos']

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')
    search_fields = ('id', 'nome', 'preco')


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
