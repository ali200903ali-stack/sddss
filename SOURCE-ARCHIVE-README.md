# NineSoft Yemen ERP — استخراج المصدر التنفيذي

المصدر الكامل موجود في الفرع:

```text
build/ninesoft-production
```

بعد سحب الفرع، نفّذ من جذر المستودع:

```bash
python source-archive/assemble_source_v2.py
cd source-archive/NineSoft-System-Ready/NineSoft-System-Ready
python scripts/init_db.py --db data/ninesoft.db
python scripts/verify_system.py --db data/ninesoft.db
./start.sh
```

على Windows:

```bat
python source-archive\assemble_source_v2.py
cd source-archive\NineSoft-System-Ready\NineSoft-System-Ready
python scripts\init_db.py --db data\ninesoft.db
python scripts\verify_system.py --db data\ninesoft.db
start.bat
```

أداة التجميع:

- تجمع الأجزاء التسعة.
- تزيل التفاف الأسطر والمسافات فقط.
- ترفض أي حرف غير صالح في Base64.
- تتحقق من بصمة SHA-256 قبل الفك.
- تمنع مسارات الأرشيف غير الآمنة.

البصمة المعتمدة:

```text
f8166c30624ec4f3751edb250ffd9ceb17c2d653f2c448c62baa1aaef8b6ad9c
```

بعد الفك اقرأ:

1. `CODEX-HANDOFF.md`
2. `deployment/HOSTINGER.md`
3. `DEPLOYMENT-CHECKLIST.md`

ملاحظات:

- النظام يعمل بعملة YER الأساسية.
- الضريبة معطلة على مستوى قاعدة البيانات والمنطق المحاسبي.
- قاعدة SQLite تُنشأ عبر `scripts/init_db.py` ولا تُرفع إلى GitHub.
- تكامل WASL وWhatsApp يحتاج بيانات اعتماد حقيقية من العميل قبل التفعيل الخارجي.
