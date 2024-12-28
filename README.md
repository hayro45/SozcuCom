# Sözcü Web Crawler

## Genel Bakış
Bu proje, sozcu.com'dan haber makalelerini kazımak için tasarlanmış bir web kazıyıcıdır. Haber makalelerine ait bağlantıları toplar, bu makalelerin içeriğini kazır ve verileri Elasticsearch'te indekslemek için hazırlar.

## Proje Yapısı
```
extensions/
    AdBlock.crx
README.md
requirements.txt
src/
    __init__.py
    elasticsearch_data.json
    link_scraper.py
    links.json
    main.py
    news_scraper.py
    news.json
    olusturucu.py
    yukleyici.py
tests/
    test_main.py
```

- `extensions/AdBlock.crx`: Kazıma sırasında reklamları engellemek için kullanılan Chrome uzantısı.
- `src/link_scraper.py`: Farklı haber kategorilerinden bağlantıları kazır.
- `src/news_scraper.py`: Toplanan bağlantılardan haber makalelerinin içeriğini kazır.
- `src/yukleyici.py`: Kazınan haber verilerini Elasticsearch için hazırlar.
- `src/olusturucu.py`: Hazırlanan haber verilerini Elasticsearch'e indeksler.
- `tests/test_main.py`: Proje için birim testleri içerir.

## Kurulum
Gerekli bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın:

```sh
pip install -r requirements.txt
```

## Kullanım
1. **Bağlantıları Kazıma**: Farklı haber kategorilerinden bağlantıları kazımak için:
    ```sh
    python src/link_scraper.py
    ```

2. **Haber İçeriğini Kazıma**: Toplanan bağlantılardan haber makalelerinin içeriğini kazımak için:
    ```sh
    python src/news_scraper.py
    ```

3. **Verileri Elasticsearch İçin Hazırlama**: Kazınan haber verilerini Elasticsearch için hazırlamak için:
    ```sh
    python src/yukleyici.py
    ```

4. **Verileri Elasticsearch'e İndeksleme**: Hazırlanan haber verilerini Elasticsearch'e indekslemek için:
    ```sh
    python src/olusturucu.py
    ```

## Testleri Çalıştırma
Uygulamanın beklendiği gibi davrandığından emin olmak için birim testlerini çalıştırabilirsiniz:

```sh
pytest tests/test_main.py
```

## Katkıda Bulunma
Bu projeye katkıda bulunmak isterseniz, lütfen depoyu fork edin ve bir pull request gönderin.

## Lisans
Bu proje [Your License] Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.