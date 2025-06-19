import typer
import test  # test.py dosyan aynı klasörde olmalı



app = typer.Typer(help="Sorun çözüm ve yönetim CLI uygulaması")

@app.command()
def kullanici_olustur(
    adress: str = typer.Argument(..., help="Kullanıcının adres bilgisi (zorunlu)")
):
    """Yeni bir kullanıcı oluşturur"""
    test.kullanici_olustur(adress)

@app.command()
def yetkili_olustur(
    adress: str = typer.Argument(..., help="Yetkili kullanıcının adresi (zorunlu)")
):  
    """Yeni bir yetkili oluşturur"""
    test.Yetkili_olustur(adress)

def parse_guven_tabakasi(value) -> list[str]:
    if isinstance(value, list) and len(value) == 1:
        # Tek bir string liste içinde verilmiş: ['k1,k2,k3']
        return [v.strip() for v in value[0].split(",") if v.strip()]
    elif isinstance(value, str):
        # Direkt string olarak verilmişse
        return [v.strip() for v in value.split(",") if v.strip()]
    return value  # zaten düzgün listeyse


@app.command()
def alan_olustur(
    adress: str = typer.Argument(..., help="Alanın adresi (zorunlu)"),
    alan_adi: str = typer.Argument(..., help="Alan adı (zorunlu)"),
    guven_tabakasi: list[str] = typer.Option(
        ..., "--guven-tabakasi", "-g",
        help="Güvenlik katmanlarını virgülle ayırarak girin, örn: a,b,c (zorunlu)",
        callback=parse_guven_tabakasi

    )
):  
    """Yeni bir alan ve güvenlik katmanları oluşturur"""
    test.alan_olustur(Adress=adress, alan_adi=alan_adi, Guven_tabakasi=guven_tabakasi)

@app.command()
def sorun_olustur(
    adress: str = typer.Argument(..., help="Sorunu oluşturan kullanıcının adresi (zorunlu)"),
    icerik: str = typer.Argument(..., help="Sorun içeriği metni (zorunlu)"),
    alan: int = typer.Argument(..., help="Sorunun ait olduğu alan ID'si (zorunlu)")
):
    """Yeni bir sorun oluşturur"""
    test.sorun_olustur(Adress=adress, icerik=icerik, alan=alan)

@app.command()
def sorun_degerlendir(
    alan: int = typer.Argument(..., help="Alan ID'si (zorunlu)"),
    sorun: int = typer.Argument(..., help="Sorun ID'si (zorunlu)"),
    adress: str = typer.Argument(..., help="Değerlendiren kullanıcının adresi (zorunlu)"),
    tercih: int = typer.Option(..., "--tercih", "-t", help="Değerlendirme tercihi (zorunlu)")
):
    """Bir sorunu değerlendirir"""
    test.sorun_degerlendir(alan=alan, sorun=sorun, adress=adress, tercih=tercih)

@app.command()
def cozum_ekle(
    alan: int = typer.Argument(..., help="Alan ID'si (zorunlu)"),
    sorun: int = typer.Argument(..., help="Sorun ID'si (zorunlu)"),
    icerik: str = typer.Argument(..., help="Çözüm metni (zorunlu)"),
    adress: str = typer.Argument(..., help="Çözümü ekleyen kullanıcının adresi (zorunlu)")
):
    """Bir çözüme ekleme yapar"""
    test.cozum_ekle(alan=alan, sorun=sorun, icerik=icerik, adress=adress)

@app.command()
def cozum_onayi(
    alan: int = typer.Argument(..., help="Alan ID'si (zorunlu)"),
    sorun: int = typer.Argument(..., help="Sorun ID'si (zorunlu)"),
    cozum: int = typer.Argument(..., help="Çözüm ID'si (zorunlu)"),
    adress: str = typer.Argument(..., help="Onaylayan kullanıcının adresi (zorunlu)"),
    tercih: int = typer.Option(..., "--tercih", "-t", help="Onay pref verdiği değer (zorunlu)")
):
    """Bir çözümü onaylar veya reddeder"""
    test.cozum_onayi(alan=alan, sorun=sorun, cozum=cozum, adress=adress, tercih=tercih)

@app.command()
def cozum_degerlendir(
    alan: int = typer.Argument(..., help="Alan ID'si (zorunlu)"),
    sorun: int = typer.Argument(..., help="Sorun ID'si (zorunlu)"),
    cozum: int = typer.Argument(..., help="Çözüm ID'si (zorunlu)"),
    yildiz: int = typer.Option(..., "--yildiz", "-y", help="Değerlendirme yıldız sayısı (zorunlu)"),
    adress: str = typer.Argument(..., help="Değerlendiren kullanıcının adresi (zorunlu)")
):
    """Bir çözümü yıldızla değerlendirir"""
    test.cozum_degerlendir(alan=alan, sorun= sorun, cozum=cozum, yildiz=yildiz, adress=adress)
# typer_click_app = app
# click_repl.register_repl(typer_click_app)
# @app.command()
# def repl():
#     """
#     Etkileşimli Typer/Click REPL moduna geç.
#     Çıkmak için 'exit' yaz.
#     """
#     click_repl.repl(app)
@app.command()
def repl():
    """
    İnteraktif CLI: 'exit' veya Ctrl-D ile çıkın.
    """
    while True:
        try:
            line = input("cli> ").strip()
        except (EOFError, KeyboardInterrupt):
            typer.echo()  # yeni satır
            break

        if not line:
            continue
        if line.lower() in ("exit", "quit"):
            break

        args = line.split()
        try:
            # Typer uygulamasını aynı process içinde tekrar çağırıyoruz
            app(args=args, prog_name="arac")
        except SystemExit:
            # exit kodu 0/1 olayı, devam etmemiz için yutuyoruz
            pass


if __name__ == "__main__":
    app()


    
