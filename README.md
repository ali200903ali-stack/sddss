# NineSoft Yemen ERP

نظام محاسبي ومخزني يمني قابل للتشغيل، مبني على واجهة NineSoft المعتمدة، بلا ضريبة، ويدعم الفواتير والمشتريات والمخزون والعملاء والموردين وشجرة الحسابات والقيود والسندات والتقارير والجرد والنسخ الاحتياطي.

## تشغيل سريع

```bash
python scripts/init_db.py --db data/ninesoft.db
./start.sh
```

- المدير: `admin` / `ChangeMe!2026`
- المبيعات: `sales` / `Sales!2026`

يجب تغيير كلمة مرور المدير قبل النشر. تعليمات Hostinger موجودة في `deployment/HOSTINGER.md`.
