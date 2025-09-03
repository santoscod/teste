from django.db import models

class Pais(models.Model):
    nome = models.CharField(max_length=100)
    cca2 = models.CharField(max_length=2, unique=True, help_text="Código de 2 letras do país")
    regiao = models.CharField(max_length=100, blank=True, null=True)
    subregiao = models.CharField(max_length=100, blank=True, null=True)
    capital = models.CharField(max_length=100, blank=True, null=True)
    populacao = models.PositiveIntegerField()
    flag_url = models.URLField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ['nome']

class Itinerary(models.Model):
    titulo = models.CharField(max_length=200, help_text="Título do Roteiro")
    country = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name="itineraries")
    data_inicio = models.DateField(help_text="Data de início da viagem")
    data_partida = models.DateField(help_text="Data de partida da viagem")
    descricao = models.TextField(help_text="Descrição detalhada do roteiro")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Preço do roteiro (opcional)")
    image = models.ImageField(upload_to='itinerary_images/', blank=True, null=True, help_text="Imagem de destaque do roteiro")

    def __str__(self):
        return f"{self.titulo} - {self.country.nome}"

    class Meta:
        verbose_name = "Roteiro"
        verbose_name_plural = "Roteiros"
        ordering = ['data_inicio']

#meu terminal na Migrations for 'catalogo':
'''catalogo/migrations/0003_auto_20250903_0506.py
    - Change Meta options on itinerary
    - Change Meta options on pais
    - Rename field start_date on itinerary to data_inicio
    - Rename field departure_date on itinerary to data_partida
    - Rename field description on itinerary to descricao
    - Rename field title on itinerary to titulo
    - Rename field name on pais to nome
    - Rename field population on pais to populacao
    - Rename field region on pais to regiao
    - Rename field subregion on pais to subregiao'''
