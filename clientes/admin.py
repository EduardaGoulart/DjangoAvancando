from django.contrib import admin
from .models import Person, Documento


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




# class ProdutoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'descricao', 'preco')
#     search_fields = ('id', 'nome', 'preco')


class DocumentosAdmin(admin.ModelAdmin):
    search_fields = ('num_doc',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentosAdmin)
# admin.site.register(Produto, ProdutoAdmin)
