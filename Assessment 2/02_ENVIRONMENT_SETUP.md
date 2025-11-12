# STEP 2: ENVIRONMENT SETUP DOCUMENTATION

**Date:** November 12, 2025  
**Student ID:** S315729  
**Project:** Ipswich Retail E-commerce DevOps Implementation

---

## 2.1 GIT CONFIGURATION FOR S315729 ACCOUNT

### Issue: PC Login vs GitHub Account

**Problem:**

- PC is logged in as: DanishButt586
- Project must be under different account: S315729
- Need to configure local Git to use correct identity

### Solution: Local Git Configuration

#### Commands Executed:

```powershell
# Navigate to project directory
cd C:\Users\Administrator\Downloads\DevOps

# Configure Git user name (local to this repository)
git config user.name "S315729"

# Configure Git user email (local to this repository)
git config user.email "s315729@student.uos.ac.uk"

# Verify configuration
git config user.name
git config user.email
```

#### Verification Results:

```
Git Username: S315729
Git Email: s315729@uos.ac.uk
```

✅ **Status:** Git configured correctly for S315729 account

### Why This Matters:

When commits are pushed to GitHub, they will be attributed to **S315729** (the student account) rather than the PC login account (DanishButt586). This ensures:

1. Proper academic attribution
2. Correct GitHub profile association
3. Assessment submission under correct identity
4. Professional portfolio building

### Git Configuration Scope:

**Local (repository-specific):** `git config user.name "S315729"`

- Only affects THIS repository
- Doesn't change global Git settings
- Perfect for using different accounts for different projects

**Global (all repositories):** `git config --global user.name "S315729"`

- Would affect ALL repositories on this PC
- NOT recommended if PC is shared or used for multiple accounts

---

## 2.2 PYTHON VIRTUAL ENVIRONMENT

### Purpose of Virtual Environment:

Virtual environments provide **isolated Python package installations** for each project, preventing:

- Dependency conflicts between projects
- Polluting global Python installation
- Version incompatibilities
- "Works on my machine" issues

### Virtual Environment Setup:

#### Creation (Already Done):

```powershell
# Create virtual environment
python -m venv .venv
```

This creates a `.venv/` directory containing:

- Isolated Python interpreter
- pip package manager
- Site-packages directory for dependencies

#### Activation:

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

#### Verification:

After activation, terminal prompt shows:

```
(.venv) PS C:\Users\Administrator\Downloads\DevOps>
```

The `(.venv)` prefix confirms the virtual environment is active.

#### Deactivation:

```powershell
deactivate
```

### Current Virtual Environment Status:

✅ Virtual environment exists: `.venv/`  
✅ Virtual environment active in terminal  
✅ Ready for package installation

---

## 2.3 DEPENDENCY INSTALLATION

### Django and Project Dependencies

#### Core Dependencies:

**1. Django==4.2**

- Web framework for MVT architecture
- Version 4.2 is LTS (Long-Term Support)
- Stable, well-documented, production-ready

**2. Pillow==10.0.0**

- Python Imaging Library (PIL fork)
- Required for ImageField in Product model
- Handles image uploads and processing

**3. python-decouple==3.8**

- Separates configuration from code
- Manages environment variables
- Keeps secrets out of version control

**4. gunicorn==21.2.0**

- WSGI HTTP Server for production
- Replaces Django's development server
- Better performance and security

**5. whitenoise==6.5.0**

- Serves static files in production
- No need for separate CDN or web server for static files
- Optimized for Django

### Installation Commands:

#### Install Dependencies:

```powershell
# Ensure virtual environment is activated
.venv\Scripts\Activate.ps1

# Install Django and core packages
pip install Django==4.2

# Install image processing
pip install Pillow==10.0.0

# Install configuration management
pip install python-decouple==3.8

# Install production server
pip install gunicorn==21.2.0

# Install static file serving
pip install whitenoise==6.5.0
```

