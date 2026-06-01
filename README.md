# Mini Company Knowledge Bot (Fartak Tech)

A lightweight AI-powered CLI assistant that answers employee queries based on internal company documents. Built as a demonstration of AI integration, context management, and project documentation.

## 📁 Project Structure
fartak-knowledge-bot/
├── bot.py                   # اسکریپت اصلی و منطق ربات (اجرای CLI و ارتباط با API گوگل)
├── requirements.txt         # لیست وابستگی‌های پایتون (google-genai, python-dotenv)
├── .env                     # متغیرهای محیطی (شامل کلید API - در گیت ثبت نمی‌شود)
├── .gitignore               # جلوگیری از آپلود فایل‌های حساس و کش‌ها در گیت‌هاب
├── README.md                # مستندات اصلی پروژه و راهنمای اجرا
│
├── docs/                    # پایگاه دانش شرکت (فایل‌های متنی که ربات می‌خواند)
│   ├── it_support.txt       # قوانین شبکه، VPN و پشتیبانی IT
│   ├── leave_policy.txt     # قوانین مرخصی کارکنان شرکت
│   └── product_specs.txt    # معرفی محصول و ویژگی‌های سیستم (EPMS)
│
└── agentic-brain/           # مغز متفکر پروژه و مستندات مدیریت فرآیند
    ├── PROJECT_BRIEF.md     # تعریف اهداف پروژه، معماری و MVP
    ├── AGENT_CONTEXT.md     # تعریف نقش هوش مصنوعی، قوانین و گاردریل‌ها (Guardrails)
    ├── MEMORY.md            # ثبت تصمیمات معماری، لاگ خطاها و مسیر یادگیری
    ├── TASKS.md             # چک‌لیست کارهای انجام‌شده و توسعه‌های آینده
    └── EVALS.md             # سناریوهای تست و ارزیابی کیفیت پاسخ‌های ربات
    
## Features
- **Dynamic Context Loading:** Reads `.txt` files from the `docs/` directory automatically.
- **Strict Guardrails:** Instructed to avoid hallucinations and only answer based on provided context.
- **Agentic Brain:** Includes a structured `agentic-brain/` directory detailing the project brief, memory, tasks, and evaluations.

## How to Run

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt


