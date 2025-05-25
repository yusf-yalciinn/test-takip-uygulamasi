# Üniversite Sınavı Test Takip Uygulaması

## Proje Hakkında
2021 yılında henüz 17 yaşındayken üniversite sınavına hazırlandığım süreçte, çözdüğüm testlerin doğru, yanlış ve boş oranlarını tarihlere göre takip etmek, bu verileri grafiklere dökmek, grafik sonuçlarını kaydetmek ve aynı uygulama üzerinde birden fazla hesap oluşturma imkanı sunarak birden fazla öğrencinin kayıtlarını tek bir çatı altında toplayabilmek amacıyla bu projeyi geliştirdim.

Proje geliştirme sürecinde **Python**, **SQL** ve **CSS** dillerini kullandım. Ayrıca, projenin ikon ve logo tasarımlarını Adobe Illustrator ile kendim yaptım. Bazı buton ikonlarını ise internetten hazır olarak temin ettim.

---

## Proje Durumu

Proje içerisindeki bazı kaynak kod dosyalarında zamanla bozulmalar meydana gelmiştir. Bu sebeple, proje şu anda **main.py** dosyası üzerinden çalışması gerekirken çalışmamaktadır. 

Bozulan dosyaların işlevleri şu şekildedir:

- `databases/analysis_database/`  
  Bu klasördeki Python dosyaları, test işlemlerinin veritabanına kayıt edilmesi, silinmesi ve güncellenmesi ile ilgili kodları içermekteydi.

- `databases/account_database/`  
  - `login_account_processes.py`: Giriş yapma işlemleri için gerekli kodlar.  
  - `register_account.py`: Kayıt olma işlemleri için gerekli kodlar.

---

## Proje Dosya Yapısı

- `docs/drafts/Taslak.pdf`  
  Projeyi geliştirmeden önce fikri daha düzenli hale getirmek için hazırladığım taslak dosyası.

- `docs/flowcharts/`  
  Bu klasör, bazı veritabanı işlemleri için hazırladığım akış şemalarını (`.png` formatında) içerir.

- `docs/flowcharts/Database Diagram.pdf`  
  Projedeki tüm akış şemalarının toplandığı genel diyagram dosyası.

---

## Kurulum ve Kullanım

> **Not:** Kaynak kodlardaki bozulmalar nedeniyle, şu an için proje doğrudan koddan çalıştırılamamaktadır. Güncellemelerle ileride tam kod desteği sağlanacaktır.
 
1. Projeyi klonlayın veya indirin.

2. `main.py` dosyasını çalıştırmayı deneyebilirsiniz, ancak mevcut durumuyla bazı hatalar çıkabilir.

Bu proje şu anda kaynak kodları tam çalışır durumda değildir. Ancak, proje ile birlikte sağlanan **setup.exe** dosyası ile uygulamayı bilgisayarınıza kurabilir ve çalıştırabilirsiniz.

**Kurulum adımları:**

1. dist klasörü içerisindeki `setup.exe` dosyasını çalıştırarak programı bilgisayarınıza kurun.  
2. Kurulum tamamlandıktan sonra masaüstünde veya başlangıç menüsünde oluşan kısayol ile programı açabilirsiniz.  
3. Uygulama, birden fazla öğrenci hesabı oluşturup test sonuçlarını takip etmenize olanak sağlar.

---

## Teknolojiler

- Python  
- SQL (veritabanı yönetimi)  
- CSS (kullanıcı arayüzü için)  
- Adobe Illustrator (ikon ve logo tasarımı)

---

## Lisans

Bu proje kişisel amaçlıdır ve açık kaynak lisans altında değildir. Proje ile ilgili sorularınız için benimle iletişime geçebilirsiniz.

---

## İletişim

yusf.yalciinn@gmail.com

---

## Notlar

- Proje ikonları ve grafikler `ico`, `png` formatlarında sağlanmıştır.  
- Veritabanı dosyaları formatındaki konfigürasyonlar da projede yer almaktadır.  
- Bozulan dosyaların tamir edilmesi veya yeniden yazılması projeyi tekrar çalışır hale getirecektir.
