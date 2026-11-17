# İptables Log Analyzer & HTML Reporter
 
Python ve Tkinter kullanılarak geliştirilmiş, `iptables` güvenlik duvarı loglarını analiz eden ve sonuçları düzenli bir HTML raporuna dönüştüren masaüstü uygulamasıdır.
 
## 🚀 Özellikler
 
* **Grafiksel Arayüz (GUI):** Tkinter tabanlı kolay kullanım.
* **Esnek Log Seçimi:** `filedialog` ile dilediğiniz log dosyasını seçebilme imkanı.
* **Detaylı Filtreleme:** IP adresine göre `Source` (Kaynak), `Destination` (Hedef) veya `Any` (Tümü) bazında arama yapabilme.
* **HTML Raporlama:** Elde edilen sonuçları şık ve düzenli bir HTML dosyası olarak dışa aktarabilme.
* **Güvenli Çıktı:** Özel karakterlerin (`&`, `<`, `>`) HTML güvenliğine uygun olarak escape edilmesi.
* **Hata Yönetimi:** Dosya okuma/yazma hatalarına karşı güvenli istisna (`try-except`) yönetimi.
## 🛠️ Kullanılan Teknolojiler
 
* **Python** (Core Logic & File Operations)
* **Tkinter** (Desktop User Interface)
* **OS / FileDialog** (System Operations)
## 📦 Kurulum ve Çalıştırma
 
1. Projeyi bilgisayarınıza klonlayın veya indirin:
```bash
git clone https://github.com/KULLANICI_ADINIZ/iptables-log-analyzer.git
```
 
2. Proje dizinine gidin:
```bash
cd iptables-log-analyzer
```
 
3. Uygulamayı çalıştırın:
```bash
python uygulama_b.py
```
 
## 📝 Kullanım
 
1. Uygulamayı başlattıktan sonra analiz etmek istediğiniz log dosyasını seçin.
2. Aranacak IP adresini ve filtreleme türünü (`Source`, `Destination` veya `Any`) belirtin.
3. Program, eşleşen kayıtları filtreleyerek log dosyasının bulunduğu dizinde bir HTML raporu (`ipTables_sonuclari.html`) oluşturacaktır.
## 🤝 Katkıda Bulunma
 
Katkı yapmak isterseniz lütfen bir `pull request` gönderin veya `issue` açın.
 
