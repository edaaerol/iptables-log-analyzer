import os
from tkinter import Tk, StringVar, ttk, filedialog, simpledialog, messagebox


def satirda_ip_var_mi(satir, ip_adresi, arama_alani):
    kelimeler = satir.split()

    for kelime in kelimeler:
        if arama_alani == "Source" and kelime == "SRC=" + ip_adresi:
            return True
        elif arama_alani == "Destination" and kelime == "DST=" + ip_adresi:
            return True
        elif arama_alani == "Any":
            if kelime == "SRC=" + ip_adresi or kelime == "DST=" + ip_adresi:
                return True

    return False


def eslesen_satirlari_bul(dosya_adi, ip_adresi, arama_alani):
    eslesen_satirlar = []

    with open(dosya_adi, "r", encoding="utf-8", errors="replace") as dosya:
        satirlar = dosya.readlines()

    for satir in satirlar:
        if satirda_ip_var_mi(satir, ip_adresi, arama_alani):
            eslesen_satirlar.append(satir)

    return eslesen_satirlar


def sonuclari_dosyaya_yaz(dosya_adi, eslesen_satirlar, ip_adresi):
    ip_html = ip_adresi.replace("&", "&amp;")
    ip_html = ip_html.replace("<", "&lt;")
    ip_html = ip_html.replace(">", "&gt;")

    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        dosya.write("<!DOCTYPE html>\n")
        dosya.write("<html lang=\"tr\">\n")
        dosya.write("<head>\n")
        dosya.write("<meta charset=\"UTF-8\">\n")
        dosya.write("<title>IP Arama Sonuclari</title>\n")
        dosya.write("</head>\n")
        dosya.write("<body>\n")
        dosya.write("<pre>\n")

        for satir in eslesen_satirlar:
            html_satir = satir.replace("&", "&amp;")
            html_satir = html_satir.replace("<", "&lt;")
            html_satir = html_satir.replace(">", "&gt;")
            html_satir = html_satir.replace(
                ip_html,
                "<span style=\"background-color: yellow; color: red;\">"
                + ip_html
                + "</span>",
            )
            dosya.write(html_satir)

        dosya.write("</pre>\n")
        dosya.write("</body>\n")
        dosya.write("</html>\n")


def arama_yap(pencere, arama_alani):
    dosya_adi = filedialog.askopenfilename(
        parent=pencere,
        title="ipTables.log dosyasini secin",
        filetypes=[("Log dosyalari", "*.log"), ("Tum dosyalar", "*.*")],
    )

    if not dosya_adi:
        return

    ip_adresi = simpledialog.askstring(
        "IP Adresi",
        "Aranacak IP adresini girin:",
        parent=pencere,
    )

    if ip_adresi is None:
        return

    if ip_adresi == "":
        messagebox.showerror("Hata", "IP adresi bos olamaz.", parent=pencere)
        return

    try:
        eslesen_satirlar = eslesen_satirlari_bul(
            dosya_adi,
            ip_adresi,
            arama_alani.get(),
        )
    except OSError as hata:
        messagebox.showerror("Dosya Hatasi", str(hata), parent=pencere)
        return

    sonuc_dosyasi = os.path.join(
        os.path.dirname(dosya_adi),
        "ipTables_sonuclari.html",
    )

    try:
        sonuclari_dosyaya_yaz(sonuc_dosyasi, eslesen_satirlar, ip_adresi)
    except OSError as hata:
        messagebox.showerror("Dosya Hatasi", str(hata), parent=pencere)
        return

    messagebox.showinfo(
        "Tamamlandi",
        "Bulunan satir sayisi: "
        + str(len(eslesen_satirlar))
        + "\nHTML dosyasi olusturuldu:\n"
        + sonuc_dosyasi,
        parent=pencere,
    )


def uygulamayi_baslat():
    pencere = Tk()
    pencere.title("Uygulama B")
    pencere.geometry("400x200")
    pencere.resizable(False, False)

    ttk.Label(
        pencere,
        text="IP arama alani",
        font=("Arial", 14),
    ).pack(pady=(25, 10))

    arama_alani = StringVar(value="Any")
    ttk.Combobox(
        pencere,
        textvariable=arama_alani,
        values=["Source", "Destination", "Any"],
        state="readonly",
        width=20,
    ).pack()

    ttk.Button(
        pencere,
        text="Dosya Sec ve Ara",
        command=lambda: arama_yap(pencere, arama_alani),
    ).pack(pady=20)

    pencere.mainloop()


if __name__ == "__main__":
    uygulamayi_baslat()
