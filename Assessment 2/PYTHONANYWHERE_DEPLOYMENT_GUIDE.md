# PYTHONANYWHERE DEPLOYMENT GUIDE

**Student ID:** S315729  
**Project:** Ipswich E-commerce  
**Username:** azmatullah  
**Site URL:** http://azmatullah.pythonanywhere.com/

---

## 🚨 TROUBLESHOOTING "Unhandled Exception" ERROR

### STEP 1: Check Error Logs

1. Go to PythonAnywhere Web tab
2. Scroll down to "Log files" section
3. Click on **error.log** file
4. Look for the most recent error message

**Common errors and solutions:**

---

## ✅ COMPLETE DEPLOYMENT CHECKLIST

### PHASE 1: Clone Repository (Bash Console)

```bash
# Navigate to home directory
cd ~

# Clone your repository
git clone https://github.com/S315729/ipswich-ecommerce.git

# Verify files were cloned
cd ipswich-ecommerce
ls -la
```

**Expected output:** Should see all your Django files (manage.py, ipswich_ecommerce/, products/, etc.)

---

### PHASE 2: Create Virtual Environment (Bash Console)

```bash
# Create virtualenv with Python 3.10
mkvirtualenv --python=/usr/bin/python3.10 ipswich-env

# You should see (ipswich-env) in your prompt
# If not, activate it manually:
workon ipswich-env
```

**Verify Python version:**

```bash
python --version
# Should show: Python 3.10.x
```

---

### PHASE 3: Install Dependencies (Bash Console)

```bash
# Make sure you're in the project directory
cd ~/ipswich-ecommerce

# Install all requirements
pip install -r requirements.txt

# Verify installation
pip list
```

**Expected packages:**

- Django==4.2
- Pillow==9.5.0
- python-decouple==3.8
- gunicorn==21.2.0
- whitenoise==6.5.0

---

### PHASE 4: Configure Django Settings

**Update settings.py for production:**

```bash
# Edit settings file
nano ~/ipswich-ecommerce/ipswich_ecommerce/settings.py
```

**Add these changes:**

```python
# IMPORTANT: Add your PythonAnywhere domain to ALLOWED_HOSTS
ALLOWED_HOSTS = ['azmatullah.pythonanywhere.com', 'localhost', '127.0.0.1']

# Set DEBUG to False for production (but start with True for testing)
DEBUG = True  # Change to False after everything works

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

**Save and exit:** Ctrl+X, then Y, then Enter

---

### PHASE 5: Run Database Migrations (Bash Console)

```bash
# Navigate to project directory
cd ~/ipswich-ecommerce

# Run migrations
python manage.py migrate

# Expected output: "Applying [migration names]... OK"
```

---

### PHASE 6: Create Superuser (Bash Console)

```bash
python manage.py createsuperuser

# Enter details:
# Username: admin
# Email: s315729@uos.ac.uk
# Password: admin123 (or your preferred password)
```

---

### PHASE 7: Collect Static Files (Bash Console)

```bash
python manage.py collectstatic --noinput

