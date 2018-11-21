from django.db import models


class Conta(models.Model):
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    def __str__(self):
        return '{}'.format(self.descricao)

class Responsavel(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome")

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        verbose_name_plural = "Responsáveis"


class TipoDespesa(models.Model):
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    def __str__(self):
        return '{}'.format(self.descricao)

    class Meta:
        verbose_name_plural = "Tipo de Despesas"


class Despesa(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, verbose_name="Conta Vinculada")
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE, verbose_name="Responsável")
    tipoDespesa = models.ForeignKey(TipoDespesa, on_delete=models.CASCADE, verbose_name="Tipo de Despesa")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Compra")
    dataCompra = models.DateField(auto_now=True, verbose_name="Data da Compra")

    def __str__(self):
        return '{} ({}) - {}'.format(self.descricao, self.conta, self.responsavel)


class Parcelas(models.Model):
    despesa = models.ForeignKey(Despesa, on_delete=models.CASCADE, verbose_name="Despesa")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    dataVencimento = models.DateField(verbose_name="Data de Vencimento")
    pagamento = models.BooleanField(default=False, verbose_name="Pago?")

    class Meta:
        verbose_name = "Parcelas"
        verbose_name_plural = "Parcelas"