import json, os
from playwright.sync_api import sync_playwright

OUT = "/home/claude/ig/hafta"
os.makedirs(OUT, exist_ok=True)

BASE = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Poppins,sans-serif;position:relative;overflow:hidden}
.brand,.bt{font-family:Lora,serif;letter-spacing:10px;font-size:28px;color:#e9cf96}
</style>%s</head><body>%s</body></html>"""

FOOT_LIGHT = '<div class="foot"><div class="ph">☎ 0545 151 71 79 &nbsp;·&nbsp; larisabeautyclub.com</div>Yalı Mah. 6523 Sk. No:32/B K:2 D:201 (Park Yaşam Ofis) Karşıyaka / İzmir</div>'
FOOT_DARK = '<div class="foot"><div class="ph">☎ 0545 151 71 79</div>Yalı Mah. 6523 Sk. No:32/B K:2 D:201<br>Park Yaşam Ofis · Karşıyaka / İzmir</div>'


def list_post(title_html, items):
    css = """<style>
body{width:1080px;height:1350px;background:#f7f2ea;color:#0b4644}
.top{position:absolute;left:0;right:0;top:0;height:470px;background:radial-gradient(circle at 25% 20%,#1f8f8a,#0b4f4c 70%);color:#fff;text-align:center;padding-top:80px}
h1{font-family:Lora,serif;font-size:80px;line-height:1.08;margin-top:36px}
h1 i{color:#e9cf96}
.list{position:absolute;left:80px;right:80px;top:400px;display:flex;flex-direction:column;gap:18px}
.it{background:#fff;border-radius:24px;padding:24px 36px;display:flex;gap:30px;align-items:center;box-shadow:0 10px 30px rgba(11,70,68,.10);border-left:6px solid #d4af6a}
.n{flex:none;width:76px;height:76px;border-radius:50%;background:linear-gradient(135deg,#f1d9a4,#c99a4a);color:#0b4644;font-family:Lora,serif;font-weight:700;font-size:40px;display:flex;align-items:center;justify-content:center}
.t b{display:block;font-size:31px;font-weight:600}
.t span{font-size:23px;color:#4f6e6c}
.foot{position:absolute;bottom:40px;left:60px;right:60px;text-align:center;font-size:21px;color:#4f6e6c;line-height:1.5}
.foot .ph{font-size:28px;color:#0b4644;font-weight:600}
</style>"""
    its = "".join(f'<div class="it"><div class="n">{i+1}</div><div class="t"><b>{a}</b><span>{b}</span></div></div>' for i, (a, b) in enumerate(items))
    body = f'<div class="top"><div class="brand">LARISA BEAUTY</div><h1>{title_html}</h1></div><div class="list">{its}</div>{FOOT_LIGHT}'
    return BASE % (css, body), (1080, 1350)


def grid_post(title_html, sub, cards, cta):
    css = """<style>
body{width:1080px;height:1350px;background:radial-gradient(circle at 20% 15%,#1f8f8a 0%,#0e5f5c 45%,#083d3b 100%);color:#fff;text-align:center}
.wrap{position:absolute;inset:60px;border:2px solid #d4af6a;border-radius:28px;padding:56px 50px}
h1{font-family:Lora,serif;font-size:76px;line-height:1.08;margin-top:30px}
h1 i{color:#e9cf96}
.sub{font-size:27px;color:#d6eeeb;margin-top:16px;font-weight:300}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:44px;text-align:left}
.c{background:rgba(255,255,255,.08);border:1px solid rgba(233,207,150,.45);border-radius:22px;padding:26px 28px}
.c b{display:block;font-family:Lora,serif;font-size:36px;color:#e9cf96}
.c span{font-size:22px;color:#e3f2f0;line-height:1.45;display:block;margin-top:8px}
.cta{margin-top:36px;display:inline-block;background:linear-gradient(135deg,#f1d9a4,#c99a4a);color:#0b4644;border-radius:50px;padding:16px 36px;font-size:26px;font-weight:600}
.foot{position:absolute;bottom:34px;left:40px;right:40px;font-size:20px;color:#bfe3df;line-height:1.5}
.foot .ph{font-size:27px;color:#fff;font-weight:600}
</style>"""
    cs = "".join(f'<div class="c"><b>{a}</b><span>{b}</span></div>' for a, b in cards)
    body = f'<div class="wrap"><div class="brand">LARISA BEAUTY</div><h1>{title_html}</h1><div class="sub">{sub}</div><div class="grid">{cs}</div><div class="cta">{cta}</div>{FOOT_LIGHT}</div>'
    return BASE % (css, body), (1080, 1350)


def story_text(kicker, title_html, text, pill, icon="✨"):
    css = """<style>
body{width:1080px;height:1920px;background:radial-gradient(circle at 30% 25%,#1f8f8a,#0b4f4c 55%,#062f2d);color:#fff;text-align:center}
.brand{position:absolute;top:200px;left:0;right:0}
.kick{position:absolute;top:330px;left:0;right:0}
.kick span{display:inline-block;border:2px solid #d4af6a;color:#e9cf96;border-radius:50px;padding:12px 34px;font-size:30px;letter-spacing:3px;font-weight:600}
.icon{position:absolute;top:470px;left:50%;transform:translateX(-50%);width:240px;height:240px;border-radius:50%;background:linear-gradient(135deg,#f1d9a4,#c99a4a);display:flex;align-items:center;justify-content:center;font-size:120px;box-shadow:0 0 0 26px rgba(233,207,150,.12),0 0 0 60px rgba(233,207,150,.06)}
h1{position:absolute;top:820px;left:60px;right:60px;font-family:Lora,serif;font-size:90px;line-height:1.1}
h1 i{color:#e9cf96}
p{position:absolute;top:1110px;left:100px;right:100px;font-size:38px;font-weight:300;color:#d6eeeb;line-height:1.45}
.pill{position:absolute;top:1330px;left:50%;transform:translateX(-50%);white-space:nowrap;background:linear-gradient(135deg,#f1d9a4,#c99a4a);color:#0b4644;border-radius:60px;padding:22px 50px;font-size:34px;font-weight:600}
.foot{position:absolute;bottom:150px;left:80px;right:80px;font-size:30px;color:#cfe8e5;line-height:1.5}
.foot .ph{font-size:44px;color:#e9cf96;font-weight:600;margin-bottom:8px}
</style>"""
    body = f'<div class="brand"><span class="bt">LARISA BEAUTY</span></div><div class="kick"><span>{kicker}</span></div><div class="icon">{icon}</div><h1>{title_html}</h1><p>{text}</p><div class="pill">{pill}</div>{FOOT_DARK}'
    return BASE % (css, body), (1080, 1920)


def story_poll(question_html, a, b, note):
    css = """<style>
body{width:1080px;height:1920px;background:radial-gradient(circle at 30% 25%,#1f8f8a,#0b4f4c 55%,#062f2d);color:#fff;text-align:center}
.brand{position:absolute;top:200px;left:0;right:0}
.q{position:absolute;top:330px;left:70px;right:70px;font-family:Lora,serif;font-size:92px;line-height:1.12}
.q i{color:#e9cf96}
.opts{position:absolute;top:840px;left:110px;right:110px;display:flex;flex-direction:column;gap:34px}
.o{background:#fff;color:#0b4644;border-radius:30px;padding:40px;font-size:48px;font-weight:600;box-shadow:0 20px 50px rgba(0,0,0,.25)}
.o small{display:block;font-size:28px;font-weight:400;color:#4f6e6c;margin-top:6px}
.note{position:absolute;top:1380px;left:100px;right:100px;font-size:34px;color:#d6eeeb;font-weight:300;line-height:1.45}
.foot{position:absolute;bottom:150px;left:80px;right:80px;font-size:30px;color:#cfe8e5;line-height:1.5}
.foot .ph{font-size:44px;color:#e9cf96;font-weight:600;margin-bottom:8px}
</style>"""
    body = f'<div class="brand"><span class="bt">LARISA BEAUTY</span></div><div class="q">{question_html}</div><div class="opts"><div class="o">{a[0]}<small>{a[1]}</small></div><div class="o">{b[0]}<small>{b[1]}</small></div></div><div class="note">{note}</div>{FOOT_DARK}'
    return BASE % (css, body), (1080, 1920)


def copy_story(post_jpg):
    css = """<style>
body{width:1080px;height:1920px;background:radial-gradient(circle at 30% 20%,#1f8f8a,#0b4f4c 55%,#062f2d);color:#fff;text-align:center}
.lbl{position:absolute;top:150px;left:0;right:0}
.lbl span{display:inline-block;border:2px solid #d4af6a;color:#e9cf96;border-radius:50px;padding:14px 40px;font-size:34px;letter-spacing:4px;font-weight:600}
img{position:absolute;top:290px;left:60px;width:960px;height:1200px;border-radius:28px;box-shadow:0 30px 70px rgba(0,0,0,.4)}
.cta{position:absolute;top:1560px;left:0;right:0;font-family:Lora,serif;font-size:56px}
.cta i{color:#e9cf96}
.ph{position:absolute;top:1680px;left:0;right:0;font-size:40px;font-weight:600;color:#e9cf96}
</style>"""
    body = f'<div class="lbl"><span>YENİ GÖNDERİ ✨</span></div><img src="file://{post_jpg}"><div class="cta">Profilde <i>tamamını</i> gör 👆</div><div class="ph">☎ 0545 151 71 79</div>'
    return BASE % (css, body), (1080, 1920)


TAGS = "#mavişehir #karşıyaka #izmir #izmirgüzellik #larisabeauty"
CONTACT = "📞 Randevu: 0545 151 71 79\n🌐 larisabeautyclub.com\n📍 Yalı Mah. 6523 Sk. No:32/B K:2 D:201 (Park Yaşam Ofis) Karşıyaka / İzmir"

ITEMS = [
    # (id, date, type, title, builder, caption)
    ("h-1115-story", "2026-11-15T18:00:00+03:00", "STORY", "Yeni hafta randevu hatırlatması",
     story_text("YENİ HAFTA", "Kendine <i>zaman ayır</i>", "Bu hafta sana iyi gelecek bakımı şimdiden planla", "Randevu: 0545 151 71 79", "💆‍♀️"), ""),
    ("h-1116-story", "2026-11-16T18:00:00+03:00", "STORY", "Anket: Doğal mı dramatik mi?",
     story_poll("Kirpikte<br>hangisi <i>sen?</i>", ("🌿 Doğal", "Hafif, günlük, fark edilmeden güzel"), ("✨ Dramatik", "Yoğun, hacimli, göz alıcı"), "Kararsız mısın? larisabeautyclub.com/kirpik adresinde canlı dene"), ""),
    ("h-1117-post", "2026-11-17T10:00:00+03:00", "POST", "Hangi kirpik stili sana göre?",
     grid_post("Hangi kirpik stili<br><i>sana göre?</i>", "Göz şekline ve tarzına göre seç", [
         ("Doğal", "Kendi kirpiklerine yakın uzunluk; günlük ve sade bir görünüm."),
         ("Kedi Gözü", "Dış köşelere doğru uzayan çizgi; gözü çeker, badem bakış verir."),
         ("Bebek Gözü", "Ortası daha uzun; gözü daha açık ve iri gösterir."),
         ("Dramatik", "Yoğun ve hacimli; özel günler ve iddialı bir bakış için."),
     ], "Canlı dene: larisabeautyclub.com/kirpik"),
     "Doğal mı, kedi gözü mü, bebek gözü mü, dramatik mi? 👀✨\n\nHer göz şekline yakışan bir kirpik stili var. Hangisinin sana uyduğundan emin değilsen, telefon kameranla stilleri canlı deneyebilirsin: larisabeautyclub.com/kirpik 📱\n\nYorumlara favori stilini yaz, birlikte karar verelim 💛\n\n" + CONTACT + "\n\n#kirpik #ipekkirpik #kirpikstili #kedigözü #kirpikuzatma " + TAGS),
    ("h-1117-story", "2026-11-17T18:00:00+03:00", "STORY", "Canlı kirpik deneme tanıtımı",
     story_text("YENİ ÖZELLİK", "Kirpiğini<br><i>önce kendinde</i> dene", "Telefon kameranla stilleri canlı gör, beğendiğini seç", "larisabeautyclub.com/kirpik", "📱"), ""),
    ("h-1118-post", "2026-11-18T10:00:00+03:00", "POST", "Tırnak bakımı 5 ipucu",
     list_post("Tırnakların<br><i>güçlü ve bakımlı</i>", [
         ("Eldivenle temizlik yap", "Deterjan ve su tırnakları kurutur, yumuşatır."),
         ("Tırnak etlerini nemlendir", "Her akşam birkaç damla bakım yağı yeter."),
         ("Tırnağı alet gibi kullanma", "Kutu, etiket açmak kırılmanın bir numaralı sebebi."),
         ("Tek yöne törpüle", "İleri geri törpülemek uçların açılmasına yol açar."),
         ("Bakımını aksatma", "Düzenli bakım, uzun süre şık görünüm demek."),
     ]),
     "Tırnaklarının hem güçlü hem bakımlı görünmesi için 5 basit alışkanlık 💅\n\n1️⃣ Bulaşık ve temizlikte eldiven kullan\n2️⃣ Tırnak etlerini her akşam nemlendir\n3️⃣ Tırnağını alet gibi kullanma\n4️⃣ Törpülerken tek yöne hareket et\n5️⃣ Düzenli bakımını aksatma\n\nKaydet, arkadaşınla paylaş 💛\n\n" + CONTACT + "\n\n#tırnak #tırnakbakımı #manikür #nailart #protez tırnak " .replace("#protez tırnak ", "#kalıcıoje ") + TAGS),
    ("h-1118-story", "2026-11-18T18:00:00+03:00", "STORY", "Randevu öncesi hazırlık",
     story_text("RANDEVU ÖNCESİ", "Kirpik randevusuna<br><i>hazır mısın?</i>", "Göz makyajsız gel · Lens takıyorsan çıkar · Rahat ol, uygulama boyunca gözlerin kapalı", "Sorular için: 0545 151 71 79", "👁️"), ""),
    ("h-1119-post", "2026-11-19T10:00:00+03:00", "POST", "Kışın cilt bakımı 4 ipucu",
     list_post("Kışın da<br><i>ışıl ışıl</i> bir cilt", [
         ("Nemlendiriciyi atlama", "Soğuk ve kalorifer cildi kurutur; sabah-akşam nemlendir."),
         ("Güneş kremi kışın da şart", "Bulutlu günlerde de güneş ışınları cilde ulaşır."),
         ("Sıcak değil ılık su", "Çok sıcak su cildin doğal yağını alır."),
         ("Bol su iç", "İçeriden nem, dışarıdan bakım kadar önemli."),
     ]),
     "Kış geldi, cildin de ilgi istiyor ❄️✨\n\n1️⃣ Nemlendiriciyi sabah-akşam kullan\n2️⃣ Güneş kremini kışın da bırakma\n3️⃣ Yüzünü sıcak değil ılık suyla yıka\n4️⃣ Gün boyu bol su iç\n\nCildine özel bakım için seni salonumuza bekliyoruz 💛\n\n" + CONTACT + "\n\n#ciltbakımı #kışbakımı #cilt #güzellik #skincare " + TAGS),
    ("h-1119-story", "2026-11-19T18:00:00+03:00", "STORY", "Sadakat kartı hatırlatması",
     story_text("UNUTMA", "5 işlem yap,<br><i>1'i bizden</i> 🎁", "Aynı işlemden 5 tane yaptır, 6.'sı hediye · 2 arkadaşını getir, 1 uygulama hediye", "Dijital Sadakat Kartı", "💛"), ""),
    ("h-1120-post", "2026-11-20T10:00:00+03:00", "POST", "Kirpik randevusu öncesi bilmen gerekenler",
     list_post("<span style='font-size:68px'>Kirpik randevusu<br><i>öncesi</i> bilmen gerekenler</span>", [
         ("Göz makyajsız gel", "Temiz kirpik, daha iyi tutunma demek."),
         ("Lens takıyorsan çıkar", "Uygulama boyunca gözlerin rahat olsun."),
         ("Kahveni sonra iç", "Rahat ve sakin olmak uygulamayı kolaylaştırır."),
         ("Gözlerin kapalı, sen dinlen", "Uygulama boyunca uzan ve keyfini çıkar."),
         ("İlk 24 saat su yok", "Uygulama sonrası ilk gün ıslatmamaya dikkat."),
     ]),
     "İlk kez ipek kirpik mi yaptıracaksın? İşte bilmen gerekenler 👁️✨\n\n✅ Göz makyajsız gel\n✅ Lens takıyorsan çıkar\n✅ Kahveni sonraya bırak, rahat ol\n✅ Uygulama boyunca gözlerin kapalı, sen dinlen\n✅ İlk 24 saat kirpiklerini ıslatma\n\nHafta sonu için yerini şimdiden ayırt 💛\n\n" + CONTACT + "\n\n#ipekkirpik #kirpik #kirpikuzatma #kirpikbakımı #izmirkirpik " + TAGS),
    ("h-1120-story", "2026-11-20T18:00:00+03:00", "STORY", "Hafta sonu randevu çağrısı",
     story_text("HAFTA SONU", "Hafta sonu<br><i>kendini şımart</i>", "Kirpik, tırnak ve cilt bakımında yerini şimdiden ayırt", "Hemen ara: 0545 151 71 79", "🌸"), ""),
    ("h-1121-post", "2026-11-21T10:00:00+03:00", "POST", "İpek kirpik sık sorulan sorular",
     grid_post("İpek kirpik<br><i>sık sorulanlar</i>", "Merak ettiklerinin kısa cevapları", [
         ("Islanır mı?", "İlk 24 saatten sonra evet; yüzünü rahatça yıkayabilirsin."),
         ("Makyaj?", "Yapabilirsin; yağ içermeyen ürünleri tercih et."),
         ("Dolgu ne zaman?", "Doğal dökülmeye göre genelde 2–3 haftada bir."),
         ("Nasıl bakarım?", "Her gün temiz bir fırçayla nazikçe tara, ovma."),
     ], "Başka sorun mu var? Bize yaz 💬"),
     "İpek kirpikle ilgili en çok sorulan sorular 💬✨\n\n💧 Islanır mı? İlk 24 saatten sonra evet.\n💄 Makyaj yapabilir miyim? Evet, yağ içermeyen ürünlerle.\n📅 Dolgu ne zaman? Genelde 2–3 haftada bir.\n🪮 Nasıl bakarım? Her gün nazikçe tara, ovma.\n\nAklına takılan başka bir şey varsa yorumlara ya da DM'den yaz, cevaplayalım 💛\n\n" + CONTACT + "\n\n#ipekkirpik #kirpik #kirpikbakımı #kirpikuzatma #sss " + TAGS),
]

COPY_TIMES = {"h-1117-post": "2026-11-17T10:05:00+03:00", "h-1118-post": "2026-11-18T10:05:00+03:00",
              "h-1119-post": "2026-11-19T10:05:00+03:00", "h-1120-post": "2026-11-20T10:05:00+03:00",
              "h-1121-post": "2026-11-21T10:05:00+03:00"}

manifest = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
    def render(name, html, size):
        hp = f"{OUT}/{name}.html"; open(hp, "w").write(html)
        pg = b.new_page(viewport={"width": size[0], "height": size[1]})
        pg.goto("file://" + hp); pg.wait_for_timeout(500)
        pg.screenshot(path=f"{OUT}/{name}.jpg", type="jpeg", quality=92); pg.close()
    for iid, date, typ, title, (html, size), cap in ITEMS:
        render(iid, html, size)
        manifest.append(dict(id=iid, date=date, type=typ, title=title, caption=cap, file=f"{iid}.jpg"))
        if iid in COPY_TIMES:
            cid = iid.replace("-post", "-copy")
            h2, s2 = copy_story(f"{OUT}/{iid}.jpg")
            render(cid, h2, s2)
            manifest.append(dict(id=cid, date=COPY_TIMES[iid], type="STORY", title=title + " (story)", caption="", file=f"{cid}.jpg", parent=iid))
    b.close()
json.dump(manifest, open(f"{OUT}/manifest.json", "w"), ensure_ascii=False, indent=1)
print(len(manifest), "items")
