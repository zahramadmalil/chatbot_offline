<div align="center">

# 🤖 Chatbot Offline with Ollama & Streamlit

### 📘 مستندات جامع و آموزش پیاده‌سازی چت‌بات آفلاین با هوش مصنوعی

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_AI-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📖 درباره پروژه

این مخزن، یک **پروژه کامل و عملی** برای ساخت یک چت‌بات هوش مصنوعی **کاملاً آفلاین** است. در این پروژه، از فریم‌ورک **Streamlit** برای ساخت رابط کاربری (UI) و از **Ollama** برای اجرای مدل‌های زبانی بزرگ (LLM) به صورت لوکال (بدون نیاز به اینترنت و API Key) استفاده شده است.

هدف این پروژه، آموزش نحوه اتصال یک رابط کاربری وب به یک مدل هوش مصنوعی محلی، مدیریت تاریخچه چت (Session State)، و اضافه کردن قابلیت‌های پیشرفته‌ای مثل **ذخیره چت** و **خلاصه‌سازی خودکار** است.

### 🗂️ فایل‌های پروژه

این پروژه شامل فایل‌های زیر است که هر کدام وظیفه مشخصی دارند:

| نام فایل | نوع | توضیح |
|---|---|---|
| `app.py` | کد اصلی | رابط کاربری Streamlit، مدیریت چت و دکمه‌ها |
| `utils.py` | کد کمکی | توابع ارتباط با Ollama، ذخیره فایل و خلاصه‌سازی |
| `requirements.txt` | وابستگی‌ها | لیست کتابخانه‌های مورد نیاز پروژه |

> ⚠️ **توجه:** فایل‌های پروژه در طول تمرین تکمیل شده‌اند. نسخه نهایی `app.py` و `utils.py` شامل تمام قابلیت‌ها (توقف مدل، پاک کردن تاریخچه، ذخیره و خلاصه‌سازی) هستند.

---

## ✨ ویژگی‌های کلیدی

- ✅ **کاملاً آفلاین:** بدون نیاز به اینترنت یا API Key (با استفاده از Ollama).
- ✅ **رابط کاربری مدرن:** استفاده از Streamlit برای ساخت چت‌روم زیبا و واکنش‌گرا.
- ✅ **مدیریت تاریخچه چت:** ذخیره پیام‌ها در `st.session_state` تا با رفرش صفحه پاک نشوند.
- ✅ **دکمه توقف مدل:** امکان متوقف کردن تولید پاسخ (در نسخه پیشرفته).
- ✅ **پاک کردن تاریخچه:** دکمه اختصاصی برای شروع مجدد چت.
- ✅ **ذخیره کل چت:** دانلود تمام مکالمات در قالب یک فایل متنی (`.txt`).
- ✅ **خلاصه‌سازی با AI:** تولید خودکار خلاصه از کل مکالمه توسط مدل و ذخیره آن.
- ✅ **مدیریت خطا:** نمایش پیام مناسب در صورت قطع ارتباط با Ollama.

---

## 🧰 پیش‌نیازها

قبل از اجرای پروژه، مطمئن شوید موارد زیر روی سیستم شما نصب شده‌اند:

- **Python** نسخه ۳.۸ یا بالاتر
- **Ollama** (نصب شده و در حال اجرا باشد)

