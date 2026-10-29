import streamlit as st
import time

# 1. Sayfa Yapılandırması
st.set_page_config(
    page_title="Sancak-Bayrak, İstiklâl Marşı",
    page_icon="🇹🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Özel CSS Tasarımı (Büyük Kalın Yazı ve Kopyalama Koruması)
st.markdown("""
    <style>
    .stApp {
        background-color: #FAFAFA;
    }
    
    /* Tek Büyük Kalın Söz Gösterim Kutusu */
    .single-quote-box {
        width: 100%;
        height: 35vh;
        background: linear-gradient(135deg, #7B0000 0%, #B22222 50%, #8B0000 100%);
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.25);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 30px;
        margin-bottom: 25px;
        border: 3px solid #DAA520;
        text-align: center;
        
        /* Metin seçimini ve kopyalamayı engelleme */
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
    
    .single-quote-text {
        font-family: 'Georgia', serif;
        font-size: 1.9rem;
        font-weight: 800;
        color: #FFFFFF;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
        margin-bottom: 15px;
        line-height: 1.4;
    }
    
    .single-quote-author {
        font-family: 'Georgia', serif;
        font-size: 1.3rem;
        font-style: italic;
        color: #FFD700;
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.7);
    }

    .header-container {
        text-align: center;
        padding: 20px 10px;
        background: linear-gradient(135deg, #8B0000 0%, #C0392B 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    .header-title {
        font-family: 'Georgia', serif;
        font-size: 2.2rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .header-subtitle {
        font-size: 1.1rem;
        font-style: italic;
        opacity: 0.95;
    }
    .disclaimer-box {
        background-color: #FFF8DC;
        border: 2px solid #DAA520;
        border-radius: 8px;
        padding: 15px 20px;
        margin-bottom: 25px;
        color: #5C4033;
        font-size: 0.95rem;
    }
    .poetry-card {
        background-color: #FFF5F5;
        border-left: 6px solid #C0392B;
        padding: 18px 25px;
        border-radius: 6px;
        margin-bottom: 25px;
        font-family: 'Georgia', serif;
        font-size: 1.25rem;
        color: #7B0000;
        font-weight: bold;
        line-height: 1.6;
        
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
    .info-card {
        background-color: #EBF5FB;
        border-left: 5px solid #2980B9;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 25px;
        font-size: 0.98rem;
        color: #1B4F72;
    }
    .article-box {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 8px;
        border: 1px solid #E0E0E0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        font-family: 'Georgia', serif;
        font-size: 1.12rem;
        line-height: 1.85;
        color: #2C3E50;
        text-align: justify;
        
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
    .highlight-paragraph {
        background-color: #FAF0E6;
        padding: 15px 20px;
        border-radius: 6px;
        border-left: 4px solid #D35400;
        margin: 15px 0;
        
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
    .footer-text {
        text-align: center;
        color: #7F8C8D;
        font-size: 0.9rem;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #E0E0E0;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Yan Menü (Sidebar) & Dil Seçimi
st.sidebar.markdown("### 🌐 Dil Seçimi / Language")
selected_lang = st.sidebar.selectbox("Dil / Language", ["Türkçe", "English"])

if selected_lang == "Türkçe":
    sb_title = "📜 Yayın Bilgileri"
    sb_author = "*Kaynak:* Tarihi Arşiv Belgeleri\n*(I. Cihan Harbi Medine Müdafası Hatıraları)*"
    sb_work = "*Eser:* Sancak-Bayrak, İstiklâl Marşı"
    sb_date = "*Yayın Tarihi:* 1 Nisan 2005"
    sb_source = "*Kaynak:* Hakikat Yayıncılık / Hakikat Dergisi\n*(Referans Eser: Medine Müdafası, Nâci Kâşif Kıcıman, Sebil Yayınevi)*"
    sb_terms_title = "⚖️ Kullanım Şartları"
    sb_terms_desc = """*HUKUKİ VE MANEVİ UYARI:\nBu uygulama **ticari amaçla kullanılamaz, satılamaz ve kopyalanamaz.** Sadece bilgi paylaşımı, manevi gelişim ve milli birlik ile beraberliği pekiştirmek amacıyla hazırlanmıştır."""
    search_label = "Makalede kelime arayın:"
    search_placeholder = "Örn: Hilâl, Emanet, Vatan..."
    header_title_text = "SANCAK-BAYRAK, İSTİKLÂL MARŞI"
    header_sub_text = "Hakikat Dergisi Arşivi (1 Nisan 2005)"
    disclaimer_text = """<b>📌 ÖNEMLİ BİLDİRİM VE KULLANIM İLKELERİ:</b><br>
        Bu yazılımın ve içerikte sunulan makalenin <b>hiçbir şekilde ticareti yapılamaz, kopyalanamaz ve ticari gayelerle çoğaltılamaz</b>. 
        Eserin kaynağı ve aidiyeti net olarak bellidir (Hakikat Yayıncılık / Hakikat Dergisi - Medine Müdafası). 
        Bu uygulama yalnızca <b>bilgi paylaşımı amacıyla, manevi gelişimi desteklemek, milli birlik ve beraberliğimizi güçlendirmek</b> üzere tasarlanmıştır."""
    poetry_text = """Dalgalan sen de şafaklar gibi ey şanlı hilâl!<br>Olsun artık dökülen kanlarımın hepsi helâl..."""
    history_note = """<b>Tarihi Not:</b> I. Cihan Harbi’nde Medine Müdafası sırasında kahraman askerler arasında Sancak-Bayrak hakkında açılan yarışmada yer alan bu anlamlı makale kısaltılarak aktarılmıştır.<br><i>(Bütün şehitlerimizin ruhları şâd olsun.)</i>"""
    footer_content = """<b>Kaynak:</b> Hakikat Yayıncılık — Hakikat Dergisi Arşivi (1 Nisan 2005)<br><i>(Medine Müdafasi, Nâci Kâşif Kıcıman, Sebil Yayınevi)</i><br><br><b>Manevi gelişim, milli birlik ve beraberlik gayesiyle hazırlanmıştır. Ticari amaçla kullanılamaz.</b>"""
    not_found_msg = "Aranan kelime veya ifade makalede bulunamadı."
    search_res_title = "🔎 İçeren Paragraflar"
    
    # Sadece Ayet ve Hadisler (Türkçe)
    quotes_list = [
        ("🇹🇷 \"Eğer biz onlara, 'Yurtlarınızdan çıkın veya yurdunuzdan çıkarılın' diye yazmış olsaydık, pek azı hariç bunu yapmazlardı.\"", "Kur'an-ı Kerim (Nisâ Suresi, 66)"),
        ("🇹🇷 \"Vatan sevgisi imandandır.\"", "Hadis-i Şerif (Aclûnî, Keşfül-Hafâ, II, 313)"),
        ("🇹🇷 \"Hiç şüphe yok ki Allah, kendi yolunda duvar gibi saf bağlayarak çarpışanları sever.\"", "Kur'an--ı Kerim (Saff Suresi, 4)")
    ]
else:
    sb_title = "📜 Publication Info"
    sb_author = "*Source:* Historical Archives\n*(Memoirs of the Defense of Medina, WWI)*"
    sb_work = "*Work:* Banner-Flag, Independence Anthem"
    sb_date = "*Publication Date:* April 1, 2005"
    sb_source = "*Source:* Hakikat Publishing / Hakikat Magazine\n*(Reference Work: Medine Müdafası, Nâci Kâşif Kıcıman, Sebil Publishing)*"
    sb_terms_title = "⚖️ Terms of Use"
    sb_terms_desc = """*LEGAL & SPIRITUAL WARNING:\nThis application **cannot be used for commercial purposes, cannot be sold or copied.** It has been prepared solely for information sharing, spiritual development, and strengthening national unity."""
    search_label = "Search keyword in the article:"
    search_placeholder = "E.g., Flag, Trust, Homeland..."
    header_title_text = "BANNER-FLAG, INDEPENDENCE ANTHEM"
    header_sub_text = "Hakikat Magazine Archive (April 1, 2005)"
    disclaimer_text = """<b>📌 IMPORTANT NOTICE & USAGE PRINCIPLES:</b><br>
        This software and the article presented herein <b>cannot be commercialized, copied, or reproduced for commercial purposes in any way</b>. 
        The source and ownership of the work are clearly defined (Hakikat Publishing / Hakikat Magazine - Medine Müdafası). 
        This application is designed solely for <b>information sharing, supporting spiritual development, and strengthening our national unity and solidarity</b>."""
    poetry_text = """Wave like the dawns, O glorious crescent!<br>May all the blood I shed be fully halal..."""
    history_note = """<b>Historical Note:</b> This meaningful article, written during the Defense of Medina in WWI regarding the Banner-Flag, is presented in an abridged version.<br><i>(May the souls of all our martyrs rest in peace.)</i>"""
    footer_content = """<b>Source:</b> Hakikat Publishing — Hakikat Magazine Archive (April 1, 2005)<br><i>(Medine Müdafasi, Nâci Kâşif Kıcıman, Sebil Publishing)</i><br><br><b>Prepared for spiritual development and national unity. Cannot be used commercially.</b>"""
    not_found_msg = "The searched keyword or phrase was not found in the article."
    search_res_title = "🔎 Matching Paragraphs"
    
    # Sadece Ayet ve Hadisler (İngilizce)
    quotes_list = [
        ("🇹🇷 \"If We had decreed upon them, 'Leave your homes,' they would not have done it, except for a few of them.\"", "Quran (An-Nisa, 66)"),
        ("🇹🇷 \"Love of the homeland is from faith.\"", "Hadith (Ajluni, Kashf al-Khafa)"),
        ("🇹🇷 \"Indeed, Allah loves those who fight in His cause in a row as though they were a single structured structure.\"", "Quran (As-Saf, 4)")
    ]

st.sidebar.markdown(f"### {sb_title}")
st.sidebar.markdown(f"{sb_author}\n\n{sb_work}\n\n{sb_date}\n\n{sb_source}")
st.sidebar.markdown("---")
st.sidebar.markdown(f"### {sb_terms_title}")
st.sidebar.warning(sb_terms_desc)
st.sidebar.markdown("---")
st.sidebar.markdown(f"### 🔍 {search_label.split()[0]} Search")
search_query = st.sidebar.text_input(search_label, placeholder=search_placeholder)

# 4. Tek Büyük Kalın Söz Alanı (Sıralı Geçiş)
if 'quote_index' not in st.session_state:
    st.session_state.quote_index = 0

current_quote, current_author = quotes_list[st.session_state.quote_index]

st.markdown(f"""
    <div class="single-quote-box">
        <div class="single-quote-text">{current_quote}</div>
        <div class="single-quote-author">— {current_author}</div>
    </div>
""", unsafe_allow_html=True)

# 5. Ana Sayfa Başlık
st.markdown(f"""
    <div class="header-container">
        <div class="header-title">{header_title_text}</div>
        <div class="header-subtitle">{header_sub_text}</div>
    </div>
""", unsafe_allow_html=True)

# 6. Bildirim ve Uyarı Kutusu
st.markdown(f"""
    <div class="disclaimer-box">
        {disclaimer_text}
    </div>
""", unsafe_allow_html=True)

# 7. Şiir ve Tarihi Bilgi Kutuları
st.markdown(f"""
    <div class="poetry-card">
        {poetry_text}
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class="info-card">
        {history_note}
    </div>
""", unsafe_allow_html=True)

# 8. Makale Metinleri
if selected_lang == "Türkçe":
    p1 = "O, ecdadın ve ‘Âl-i Osman’ın pâk ve mübârek kanlariyle nescedüp bize teslim eyledikleri bir emânettir. O, öyle bir çevredir ki; bütün Osmanlılığın mevcûdiyetini, şan ve şerefini, tarih ve mukaddesatını, kadınlarımızın ırz ve namusunu, kızlarımızın bekâretini, çocuklarımızın saadetini çıkınlıyor. Biz onun üzerine nasıl titremeyiz? Hepimize teneffüs hakkı veren odur. Hey’et-i içtimaiyemize ifaza-i hayat ve hararet eden hep onun asîl ve civanmerd kalbidir."
    p2 = "Eğer O çarpmazsa bizim de nabzımız atmaz, göğsümüz vurmaz. Allah esirgesin, eğer onun gülbenzi hasara uğrarsa ‘Kâbe’mizin kara gömleği yırtılır. Peygamberimizin yeşil örtüsü çâk edilir. Analarımızın ak saçı yolunur, kızlarımızın ırzı hetk olunur."
    p3 = "Görmüyor musunuz? Ne kadar canlı, asabî, serbâz ve serefrâz!.. Hiçbir gelin o kadar sevimli, zarif ve nâzenin olamaz. Hiçbir delikanlı onun kadar şehlevend, cevvâl ve nevcivân değildir. Bizzat atalarımızın ruh-i pür fütûhunu hâmil olmasaydı, saflarımızın önünde bu kadar kahramanca göğüs gerer miydi?"
    p4 = "Sancağımız hayat-i ebedîye ile bahtiyardır. Vatanın fedakâr çocukları kanlarını, canlarını ona hibe ve ilhak ettikleri içindir ki; daima böyle genç ve dinç kalacaktır."
    p5 = "Karşısında cephe alarak resm-i ta’zim ifâ edişimiz sebepsiz değildir. Biz onda, bütün ‘Âl-i Osman’ı, mâzimizin kahramanlıklarını, mefkûremiz uğrunda can veren bütün âbâ ve evliya-yi vatanı selâmlıyoruz. Tarihimiz ziyaa uğrarsa, Sancağımız onu yeniden ibda’ ve te’lif edebilir. Ona bakarken nasıl göğsümüz şişmez, nasıl gözlerimiz yaşarmaz?.. Yedi asrın şan ve şükûhunu, âlâm ve fecâyiini ihtiva eden bu emsalsiz temaşa bizi saatlerce hıçkırtıp ağlatsa yeridir!.."
    p6 = "Ya o al rengi biliyor musunuz? Memleketin bütün mukadderatı ve aziz istikbali için o kadar cömertçe akıtılan kanlara işaret ediyor. Filvâki babalarımız, yurdumuz için kadınların da yapabilecekleri gibi yalnız gözyaşı dökmediler."
    p7 = "Bu ocağı kurarken, bizzat kendilerini kurban ettiler. Sancağımızı kaldırmak için düştüler. Onun şan ve şerefle dalgalanması için kendi ciğerlerinin şehik ve zefirlerinden kasr ve tasarruf ettiler."
    p8 = "Onda çırpınan şey, eslâfımızın ervah-ı gayretidir. Onun mukaddes alevinde yanan çıra, şehidlerimizin ecza-yi intikamıdır."
    p9 = "Dünyanın bütün çiçekleri ‘Albayrak’ın yanında renksiz ve kokusuzudur. Biz onun katmerlerinde bizzat cenneti koklarız. Bozkırlarda onun ateşi etrafında ısınırız, kum çöllerinde onun gelincik terâvetiyle yüreğimizi tâzeleriz. Fecrin akını gibi bir gecede Asya’dan Avrupa’ya baskın yapan Bayrağımızı bütün ufuklar tanır... ‘Eflâk’, ‘Buğdan’ Ovaları, ‘Avusturya-Macaristan’, ‘Lehistan’ Sahraları, ‘Volga-Tebriz’ illeri, ‘Cezayir-Nis’ sahilleri hep onun devrine ve devlet-i dâmenbûsuna erdiler."
    p10 = "‘Bosna ve Kırım’ın bahçeleri, İran’ın gülistanları bu kadar güzel âteşin bir gül daha asla vermeyecek. Tuna yalıları, Hind suları Hilâlimiz gibi mürassa’ ve müsa’şa, bir gerdanlık madâm-el-hayat takınmayacaktır."
    p11 = "Atalarımız, nasıl bayrağımızı damarlarının en girânbâhâ yakutlariyle bezemişlerse, analarımız da en güzel incilerini onun üzerine işlemişlerdir. Şu ‘Ay’a bakınız, suyu ne kadar temiz ve şeffaf!.. Mukadderatımızın hulliyati için en kıymetlisi, şüphe yok, budur. Çünkü; sevgili ninelerimizin sıcak ve samimi gözyaşlariyle tarsi’ edilmiştir. Ya hepimizin gözbebeği olan şu parlak ‘Yıldız’... Bizi bütün gece yatağımızın başucunda uyanık bekleyen odur!.. Müddet-i hayatında bir kere bile kirpiklerini kırpmamış, her zaman üzerimize titremiş, obamızı, yurdumuzu, serhadlerimizi canfedâyâne korumuştur. Bize olan rifk-u şâfakatı annelerimizinkinden fazladır. Nazarı kuru, fakat gözleri doludur."
    p12 = "Sancağımızın şan ve şerefle taşıdığı büyük hamâil altında henüz kanayan cerihaları da vardır. O’nun vakit vakit kabaran göğsü, çocuklarına söylemek istemediği, maamafih hepimizin bildiği hicranlarını kâfi derecede tefsir eder. Bu yaraları zaman ve nisyan tedâvi edemez. Onları sarıp kapatacak olan ancak genç nesillerdir ve bayrağımız işte bu ümid ile mağrur ve gururunda mazurdur. İnsaf ediniz, hangi baba evlâdlarına mağrur olmaz?.."
    p13 = "Asırlardır mefâhiriyle doldurmuş, bütün Şark’a bir fecr-i sâdık getirmiş, Allah’ın dava-yi vahdanîyeti, peygamberin tarik-ı hidâyeti, Hakk’ından ve nefsinden emin olanlara has bir kahramanlıkla, her zaman bir başına müdafaa etmiş insaniyetin nısfı mazlumunu bağrına basmış olan Sancağımıza lâyık olduğu zafer ve istikbâli Allah dirığ etmeyecek!.. Bizzat istikbâl, ondan başkasının dudağını açmasına müsaade eylemeyecektir. Her Osmanlı genci, Bayrağı’nın aşkiyle bîihtiyardır. Onun gölgesinde gelecek her ölümü, vallahi anası gibi kucaklar!.."
    p14 = "Boralarla şakalaşan, tayfunlarla oynaşan, tarihlere meydan okuyan ve Dünya’larla savaşan Türkler’in Bayrağı!.. Fâtihlerin Sancağı hakkındaki hikâyeler aşk ve ölümle nihâyet buluyordu."
else:
    p1 = "It is a sacred trust woven by our ancestors and the House of Osman with their pure and blessed blood, handed down to us. It is such an encompassing circle that it embodies the entire existence, glory, honor, history, and sacred values of Ottomanism, the chastity and honor of our women, the purity of our daughters, and the happiness of our children. How can we not cherish it? It is the very entity that grants us the right to breathe. The noble and chivalrous heart of the banner is what infuses life and warmth into our society."
    p2 = "If it does not beat, our pulse ceases, our chest stops heaving. God forbid, if its crimson hue suffers damage, the black cover of our Kaaba would be torn, the green veil of our Prophet would be rent, the white hair of our mothers would be torn out, and the chastity of our daughters would be violated."
    p3 = "Do you not see it? How vibrant, spirited, bold, and proud!.. No bride can be as lovely, graceful, and delicate. No youth is as fervent, dynamic, and youthful as it is. Had it not carried the triumphant spirit of our ancestors itself, would it have stood so heroically at the forefront of our ranks?"
    p4 = "Our Banner is blessed with eternal life. Because the devoted children of the homeland have dedicated and united their blood and lives with it, it will always remain so young and vigorous."
    p5 = "Our bowing before it in formal salute is not without reason. In it, we salute the entire House of Osman, the heroics of our past, and all the fathers and saints of the homeland who gave their lives for our ideals. Should our history perish, our Banner can recreate and author it anew. How can our chests not swell, how can our eyes not fill with tears while looking at it?.. This peerless spectacle containing the glory, splendor, grief, and tragedies of seven centuries is enough to make us weep in sobs for hours!"
    p6 = "Do you know that crimson color? It points to the blood so generously shed for the destiny and sacred future of the country. Indeed, our fathers did not merely shed tears as women might do for the homeland."
    p7 = "While establishing this hearth, they sacrificed themselves. They fell to raise our Banner. They practiced self-denial from the sighs and breaths of their own chests so that it might wave with glory and honor."
    p8 = "What flutters in it is the zeal-filled spirit of our predecessors. The fire burning in its sacred flame is the vengeance-part of our martyrs."
    p9 = "All the flowers of the world are colorless and scentless next to the 'Red Flag'. We smell paradise itself in its folds. We warm ourselves around its fire in the steppes, and we refresh our hearts with the poppy-like freshness of it in sand deserts. Like the dawn's rush, raiding from Asia to Europe in a single night, our Flag is recognized by all horizons... The plains of Wallachia and Moldavia, the steppes of Austria-Hungary and Poland, the regions of Volga-Tabriz, and the coasts of Algiers and Nice have all attained its era and kissed its threshold."
    p10 = "The gardens of Bosnia and Crimea, the rose gardens of Iran will never produce another rose as lovely and fiery as this. The shores of the Danube and the waters of India will never wear a necklace as gem-studded and radiant as our Crescent for the duration of life."
    p11 = "Just as our ancestors adorned our flag with the most precious rubies of their veins, our mothers have embroidered their most finest pearls upon it. Look at that 'Crescent', how pure and transparent its waters are!.. Without a doubt, this is the most precious thing for the permanence of our destiny. Because it is studded with the warm and sincere tears of our beloved grandmothers. And that bright 'Star', the apple of all our eyes... It is the one that kept watch over our bedside all night long!.. Not once blinking its eyelashes throughout its life, always watching over us, protecting our settlements, homeland, and borders with self-sacrifice. Its compassion toward us exceeds that of our mothers. Its gaze is dry, but its eyes are full."
    p12 = "Under the grand sash that our Banner carries with glory and honor, there are still bleeding wounds. Its swelling chest from time to time sufficiently interprets its heartbreaks, which it does not wish to tell its children, yet we all know. Time and oblivion cannot cure these wounds. Only the young generations can bandage and close them, and our Banner is excusable in its pride and haughtiness precisely with this hope. Have some fairness, which father would not be proud of his children?"
    p13 = "God will not withhold the victory and future deserved by our Banner—which has filled ages with its glorious deeds, brought a true dawn to the entire East, defended single-handedly with a courage unique to those secure in God's oneness, the Prophet's guidance, and their own righteousness, and embraced the oppressed half of humanity!.. Future itself will not allow anyone other than it to open its lips. Every Ottoman youth is involuntarily in love with his Flag. By God, he embraces every death that comes under its shadow just like his mother!"
    p14 = "The Flag of the Turks who joke with storms, play with typhoons, challenge histories, and fight worlds!... The stories concerning the Banners of the Conquerors were ending with love and death."

paragraphs = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]

# 9. Arama Özelliği
if search_query:
    st.subheader(f"{search_res_title} ('{search_query}')")
    found = False
    for idx, p in enumerate(paragraphs, 1):
        if search_query.lower() in p.lower():
            highlighted_p = p.replace(search_query, f"*{search_query}*")
            st.markdown(f"<div class='highlight-paragraph'><b>Paragraph {idx}:</b><br>{highlighted_p}</div>", unsafe_allow_html=True)
            found = True
    if not found:
        st.warning(not_found_msg)
else:
    st.markdown("<div class='article-box'>", unsafe_allow_html=True)
    for p in paragraphs:
        st.write(p)
        st.write("")
    st.markdown("</div>", unsafe_allow_html=True)

# 10. Alt Bilgi (Footer)
st.markdown(f"""
    <div class="footer-text">
        {footer_content}
    </div>
""", unsafe_allow_html=True)

# 11. Sayfa yenileme ve sıradaki söze geçiş (Ayet ve Hadislerin sırayla görünmesi için)
st.session_state.quote_index = (st.session_state.quote_index + 1) % len(quotes_list)
time.sleep(5)
st.rerun()