# نشر مصر تحكي على PythonAnywhere بدون بطاقة

هذا المشروع يعمل كـ Django WSGI app، لذلك استخدم PythonAnywhere لتشغيله كخادم حقيقي.

## 1. إنشاء الحساب

أنشئ حساب Beginner مجاني من PythonAnywhere، ثم افتح Bash Console.

## 2. رفع المشروع

إذا كان المشروع على GitHub:

~~~bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git discover_egypt
cd discover_egypt
~~~

أو ارفع ملفات المشروع من تبويب Files.

## 3. تثبيت البيئة

~~~bash
mkvirtualenv --python=/usr/bin/python3.13 discover-egypt
workon discover-egypt
pip install -r requirements.txt
~~~

## 4. تجهيز قاعدة البيانات والملفات الثابتة

~~~bash
cd ~/discover_egypt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py check --deploy
~~~

المهاجرات تنشئ المحتوى العربي الافتتاحي تلقائيًا، ولا تحتاج إلى نسخ db.sqlite3 من جهازك.

## 5. إنشاء Web App

من تبويب **Web**:

1. اختر **Add a new web app**.
2. اختر **Manual configuration**.
3. اختر Python 3.13.
4. اربط البيئة الافتراضية discover-egypt.
5. افتح ملف WSGI والصق محتوى pythonanywhere_wsgi.py.example.
6. استبدل YOUR_USERNAME باسم حسابك الحقيقي.
7. استبدل مسار المشروع إذا اخترت مجلدًا مختلفًا.

## 6. إعداد المتغيرات

في قسم Environment variables أضف:

~~~text
DEBUG=False
DJANGO_SECRET_KEY=ضع-مفتاحًا-عشوائيًا-طويلًا
PYTHONANYWHERE_USERNAME=اسم-حسابك
~~~

الإعدادات تضيف نطاق اسم-حسابك.pythonanywhere.com تلقائيًا إلى ALLOWED_HOSTS وCSRF_TRUSTED_ORIGINS.

## 7. static files

في تبويب Web أضف:

~~~text
URL: /static/
Directory: /home/YOUR_USERNAME/discover_egypt/staticfiles
~~~

ثم اضغط **Reload**.

سيكون الموقع على:

~~~text
https://YOUR_USERNAME.pythonanywhere.com/
~~~

الحساب المجاني مناسب للتجربة والمشروع الشخصي، لكنه محدود بعامل تشغيل واحد وسعة موارد محدودة، وقد يتوقف التطبيق غير المستخدم وفق سياسة الحساب المجاني الحالية.
