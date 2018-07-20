from django.contrib import admin
from .models import Person, Documento, Venda, Produto


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

    def tem_foto(self, obj):
        if obj.photo:
            return "Possui"
        return "Não Possui"

    tem_foto.short_description = 'Possui foto'


class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc', 'desconto')
    raw_id_fields = ("pessoa",)
    list_display = ('id', 'pessoa', 'total')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