#### Alternative: Install from requirements.txt

```powershell
pip install -r requirements.txt
```

This is faster and ensures exact versions match.

### Generate requirements.txt:

After installing packages, freeze current versions:

```powershell
pip freeze > requirements.txt
```

#### Current requirements.txt Content:

```
Django==4.2
Pillow==10.0.0
python-decouple==3.8
gunicorn==21.2.0
whitenoise==6.5.0
```

### Why Pin Exact Versions?

✅ **Reproducibility:** Same versions across all environments  
✅ **Consistency:** Dev, staging, prod have identical dependencies  
✅ **Stability:** Prevents breaking changes from automatic updates  
✅ **Debugging:** Easier to troubleshoot when versions are known

### Optional Development Dependencies:

For development and testing (not required for deployment):

```powershell
# Code quality
pip install flake8==6.1.0

# Test coverage
pip install coverage==7.3.2

# Debugging
pip install django-debug-toolbar==4.2.0
```

**Note:** These are NOT in requirements.txt because they're development-only tools.

---

## 2.4 PROJECT DIRECTORY STRUCTURE

### Current Structure Verification:

```
C:\Users\Administrator\Downloads\DevOps\
│
├── .venv/                          # Virtual environment (excluded from Git)
│   ├── Scripts/
│   ├── Lib/
│   └── Include/
│
├── ipswich_ecommerce/             # Main Django project
│   ├── __init__.py
│   ├── settings.py                 # Project configuration
│   ├── urls.py                     # URL routing
│   ├── wsgi.py                     # WSGI config for deployment
│   └── asgi.py                     # ASGI config (async)
│
├── products/                       # Products app
│   ├── models.py                   # Category, Product models
│   ├── views.py                    # Product listing, detail views
│   ├── urls.py                     # Product URL patterns
│   ├── admin.py                    # Admin configuration
│   └── migrations/                 # Database migrations
│
├── cart/                          # Shopping cart app
│   ├── models.py                   # Cart, CartItem models
│   ├── views.py                    # Cart operations
│   ├── urls.py                     # Cart URL patterns
│   └── migrations/
│
├── orders/                        # Order management app
│   ├── models.py                   # Order, OrderItem models
│   ├── views.py                    # Order processing
│   ├── urls.py                     # Order URL patterns
│   └── migrations/
│
├── templates/                     # HTML templates
│   ├── base.html                   # Base template
│   ├── home.html                   # Homepage
│   ├── products/
│   │   ├── product_list.html
│   │   └── product_detail.html
│   ├── cart/
│   │   └── cart_detail.html
│   └── orders/
│       ├── create_order.html
│       ├── order_list.html
│       └── order_detail.html
│
├── static/                        # Static files (CSS, JS, images)
│   └── (Bootstrap CDN used, minimal local static files)
│
├── media/                         # User-uploaded files (product images)
│   └── products/
│
├── Assessment 2/                  # Documentation for this assessment
│   ├── 01_PLANNING_DOCUMENTATION.md
│   ├── 02_ENVIRONMENT_SETUP.md (this file)
│   └── SCREENSHOT_CHECKLIST.md
│
├── .github/                       # GitHub-specific files
│   └── workflows/
│       └── django-ci-cd.yml       # CI/CD pipeline
│
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker container config
├── docker-compose.yml            # Multi-container setup
├── .gitignore                    # Git exclusions
├── README.md                     # Project documentation
├── db.sqlite3                    # SQLite database (dev only)
├── tests.py                      # Unit tests
├── populate_db.py                # Sample data script
└── create_superuser.py           # Admin user creation script
```

### Directory Purpose Explanation:

#### Application Code:

- `ipswich_ecommerce/`: Project configuration and settings
- `products/`, `cart/`, `orders/`: Django apps (modular components)
- `templates/`: HTML files using Django template language
- `static/`: CSS, JavaScript, images (served by WhiteNoise in production)
- `media/`: User-uploaded content (product images)

