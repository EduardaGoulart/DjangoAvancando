from django.contrib import admin
from .models import Person, Documento, Venda, Produto


class PersonAdmin(admin.ModelAdmin):
    # Campos exibidos no admin
    # fields = ('first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc',)
    # Exibe todos os campos, exceto os que estão nesta lista
    exclude = ['bio', ]
    # Exibe um grid com os campos selecionados. O primeiro field é o link
    list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)
