from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Conta, Responsavel, TipoDespesa, Despesa, Parcelas


AdminSite.site_title = 'Minhas despesas'
AdminSite.site_header = 'Controle de despesas'
AdminSite.index_title = 'Controle de despesas'


class ParcelasIntoAdmin (admin.TabularInline):
    model = Parcelas
    extra = 1


class ParcelasAdmin(admin.ModelAdmin):
    list_display = ['despesa', 'valor', 'dataVencimento']
    list_filter = ['dataVencimento']


class DespesaAdmin (admin.ModelAdmin):
    inlines = [
        ParcelasIntoAdmin
    ]
    list_display = ['descricao', 'valor', 'dataCompra']
    list_filter = ['dataCompra']
    search_fields = ['descricao']

admin.site.register(Conta)
admin.site.register(Responsavel)
admin.site.register(TipoDespesa)
admin.site.register(Despesa, DespesaAdmin)
admin.site.register(Parcelas, ParcelasAdmin)
