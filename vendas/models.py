from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from clientes.models import Person
from produtos.models import Produto


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    impostos = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)

    # def get_total(self):
    #     tot = 0
    #     for produto in self.produtos.all():
    #         tot += produto.preco

    #    return tot - self.desconto + self.impostos

    def __str__(self):
        return self.numero


class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.venda.numero + ' - ' + self.produto.descricao

# @receiver(m2m_changed, sender=Venda.produtos.through)
def update_vendas_total(sender, instance, **kwargs):
    instance.total = instance.get_total()
    instance.save()
