# UBYS Not Kontrol Sistemi

Bu proje, Çanakkale Onsekiz Mart Üniversitesi (ÇOMÜ) öğrencilerinin UBYS sistemindeki notlarını otomatik olarak kontrol eden ve değişiklikleri bildiren bir sistemdir.

## Özellikler

- UBYS sistemine otomatik giriş yapma
- Not değişikliklerini kontrol etme
- Değişiklik durumunda Pushover üzerinden bildirim gönderme
- 5 dakikada bir otomatik kontrol
- 30 dakikada bir durum bildirimi

## Kurulum

1. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

2. `.env` dosyası oluşturun ve aşağıdaki bilgileri ekleyin:
```
ubys_tc_no=TC_KIMLIK_NO
ubys_password=UBYS_SIFRE
app_api_key=PUSHOVER_APP_API_KEY
user_secret_api_key=PUSHOVER_USER_SECRET
```

## Kullanım

Programı çalıştırmak için:
```bash
python main.py
```

## Gereksinimler

- Python 3.x
- Chrome tarayıcı
- Pushover hesabı ve API anahtarları
- UBYS hesap bilgileri

## Güvenlik

- Hassas bilgiler (TC kimlik no, şifre, API anahtarları) `.env` dosyasında saklanmaktadır
- `.env` dosyasını asla GitHub'a pushlamayın
- `.gitignore` dosyası `.env` dosyasını zaten hariç tutmaktadır

## Notlar

- Program çalışırken Chrome tarayıcısı arka planda çalışacaktır
- Her 5 dakikada bir not kontrolü yapılır
- Her 30 dakikada bir durum bildirimi gönderilir
- Not değişikliği tespit edildiğinde anında bildirim gönderilir