# Should show: "X static files copied to '/home/azmatullah/ipswich-ecommerce/staticfiles'"
```

---

### PHASE 8: Configure Web App

#### A. Create Web App

1. Go to **Web** tab in PythonAnywhere
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"**
4. Select **"Python 3.10"**
5. Click **Next** through the dialogs

---

#### B. Configure WSGI File

1. In Web tab, find **"Code"** section
2. Click on **WSGI configuration file** (e.g., `/var/www/azmatullah_pythonanywhere_com_wsgi.py`)
3. **Delete ALL the default code**
4. **Replace with this:**

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/azmatullah/ipswich-ecommerce'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable to tell Django where your settings module is
os.environ['DJANGO_SETTINGS_MODULE'] = 'ipswich_ecommerce.settings'

# Import Django's WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

5. **Click "Save"** (top right)

**CRITICAL:** Make sure you replace `azmatullah` with your actual username if different!

---

#### C. Set Virtual Environment Path

1. In Web tab, scroll to **"Virtualenv"** section
2. Enter this path:
   ```
   /home/azmatullah/.virtualenvs/ipswich-env
   ```
3. The path should turn **blue** if correct

---

#### D. Configure Static Files Mapping

1. In Web tab, scroll to **"Static files"** section
2. Add two mappings:

**Mapping 1 - Static files:**

- URL: `/static/`
- Directory: `/home/azmatullah/ipswich-ecommerce/staticfiles`

**Mapping 2 - Media files:**

- URL: `/media/`
- Directory: `/home/azmatullah/ipswich-ecommerce/media`

3. Click **green checkmark** to save each mapping

---

### PHASE 9: Reload Web App

1. Scroll to top of Web tab
2. Click the big green **"Reload"** button
3. Wait for confirmation message

---

### PHASE 10: Test Your Site

1. Open a new browser tab
2. Go to: **http://azmatullah.pythonanywhere.com/**
3. You should see your Django homepage!

---

## 🔍 TROUBLESHOOTING COMMON ERRORS

### Error 1: ImportError - No module named 'django'

**Cause:** Django not installed or wrong virtualenv path

**Solution:**

```bash
workon ipswich-env
pip install -r requirements.txt
```

Then check virtualenv path in Web tab is correct:
`/home/azmatullah/.virtualenvs/ipswich-env`

---

### Error 2: DisallowedHost at /

**Error message:** "Invalid HTTP_HOST header: 'azmatullah.pythonanywhere.com'"

**Solution:** Update `settings.py`:

```python
ALLOWED_HOSTS = ['azmatullah.pythonanywhere.com', 'localhost']
```

Then reload web app.

---

### Error 3: Static files not loading (no CSS)

**Cause:** Static files not collected or mapping incorrect

**Solution:**

```bash
cd ~/ipswich-ecommerce
python manage.py collectstatic --noinput
```

Verify static files mapping in Web tab:

- URL: `/static/`
- Directory: `/home/azmatullah/ipswich-ecommerce/staticfiles`

---

### Error 4: OperationalError - no such table

**Cause:** Database migrations not run

**Solution:**

```bash
cd ~/ipswich-ecommerce
python manage.py migrate
```

---

### Error 5: 500 Internal Server Error

**Solution:** Check error log for details:

1. Go to Web tab
2. Click **error.log** link
3. Look for the traceback at the bottom
4. Common fixes:
   - Set `DEBUG = True` temporarily to see detailed error
   - Check all paths in WSGI file are correct
   - Verify virtualenv is activated

---

## 📋 VERIFICATION CHECKLIST

Before asking for help, verify:

- ✅ Repository cloned: `cd ~/ipswich-ecommerce && ls` shows files
- ✅ Virtualenv created: `workon ipswich-env` works
- ✅ Dependencies installed: `pip list` shows Django
- ✅ Migrations run: `python manage.py showmigrations` shows [X]
- ✅ Static files collected: `ls staticfiles/` shows files
- ✅ WSGI file configured correctly with YOUR username
- ✅ Virtualenv path set in Web tab
- ✅ Static files mapping added
- ✅ ALLOWED_HOSTS includes your domain
- ✅ Web app reloaded

---

## 🎯 QUICK FIX COMMANDS

If something goes wrong, run these in Bash console:

```bash
# Activate environment
workon ipswich-env

# Go to project
cd ~/ipswich-ecommerce

# Pull latest code
git pull origin main

# Reinstall dependencies
pip install -r requirements.txt --upgrade

# Remigrate database
python manage.py migrate

# Recollect static files
python manage.py collectstatic --noinput --clear

# Test Django
python manage.py check
```

Then reload web app in Web tab.

---

## 📸 SCREENSHOTS TO TAKE

### Screenshot 60: WSGI Configuration

- Show the complete WSGI file with your Django configuration
- **Caption:** "Figure 60: WSGI configuration linking web server to Django application"

### Screenshot 61: Virtual Environment Path

- Show the Virtualenv section with the path filled in
- **Caption:** "Figure 61: Configuring virtual environment path for production application"

### Screenshot 62: Static Files Configuration

- Show both static and media mappings
- **Caption:** "Figure 62: Configuring static and media file serving for production"

### Screenshot 63: Reload Web App

- Click the Reload button and capture the confirmation
- **Caption:** "Figure 63: Reloading web application to apply configuration changes"

### Screenshot 64: Live Homepage

- Your working site at http://azmatullah.pythonanywhere.com/
- **Caption:** "Figure 64: Live application homepage successfully deployed to production environment"

---

## 📞 GETTING HELP

If you're still stuck:

1. **Check error.log** - Most specific error information
2. **Check server.log** - HTTP request logs
3. **Forum:** https://www.pythonanywhere.com/forums/
4. **Email:** liveusercare@pythonanywhere.com
5. **Include:**
   - Your username (azmatullah)
   - Last 50 lines of error.log
   - What you were trying to do
   - What you've already tried

---

## ⚡ NEXT STEPS AFTER DEPLOYMENT WORKS

1. **Set DEBUG = False** in settings.py for security
2. **Test all functionality:**
   - Homepage loads
   - Products page shows items
   - Cart works
   - Admin panel accessible
3. **Take all required screenshots** (64-67)
4. **Populate production database** with sample products
5. **Test on different devices/browsers**

---

## 🔐 SECURITY NOTES

**Before submission:**

- Set `DEBUG = False` in production
- Never commit your `.env` file with secrets
- Use strong passwords for superuser
- Keep `SECRET_KEY` secret

---

## ✅ SUCCESS INDICATORS

Your deployment is successful when:

- ✅ http://azmatullah.pythonanywhere.com/ shows homepage
- ✅ Navigation works (Products, Cart, Admin links)
- ✅ Static files load (Bootstrap CSS visible)
- ✅ Admin panel accessible at /admin/
- ✅ No errors in error.log
- ✅ All pages load without 500 errors

---

**Good luck with your deployment! 🚀**

Need help? Check the error logs first, then refer to specific troubleshooting sections above.