#### DevOps & Configuration:

- `.venv/`: Isolated Python environment
- `.github/workflows/`: CI/CD automation
- `Dockerfile`, `docker-compose.yml`: Containerization
- `requirements.txt`: Dependency management
- `.gitignore`: Version control exclusions

#### Development Tools:

- `manage.py`: Django CLI for running server, migrations, tests
- `tests.py`: Automated test suite
- `populate_db.py`: Creates sample data for testing
- `create_superuser.py`: Creates admin user

#### Documentation:

- `Assessment 2/`: Assignment-specific documentation
- `README.md`: Project setup and usage guide

---

## 2.5 ENVIRONMENT VARIABLES (Optional Enhancement)

### Using python-decouple for Configuration:

#### Create .env file (NOT committed to Git):

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

#### Update settings.py to use decouple:

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='dev-secret-key')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')
```

### Benefits:

✅ Secrets not in version control  
✅ Different configs for dev/prod  
✅ Easy to change without code edits  
✅ More secure

**Note:** For this PoC, we keep it simple without .env file, but in production this would be essential.

---

## 2.6 VERIFICATION CHECKLIST

### Environment Setup Complete:

- [x] Git configured for S315729 account
- [x] Virtual environment created and activated
- [x] Django 4.2 installed
- [x] All dependencies installed (Pillow, decouple, gunicorn, whitenoise)
- [x] requirements.txt generated with pinned versions
- [x] Project directory structure verified
- [x] Ready for Django development

### Next Steps:

1. ✅ Environment setup complete
2. ⏭️ Document Django project structure (models, views, templates)
3. ⏭️ Setup version control (Git, GitHub)
4. ⏭️ Run and document tests
5. ⏭️ Configure CI/CD pipeline

---

## SCREENSHOTS TO TAKE FOR THIS SECTION

### Please capture the following screenshots:

**Screenshot 10:** Git configuration verification

```powershell
git config user.name
git config user.email
```

- Show S315729 and s315729@student.uos.ac.uk output
- Caption: "Figure 10: Git configured for S315729 student account"

**Screenshot 11:** Virtual environment activated

- Terminal showing `(.venv)` prefix
- Caption: "Figure 11: Python virtual environment activated for project isolation"

**Screenshot 12:** pip install output (if reinstalling)

```powershell
pip install Django==4.2 Pillow python-decouple whitenoise gunicorn
```

- Caption: "Figure 12: Installing Django and production dependencies"

**Screenshot 13:** requirements.txt file

- Open requirements.txt in VS Code
- Show all dependencies with versions
- Caption: "Figure 13: Requirements file with all dependencies and versions"

---

## REFLECTION NOTES FOR REPORT

### What I Learned:

**Git Configuration:**

- Local vs global git config matters for multi-account usage
- Essential to verify identity before committing
- Prevents attribution errors in academic submissions

**Virtual Environments:**

- Critical for reproducible Python development
- Isolates dependencies per project
- Industry best practice

**Dependency Management:**

- Pinning versions prevents "works on my machine" issues
- requirements.txt enables automated deployment
- Foundation for Docker containerization

**Project Structure:**

- Django's app-based architecture promotes modularity
- Separation of concerns (MVT pattern)
- Scalable foundation for growth

### Challenges Encountered:

**Initial Challenge:** Remembering to activate virtual environment before pip install

- **Solution:** Always check for `(.venv)` prefix in terminal

**Consideration:** Whether to use .env file for configuration

- **Decision:** Kept simple for PoC, but noted for production enhancement

### DevOps Connection:

This environment setup enables:

- **Consistency:** Same dependencies in dev, CI, and production
- **Automation:** requirements.txt feeds into CI/CD pipeline
- **Reproducibility:** Any developer can recreate environment
- **Isolation:** No conflicts with other projects on same machine

---

**Status:** Environment setup complete! Ready for Django development and Git workflows.
