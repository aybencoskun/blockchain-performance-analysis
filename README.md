
# Kripto Bot Performans Analizi

## Proje Özeti

Bu proje, bir blockchain botunun işlem alım kararlarında kullandığı `diff` (fiyat farkı) ve `seconds` (geçmiş süre) parametrelerine göre başarı (`result = 1`) oranlarını analiz etmek ve görselleştirmek amacıyla geliştirilmiştir.

Amaç, belirli koşullarda botun başarılı işlem yapma olasılığını hesaplamak ve bu başarıyı görsel olarak ifade edebilecek bir sistem hazırlamaktır.

## Girdi Verisi

Veri, bir Python botu tarafından düzenli olarak toplanmakta olup her bir kayıt şu üç parametreyi içerir:

- `diff` (float): Şu anki coin fiyatı ile `seconds` saniye önceki fiyat arasındaki fark.
- `seconds` (int): Geriye doğru bakılan saniye.
- `result` (0 veya 1): Bot bu koşulda kâr ettiyse 1, zarar ettiyse 0.

Veri JSON formatındadır: `round_finality_data.json`

## Analiz Adımları

Script aşağıdaki işlemleri yapar:

1. Veri Yükleme
2. Veri Gruplama (Binning): `diff` → 0.1 adımlarla, `seconds` → her saniye
3. Pivot Tablonun Oluşturulması
4. Heatmap ile Görselleştirme
5. Histogram
6. Sonuçların `output/` klasörüne aktarılması

## Dosya Yapısı

```
proje-klasörü/
├── analyze.py
├── round_finality_data.json
├── README.md
└── output/
    ├── heatmap_success_rate.png
    ├── diff_distribution.png
    └── summary_table.csv
```

## Kullanım

### Gereksinimler

- Python 3.8+
- Gerekli kütüphaneler:
  - pandas
  - matplotlib
  - seaborn
  - numpy

Kurulum:

```
pip install pandas matplotlib seaborn numpy
```

### Çalıştırma

```
python analyze.py
```

Çalıştırıldığında `output/` klasörü oluşur ve analiz sonuçları buraya kaydedilir.

## Esneklik ve Tekrar Kullanım

Script tekrar tekrar çalıştırılabilir. Yeni veriler geldiğinde yalnızca `round_finality_data.json` dosyası güncellenmeli ve script yeniden çalıştırılmalıdır.

## Genişletme Önerileri

- Zaman bazlı analiz (gün/saat)
- Regresyon modelleme
- Otomatik rapor üretimi
