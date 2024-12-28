from elasticsearch import Elasticsearch
import json

# Elasticsearch bağlantısı
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# Veriyi Elasticsearch'e aktar
with open('elasticsearch_data.json', 'r', encoding='utf-8') as f:
    elasticsearch_data = json.load(f)

# Veriyi Elasticsearch'e aktar
for i, doc in enumerate(elasticsearch_data):
    es.index(index='haberler', document=doc, id=i + 1)
    print(f"Document {i + 1} indexed.")

print("Veri Elasticsearch'e başarıyla aktarıldı.")