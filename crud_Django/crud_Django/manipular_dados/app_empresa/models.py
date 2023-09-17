from django.db import models

class App_empresa(models.Model):  
    nome_produto = models.CharField(max_length=30)  
    quantidade = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s " %(self.nome_produto) 
    class Meta:  
        db_table = "app_empresa"  