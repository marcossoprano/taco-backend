
import pandas as pd
from django.core.management.base import BaseCommand
from alimentos.models import Alimento

class Command(BaseCommand):
    help = 'Importa alimentos da tabela TACO a partir do arquivo taco-db-nutrientes.csv'

    def handle(self, *args, **kwargs):
        arquivo_csv = 'taco-db-nutrientes.csv'
        colunas = ['Nome', 'Energia (kcal)', 'Proteína (g)', 'Lipídeos (g)', 'Carboidrato (g)']
        df = pd.read_csv(arquivo_csv, on_bad_lines='skip')
        import unicodedata
        def normalize(col):
            return unicodedata.normalize('NFKD', col).encode('ASCII', 'ignore').decode().replace(' ', '').lower()
        cols_map = {normalize(c): c for c in df.columns}
        nome_col = df.columns[1]
        energia_col = None
        proteina_col = None
        carbo_col = None
        gordura_col = None
        for key in cols_map:
            if 'energia(kcal)' in key:
                energia_col = cols_map[key]
            if 'proteina(g)' in key:
                proteina_col = cols_map[key]
            if 'carboidrato(g)' in key:
                carbo_col = cols_map[key]
            if 'lipideos(g)' in key:
                gordura_col = cols_map[key]
        count = 0
        def parse_float(val):
            if pd.isna(val):
                return 0.0
            try:
                return float(val)
            except (ValueError, TypeError):
                if str(val).strip() in ['Tr', '-', '']:
                    return 0.0
                return 0.0
        for _, row in df.iterrows():
            nome = str(row[nome_col]).strip()
            calorias = parse_float(row[energia_col]) if energia_col else 0.0
            proteinas = parse_float(row[proteina_col]) if proteina_col else 0.0
            carboidratos = parse_float(row[carbo_col]) if carbo_col else 0.0
            gorduras = parse_float(row[gordura_col]) if gordura_col else 0.0
            Alimento.objects.update_or_create(
                nome=nome,
                defaults={
                    'calorias': calorias,
                    'proteinas': proteinas,
                    'carboidratos': carboidratos,
                    'gorduras': gorduras
                }
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f'Importação concluída! {count} alimentos importados.'))