### ۱. نصب Ollama
برای نصب Ollama، به سایت رسمی آن مراجعه کنید: [ollama.com](https://ollama.com/)
پس از نصب، در ترمینال دستور زیر را اجرا کنید تا سرویس Ollama فعال شود:

ollama serve

### ۲. دانلود مدل زبانی
در یک ترمینال جدید، مدل `gemma3:1b` (یا هر مدل دیگری) را دانلود کنید:

ollama pull gemma3:1b

---

## 🚀 نصب و راه‌اندازی پروژه

### ۱. کلون کردن مخزن
git clone https://github.com/your-username/chatbot-offline.git
cd chatbot-offline

### ۲. ساخت محیط مجازی (توصیه می‌شود)
python -m venv venv

در لینوکس/مک:
source venv/bin/activate

در ویندوز:
venv\Scripts\activate

### ۳. نصب وابستگی‌ها
کتابخانه‌های مورد نیاز را نصب کنید:
pip install -r requirements.txt

---

## 🎯 نحوه استفاده

پس از نصب، کافی است فایل اصلی Streamlit را اجرا کنید:

streamlit run app.py

سپس مرورگر شما به صورت خودکار باز می‌شود (معمولاً روی آدرس `http://localhost:8501`) و می‌توانید با چت‌بات گفتگو کنید.

---

## 📘 مستندات فنی فایل‌ها

### 📄 فایل `app.py` — رابط کاربری و منطق چت

این فایل مسئول نمایش صفحه وب، دریافت ورودی کاربر و مدیریت وضعیت (State) است.

#### 🎓 چه چیزی یاد می‌گیرید؟
- **تنظیمات صفحه:** `st.set_page_config`
- **مدیریت حافظه:** استفاده از `st.session_state` برای ذخیره پیام‌ها.
- **نمایش پیام‌ها:** استفاده از `st.chat_message` و `st.chat_input`.
- **نمایش لودینگ:** استفاده از `st.spinner` هنگام تولید پاسخ.
- **دکمه‌های تعاملی:** استفاده از `st.button` و `st.columns` برای چیدمان.

#### 💻 بخش‌های مهم کد:
**۱. مقداردهی اولیه:**
if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role': 'ai', 'content': 'How Can I Help You?'}]

**۲. دریافت ورودی و تولید پاسخ:**
prompt = st.chat_input('Enter Your Question')
if prompt:
    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role': 'user', 'content': prompt})
    
    with st.spinner('Generating Response...'):
        response = utils.call_ollama_model(prompt, MODEL)
        
    st.chat_message('ai').write(response)
    st.session_state['messages'].append({'role': 'ai', 'content': response})

**۳. دکمه‌های کنترل و ذخیره‌سازی:**
دکمه‌های «توقف مدل»، «پاک کردن تاریخچه»، «ذخیره کل چت» و «خلاصه‌سازی» در این فایل با استفاده از `st.button` پیاده‌سازی شده‌اند.

---

### 📄 فایل `utils.py` — توابع کمکی و ارتباط با Ollama

این فایل شامل توابعی است که منطق اصلی برنامه را از رابط کاربری جدا می‌کنند.

#### 🎓 چه چیزی یاد می‌گیرید؟
- **ارتباط HTTP:** استفاده از کتابخانه `requests` برای ارسال درخواست POST به Ollama.
- **مدیریت خطا:** استفاده از `try/except` برای جلوگیری از کرش برنامه در صورت قطع ارتباط.
- **کار با فایل:** خواندن و نوشتن در فایل‌های `.txt` با انکودینگ `utf-8`.
- **مهندسی پرامپت (Prompt Engineering):** ساخت یک پرامپت بهینه برای خلاصه‌سازی چت.

#### 💻 بخش‌های مهم کد:

**۱. اتصال به Ollama:**
def call_ollama_model(prompt, model, stream=False):
    url = 'http://localhost:11434/api/generate'
    payload = json.dumps({'prompt': prompt, 'model': model, 'stream': stream})
    
    try:
        response = requests.post(url, data=payload, headers={'Content-Type': 'application/json'}, timeout=900)
    except requests.exceptions.ConnectionError:
        return "❌ خطا: نمی‌توان به Ollama متصل شد. مطمئن شوید Ollama اجرا می‌شود."
    
    if response.status_code == 200:
        return response.json()['response']

**۲. خلاصه‌سازی چت:**
تابع `summarize_chat` کل مکالمه را به یک متن تبدیل کرده و با یک پرامپت بهینه (به زبان انگلیسی) از مدل می‌خواهد تا آن را به فارسی خلاصه کند.

**۳. ذخیره‌سازی:**
توابع `save_chat_to_file` و `save_summary_to_file` پیام‌ها را با فرمت مرتب در فایل‌های متنی ذخیره می‌کنند تا کاربر بتواند آن‌ها را دانلود کند.

---

## 🗂️ ساختار پیشنهادی پروژه

chatbot-offline/
│
├── app.py                # فایل اصلی رابط کاربری Streamlit
├── utils.py              # توابع ارتباط با مدل و ذخیره‌سازی
├── requirements.txt      # لیست کتابخانه‌های مورد نیاز
├── README.md             # همین فایل
└── .gitignore            # فایل‌های نادیده‌گرفته‌شده (مثل venv)

---

## 🧠 مفاهیم کلیدی آموزش‌داده‌شده

<details>
<summary><b>🔹 ۱. Streamlit چیست؟</b></summary>
Streamlit یک فریم‌ورک پایتون است که به شما اجازه می‌دهد بدون نیاز به HTML/CSS، یک رابط کاربری وب زیبا برای پروژه‌های داده و هوش مصنوعی بسازید.
</details>

<details>
<summary><b>🔹 ۲. Ollama چیست؟</b></summary>
Ollama ابزاری است که به شما امکان می‌دهد مدل‌های زبانی بزرگ (مثل Llama, Gemma, Mistral) را به صورت کاملاً آفلاین روی سیستم خود اجرا کنید. این ابزار یک API محلی در پورت `11434` ارائه می‌دهد.
</details>

<details>
<summary><b>🔹 ۳. Session State در Streamlit</b></summary>
در Streamlit، هر بار که کاربر با صفحه تعامل می‌کند، کل اسکریپت از نو اجرا می‌شود. برای اینکه تاریخچه چت از بین نرود، از `st.session_state` استفاده می‌کنیم که مانند یک حافظه موقت برای هر کاربر عمل می‌کند.
</details>

<details>
<summary><b>🔹 ۴. خلاصه‌سازی با AI (Prompt Engineering)</b></summary>
برای خلاصه‌سازی، ما کل متن مکالمه را به عنوان ورودی به مدل می‌دهیم و در پرامپت خود دقیقاً مشخص می‌کنیم که مدل چه نکاتی را باید خلاصه کند (مثلاً: موضوعات اصلی، سوالات کاربر، پاسخ‌های دستیار) و خروجی را به زبان فارسی بدهد.
</details>

---

## 🐛 عیب‌یابی رایج (Troubleshooting)

| مشکل | راه‌حل |
|------|--------|
| `ConnectionError` هنگام ارسال پیام | مطمئن شوید Ollama در پس‌زمینه اجرا می‌شود (دستور `ollama serve`). |
| مدل پاسخ نمی‌دهد | ممکن است مدل دانلود نشده باشد. با `ollama pull gemma3:1b` آن را دانلود کنید. |
| کندی در تولید پاسخ | مدل‌های بزرگ به منابع سیستم (RAM/GPU) نیاز دارند. از مدل‌های سبک‌تر مثل `gemma3:1b` استفاده کنید. |
| فونت فارسی در فایل‌های txt به هم می‌ریزد | مطمئن شوید فایل را با انکودینگ `UTF-8` باز می‌کنید. |

---

## ❓ سوالات متداول (FAQ)

**۱. آیا این چت‌بات به اینترنت نیاز دارد؟**
خیر، این پروژه برای اجرای کاملاً آفلاین طراحی شده است. تنها در مرحله اول (دانلود مدل) به اینترنت نیاز دارید.

**۲. چرا از `gemma3:1b` استفاده شده است؟**
این مدل حجم کمی دارد (حدود ۱ گیگابایت) و برای اجرا روی سیستم‌های معمولی مناسب است. شما می‌توانید با تغییر متغیر `MODEL` در `app.py` از مدل‌های قوی‌تر مثل `llama3` استفاده کنید.

**۳. آیا می‌توانم چت را در دیتابیس ذخیره کنم؟**
بله، در نسخه فعلی چت در فایل متنی ذخیره می‌شود، اما می‌توانید توابع `utils.py` را تغییر دهید تا از دیتابیس (مثل SQLite) استفاده کند.

---

## 🤝 مشارکت

از مشارکت شما در این پروژه استقبال می‌شود! برای همکاری:

1. پروژه را **Fork** کنید.
2. یک شاخه جدید بسازید: `git checkout -b feature/amazing-feature`
3. تغییرات خود را **Commit** کنید: `git commit -m "Add some amazing feature"`
4. شاخه را **Push** کنید: `git push origin feature/amazing-feature`
5. یک **Pull Request** باز کنید 🎉

---

## 📚 منابع پیشنهادی

- 📘 [مستندات رسمی Streamlit](https://docs.streamlit.io/)
- 📗 [مستندات رسمی Ollama](https://github.com/ollama/ollama)
- 📕 [مستندات کتابخانه Requests](https://requests.readthedocs.io/)

---

## 📄 مجوز

این پروژه تحت مجوز **MIT** منتشر شده است. برای اطلاعات بیشتر فایل [LICENSE](LICENSE) را مطالعه کنید.

---

<div align="center">

### ⭐ اگر این پروژه برایتان مفید بود، به آن ستاره بدهید! ⭐

ساخته شده با ❤️ و Python

</div>
