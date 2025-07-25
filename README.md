
# Simple HTTP Header Analyzer

ይህ የፓይዘን ፕሮጀክት የድረ-ገጽ አድራሻ (URL) ተቀብሎ የHTTP Headersን የሚያወጣ እና ለደህንነት ወሳኝ የሆኑትን Headers ይተነትናል። የHTTP Headers ለድር አፕሊኬሽኖች ደህንነት ወሳኝ ናቸው፤ ይህ ፕሮጀክት በድር ደህንነት (Web Security) ላይ ያለህን ፍላጎት ያሳያል።

## የፕሮጀክቱ ዓላማ

* የድር አገልጋይ የHTTP ምላሽ Headersን እንዴት ማግኘት እንደሚቻል ማሳየት።
* የተለመዱ እና ወሳኝ የደህንነት Headersን መለየት እና ጠቀሜታቸውን ማብራራት።
* ለጀማሪ የሳይበር ሴኩሪቲ ተማሪዎች የድር ደህንነት መሰረታዊ ግንዛቤን መስጠት።

## እንዴት ይሰራል?

ስክሪፕቱ የ `requests` ላይብረሪን በመጠቀም ለተሰጠው URL የHTTP GET request ይልካል። ከምላሹ (response) ውስጥ የHTTP Headersን ያወጣና ያሳያል። ከዚያም፣ እንደ **Strict-Transport-Security (HSTS)**፣ **Content-Security-Policy (CSP)**፣ **X-Frame-Options**፣ **X-Content-Type-Options**፣ **Referrer-Policy** እና **Permissions-Policy** ያሉ የደህንነት Headers መኖር አለመኖራቸውን ይፈትሻል። እነዚህ Headers ባይኖሩም ተጋላጭነትን ሊያመለክት ይችላል።

በተጨማሪም፣ በ`Set-Cookie` Header ውስጥ `Secure` እና `HttpOnly` flags መኖራቸውን ይፈትሻል፣ ይህም የኩኪዎችን ደህንነት ያሻሽላል።

## እንዴት መጠቀም ይቻላል

1.  **የሚያስፈልገውን ላይብረሪ ጫን:**
    ```bash
    pip install requests
    ```
2.  **ፋይሉን አውርድ:** `http_header_analyzer.py` የሚለውን ፋይል ወደ ኮምፒውተርህ አውርድ።
3.  **ስክሪፕቱን አሂድ:**
    * **በሊኑክስ (WSL ወይም Virtual Machine):** ተርሚናል ከፍተህ ወደ ፋይሉ ዳይሬክተሪ ሂድና ይህንን ትዕዛዝ አስገባ:
        ```bash
        python3 http_header_analyzer.py
        ```
    * **በዊንዶውስ (Python ከተጫነ):** Command Prompt (CMD) ወይም PowerShell ከፍተህ ወደ ፋይሉ ዳይሬክተሪ ሂድና ይህንን ትዕዛዝ አስገባ:
        ```cmd
        python http_header_analyzer.py
        ```
4.  **URL አስገባ:** ስክሪፕቱ ሲጠይቅ ለመፈተሽ የሚፈልጉትን የድረ-ገጽ አድራሻ (URL) አስገባና Enter ተጫን (ለምሳሌ: `google.com`, `https://mozilla.org`)።
5.  **ውጣ:** ለመውጣት `q` ብለህ አስገባና Enter ተጫን።

## የደህንነት ጠቀሜታ

* **HSTS:** ከMan-in-the-Middle (MITM) ጥቃቶች ይጠብቃል፤ አሳሾች ሁልጊዜ HTTPSን እንዲጠቀሙ ያስገድዳል።
* **CSP:** XSS (Cross-Site Scripting) እና የዳታ ኢንጀክሽን (data injection) ጥቃቶችን ይከላከላል፤ አሳሹ ምን አይነት የድረ-ገጽ ሃብቶችን (scripts, stylesheets) መጫን እንደሚችል ይቆጣጠራል።
* **X-Frame-Options:** Clickjacking ጥቃቶችን ይከላከላል፤ የድረ-ገጽህን ይዘት በሌላ ድረ-ገጽ Frame ውስጥ እንዳይካተት ይከለክላል።
* **X-Content-Type-Options:** MIME sniffing ጥቃቶችን ይከላከላል፤ አሳሾች የፋይልን አይነት (ለምሳሌ `image/jpeg` ወይም `text/html`) ከይዘቱ ሳይሆን ከHeader እንዲወስዱ ያስገድዳል።
* **Referrer-Policy:** ከገጽህ ወደ ሌላ ገጽ ስትሄድ ምን ያህል Referrer information እንደሚላክ ይቆጣጠራል።
* **Permissions-Policy:** የአሳሹን ባህሪያት (ለምሳሌ ካሜራ፣ ማይክሮፎን፣ ጂፒኤስ) የድረ-ገጽህን ይዘት እንዲጠቀም መፍቀድ ወይም መከልከል ያስችላል።
* **Secure/HttpOnly Cookies:** `Secure` flag ኩኪዎች የሚላኩት በHTTPS ግንኙነት ብቻ መሆኑን ያረጋግጣል፤ `HttpOnly` flag ደግሞ client-side scripts (JavaScript) ኩኪዎችን እንዳይደርሱባቸው ይከለክላል፣ ይህም XSS ጥቃቶችን ይቀንሳል።

