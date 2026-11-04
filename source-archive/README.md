# NineSoft Yemen ERP — Source Archive

هذا الفرع يحتوي مصدر النظام التنفيذي في أرشيف نصي مقسم حتى يبقى المستودع خفيفًا وقابلًا للسحب عبر GitHub.

## استخراج المصدر

من جذر المستودع شغّل:

```bash
python source-archive/assemble_source.py
cd source-archive/NineSoft-System-Ready
python scripts/init_db.py --db data/ninesoft.db
python scripts/verify_system.py --db data/ninesoft.db
./start.sh
```

على Windows:

```bat
python source-archive\assemble_source.py
cd source-archive\NineSoft-System-Ready
python scripts\init_db.py --db data\ninesoft.db
start.bat
```

بصمة أرشيف المصدر المتوقعة:

```text
SHA-256: f8166c30624ec4f3751edb250ffd9ceb17c2d653f2c448c62baa1aaef8b6ad9c
```

أداة التجميع ترفض الفك إذا كان أي جزء مفقودًا أو إذا لم تتطابق البصمة، وتمنع المسارات غير الآمنة داخل الأرشيف.

## ملاحظات مهمة لكوديكس

- المرجع التنفيذي الكامل موجود بعد الفك في `source-archive/NineSoft-System-Ready/`.
- اقرأ أولًا `CODEX-HANDOFF.md` ثم `deployment/HOSTINGER.md`.
- النظام يمني بالكامل، عملته الأساسية YER، والضريبة معطلة على مستوى قاعدة البيانات.
- قاعدة SQLite لا تُحفظ في GitHub؛ أنشئها بالأمر المذكور أعلاه أو استخدم ملف ZIP الكامل المسلم للمستخدم، وهو يحتوي قاعدة جاهزة.
- بيانات WASL وWhatsApp تحتاج مفاتيح وبيانات اعتماد العميل قبل تفعيل الربط الخارجي.
