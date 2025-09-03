import requests
from django.core.management.base import BaseCommand
from catalogo.models import Pais

class Command(BaseCommand):
    help = 'Sincroniza os países da API externa com o banco de dados'

    def handle(self, *args, **kwargs):
        url = 'https://restcountries.com/v3.1/all?fields=name,cca2,region,subregion,capital,population,flags' #API dos paises 
        self.stdout.write('Buscando países na API...')

        try:
            response = requests.get(url)
            response.raise_for_status()  # Lança erro se não for 200 OK
            countries_data = response.json()
        except requests.RequestException as e:
            self.stderr.write(f"Erro ao acessar API: {e}")
            return

        count = 0
        for country_data in countries_data:
            cca2 = country_data.get('cca2', '')
            nome = country_data.get('name', {}).get('common', '')
            populacao = country_data.get('population', 0)
            regiao = country_data.get('region', '')
            subregiao = country_data.get('subregion', '')

            capital_list = country_data.get('capital', [])
            capital = capital_list[0] if capital_list else ''

            flag_url = country_data.get('flags', {}).get('png', '')

            if not cca2 or not nome:
                continue  # Pula países sem código ou nome

            Pais.objects.update_or_create(
                cca2=cca2,
                defaults={
                    'nome': nome,
                    'populacao': populacao,
                    'regiao': regiao,
                    'subregiao': subregiao,
                    'capital': capital,
                    'flag_url': flag_url,
                }
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f'{count} países sincronizados com sucesso!'))
