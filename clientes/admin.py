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
    # list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc',)

    # Filtra em categorias os dados do banco
    list_filter = ('age', 'salary',)


class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc', 'desconto')


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto)
