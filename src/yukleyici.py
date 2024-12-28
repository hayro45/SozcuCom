import json
from datetime import datetime

def prepare_elasticsearch_data(news_data):
    """Json haber verisini Elasticsearch formatına hazırlar."""
    all_news = []   
    for category, articles in news_data.items():
        for article in articles:
            # created_date'i ISO 8601 formatına dönüştür
            created_date_str = article.get("created_date")  # "created_date" anahtarını kontrol et
            
            if created_date_str:
                created_date_obj = datetime.fromisoformat(created_date_str.replace("+03:00", ""))
                article["created_date"] = created_date_obj.isoformat()
            article["kategori"] = category
            all_news.append(article)
    return all_news


# news.json dosyasını oku
with open('news.json', 'r', encoding='utf-8') as f:
    news_json = json.load(f)

# Elasticsearch verisi olarak hazırla
elasticsearch_data = prepare_elasticsearch_data(news_json)

# elasticsearch_data.json dosyasına yaz
with open('elasticsearch_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(elasticsearch_data, outfile, indent=4, ensure_ascii=False)


print(elasticsearch_data)
print("elasticsearch_data.json dosyası başarıyla oluşturuldu.")

