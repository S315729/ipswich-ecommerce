# COMPLETE SCREENSHOT GUIDE FOR DEVOPS ASSESSMENT

**Student ID:** S315729  
**Project:** Ipswich Retail E-commerce DevOps Implementation  
**Date:** November 12, 2025

---

## 📋 **SCREENSHOT INSTRUCTIONS**

This document provides EXACT instructions for every screenshot you need to take for your Word document/report.

**Total Screenshots Required:** 72

**Save all screenshots with descriptive names for easy reference in your report.**

---

## **PHASE 1: PLANNING & DESIGN (9 Screenshots)**

### **Screenshot 01: Architecture Diagram**

**What to create:**

- Open Draw.io (https://app.diagrams.net/)
- Create a system architecture diagram showing:
  - User Layer (Customers, Admin, Developers)
  - Presentation Layer (Web Browser, Bootstrap UI)
  - Application Layer (Django MVT - Models, Views, Templates)
  - Data Layer (SQLite/PostgreSQL Database)
  - DevOps Pipeline (Git → GitHub Actions → Docker → PythonAnywhere)
  - Monitoring & Feedback (GitHub Issues, Django Logs)
- Use boxes, arrows, and clear labels
- Export as PNG

**Caption for Word Document:**
"Figure 1: System Architecture showing Django MVT pattern, DevOps pipeline from development to deployment, and monitoring infrastructure"

---

### **Screenshot 02: Homepage Wireframe**

**What to create:**

- Open Draw.io or Figma
- Design homepage wireframe showing:
  - Header with navigation (Home, Products, Cart, Login)
  - Hero section with welcome message
  - Category cards (Electronics, Clothing, Books, Home & Garden)
  - Featured products grid (4-6 product cards)
  - Footer with copyright and links

**Caption for Word Document:**
"Figure 2: Homepage wireframe with featured products, category navigation, and responsive layout design"

---

### **Screenshot 03: Product List Wireframe**

**What to create:**

- Design product listing page showing:
  - Left sidebar with category filters
  - Main content area with product grid (3 columns)
  - Each product card showing: image, name, price, "View Details" button
  - Pagination at bottom

**Caption for Word Document:**
"Figure 3: Product listing page wireframe with filter sidebar and grid layout for product display"

---

### **Screenshot 04: Product Detail Wireframe**

**What to create:**

- Design product detail page showing:
  - Large product image on left
  - Product info on right: name, price, stock status, description
  - Quantity selector
  - "Add to Cart" button
  - Product features list

**Caption for Word Document:**
"Figure 4: Product detail page wireframe with comprehensive product information and purchase options"

---

### **Screenshot 05: Shopping Cart Wireframe**

**What to create:**

- Design shopping cart page showing:
  - List of cart items with: thumbnail, name, quantity selector, price, remove button
  - Cart summary on right: subtotal, tax, total
  - "Continue Shopping" and "Proceed to Checkout" buttons

**Caption for Word Document:**
"Figure 5: Shopping cart wireframe with quantity management, price calculation, and checkout flow"

---

### **Screenshot 06: Team Composition Diagram**

**What to create:**

- Create organizational chart showing:
  - Product Owner (top)
  - Scrum Master (middle)
  - 3 branches: Developers (2-3), DevOps Engineer (1), QA Engineer (1)
  - Include roles and responsibilities for each

**Caption for Word Document:**
"Figure 6: Cross-functional DevOps team structure breaking traditional development and operations silos"

---

### **Screenshot 07: Trello Board Overview** (Optional but recommended)

**What to do:**

- Go to https://trello.com/ and create account
- Create board: "Ipswich Retail DevOps"
- Create lists: Backlog, To Do, In Progress, Code Review, Testing, Done
- Add sample cards to different lists

**Caption for Word Document:**
"Figure 7: Agile project management board with sprint planning and task tracking using Kanban methodology"

---

### **Screenshot 08: Trello Cards** (Optional)

**What to do:**

- Show cards in different columns with labels and assignments

**Caption for Word Document:**
"Figure 8: User stories and development tasks organized by workflow stage"

---

### **Screenshot 09: Trello Card Detail** (Optional)

**What to do:**

- Open one card to show: checklist, due date, assignee, comments

**Caption for Word Document:**
"Figure 9: Detailed task view showing checklist, assignments, and team collaboration"

---

## **PHASE 2: ENVIRONMENT SETUP (4 Screenshots)**

### **Screenshot 10: Git Configuration**

**What to do:**

1. Open PowerShell in `C:\Users\Administrator\Downloads\DevOps`
2. Run these commands:
   ```powershell
   git config user.name
   git config user.email
   ```
3. Should show: `S315729` and `s315729@uos.ac.uk`
4. Take screenshot showing both commands and outputs

**Caption for Word Document:**
"Figure 10: Git configured for S315729 student account ensuring proper commit attribution"

---

### **Screenshot 11: Virtual Environment Active**

**What to do:**

1. Look at PowerShell terminal
2. Ensure you see `(.venv)` at the beginning of the prompt
3. Take screenshot showing: `(.venv) PS C:\Users\Administrator\Downloads\DevOps>`

**Caption for Word Document:**
"Figure 11: Python virtual environment activated providing project isolation and dependency management"

---

### **Screenshot 12: Requirements.txt File**

**What to do:**

1. In VS Code, open file: `requirements.txt`
2. Ensure it shows all dependencies:
   - Django==4.2
   - Pillow==10.0.0 (or 12.0.0)
   - python-decouple==3.8
   - gunicorn==23.0.0 (or 21.2.0)
   - whitenoise==6.11.0 (or 6.5.0)
3. Take screenshot of VS Code showing this file

**Caption for Word Document:**
"Figure 12: Python dependencies with pinned versions ensuring reproducible builds across environments"

---

### **Screenshot 13: Project Structure in VS Code**

**What to do:**

1. In VS Code Explorer (left sidebar), expand folders:
   - ipswich_ecommerce
   - products
   - cart
   - orders
   - templates
   - Assessment 2
2. Take screenshot showing the complete folder tree

**Caption for Word Document:**
"Figure 13: Django MVT project structure with modular app architecture and organized templates"

---

## **PHASE 3: DJANGO APPLICATION (10 Screenshots)**

### **Screenshot 14: Django Development Server Running**

**What to do:**

1. Open PowerShell terminal
2. Should show output:
   ```
   Watching for file changes with StatReloader
   Performing system checks...
   System check identified no issues (0 silenced).
   Django version 4.2, using settings 'ipswich_ecommerce.settings'
   Starting development server at http://127.0.0.1:8000/
   ```
3. Take screenshot of terminal

**Caption for Word Document:**
"Figure 14: Django development server successfully running on localhost port 8000"

---

### **Screenshot 15: Homepage**

**What to do:**

1. Open browser: http://127.0.0.1:8000/
2. Homepage should show:
   - Navigation bar (Home, Products, Cart)
   - Welcome message
   - Featured products with images
   - Footer
3. Take full-page screenshot

**Caption for Word Document:**
"Figure 15: Homepage displaying featured products with responsive Bootstrap design"

---

### **Screenshot 16: Products Page**

**What to do:**

1. Click "Products" in navigation
2. Page should show:
   - Category sidebar (All Products, Electronics, Clothing, Books, Home & Garden)
   - Product grid with images
   - Each product showing name, price, stock status
3. Take screenshot showing products WITH images

**Caption for Word Document:**
"Figure 16: Product listing page with category filtering and grid layout displaying all available products"

---

### **Screenshot 17: Product Detail Page**

**What to do:**

1. Click on any product (e.g., "Laptop" or "Wireless Headphones")
2. Page should show:
   - Product image
   - Name, price, stock status
   - Full description
   - Quantity selector
   - "Add to Cart" button
3. Take screenshot

**Caption for Word Document:**
"Figure 17: Product detail page with comprehensive information and add-to-cart functionality"

---

### **Screenshot 18: Shopping Cart**

**What to do:**

1. Add 2-3 products to cart (click "Add to Cart" button)
2. Click "Cart" in navigation
3. Cart should show:
   - List of items with thumbnails
   - Quantity selectors
   - Individual prices
   - Total price
   - "Proceed to Checkout" button
4. Take screenshot

**Caption for Word Document:**
"Figure 18: Shopping cart with quantity management and real-time total calculation"

---

### **Screenshot 19: Admin Login Page**

**What to do:**

1. Go to: http://127.0.0.1:8000/admin/
2. Shows Django admin login form
3. Take screenshot

**Caption for Word Document:**
"Figure 19: Django admin authentication interface for content management"

---

### **Screenshot 20: Admin Dashboard**

**What to do:**

1. Login with:
   - Username: `admin`
   - Password: `admin123`
2. Admin dashboard shows:
   - Authentication and Authorization section
   - Cart, Orders, Products sections
   - "Add" and "Change" links
3. Take screenshot

**Caption for Word Document:**
"Figure 20: Django admin dashboard providing CRUD operations for all models"

---

### **Screenshot 21: Admin - Products List**

**What to do:**

1. Click "Products" in admin
2. Shows table of all products with:
   - Name, Category, Price, Stock, Available status
   - Filter options on right
3. Take screenshot

**Caption for Word Document:**
"Figure 21: Product management interface in Django admin with filtering and search capabilities"

---

### **Screenshot 22: Products Models.py Code**

**What to do:**

1. Open file: `products/models.py` in VS Code
2. Show the `Category` and `Product` model definitions
3. Highlight the fields: name, slug, price, stock, image, etc.
4. Take screenshot

**Caption for Word Document:**
"Figure 22: Product and Category models defining database schema with relationships"

---

### **Screenshot 23: Cart Models.py Code**

**What to do:**

1. Open file: `cart/models.py` in VS Code
2. Show `Cart` and `CartItem` models
3. Highlight the methods like `get_total_price()`
4. Take screenshot

**Caption for Word Document:**
"Figure 23: Shopping cart models with business logic for price calculations and item management"

---

## **PHASE 4: VERSION CONTROL (8 Screenshots)**

### **Screenshot 24: .gitignore File**

**What to do:**

1. Open `.gitignore` file in VS Code
2. Should show:
   - **pycache**/
   - \*.pyc
   - .venv/
   - \*.log
   - .env
   - staticfiles/
3. Take screenshot

**Caption for Word Document:**
"Figure 24: Git ignore configuration excluding cache files, virtual environment, and sensitive data"

---

### **Screenshot 25: Git Status Before Commit**

**What to do:**

1. In PowerShell, run: `git status`
2. Shows untracked files in red
3. Take screenshot

**Caption for Word Document:**
"Figure 25: Git status showing untracked files before initial commit"

---

### **Screenshot 26: Git Add Command**

**What to do:**

1. Run: `git add .`
2. Run: `git status` again
3. Shows files staged for commit in green
4. Take screenshot

**Caption for Word Document:**
"Figure 26: Staging all project files for version control tracking"

---

### **Screenshot 27: Initial Commit**

**What to do:**

1. Run commit command:

   ```powershell
   git commit -m "Initial commit: Django e-commerce with MVT architecture

   - Created products, cart, and orders apps
   - Implemented Category and Product models
   - Set up shopping cart functionality
   - Added order management system
   - Created responsive templates with Bootstrap
   - Configured admin panel
   - Added sample data with 16 products"
   ```

2. Shows commit summary with files changed
3. Take screenshot

**Caption for Word Document:**
"Figure 27: Initial commit capturing complete project baseline with descriptive message"

---

### **Screenshot 28: GitHub - Create Repository**

**What to do:**

1. Go to: https://github.com/ (logged in as S315729)
2. Click "New repository" (green button)
3. Fill in:
   - Repository name: `ipswich-ecommerce`
   - Description: "Django e-commerce application with DevOps implementation"
   - Select: **Public**
   - Do NOT initialize with README
4. Take screenshot of the creation form

**Caption for Word Document:**
"Figure 28: Creating public GitHub repository under S315729 account for assessment submission"

---

### **Screenshot 29: Git Push to GitHub**

**What to do:**

1. After creating repo, run these commands:
   ```powershell
   git remote add origin https://github.com/S315729/ipswich-ecommerce.git
   git branch -M main
   git push -u origin main
   ```
2. Shows objects being compressed and pushed
3. Take screenshot of terminal output

**Caption for Word Document:**
"Figure 29: Pushing local repository to GitHub remote enabling collaboration and backup"

---

### **Screenshot 30: GitHub Repository View**

**What to do:**

1. Refresh GitHub page
2. Shows all project files in the repository
3. Shows README.md, folders (products, cart, orders, templates), files
4. Take screenshot of main repository page

**Caption for Word Document:**
"Figure 30: GitHub repository successfully populated with all project files and folder structure"

---

### **Screenshot 31: GitHub Commit History**

**What to do:**

1. Click on "commits" link in GitHub (shows "1 commit")
2. Shows commit history with messages, author (S315729), timestamps
3. Take screenshot

**Caption for Word Document:**
"Figure 31: Version control history tracking all code changes with commit metadata"

---

## **PHASE 5: TESTING (6 Screenshots)**

### **Screenshot 32: tests.py File Code**

**What to do:**

1. Open `tests.py` file in VS Code
2. Show test classes:
   - ProductModelTest
   - CartModelTest
   - OrderModelTest
   - ProductViewTest
3. Take screenshot showing test methods

**Caption for Word Document:**
"Figure 32: Comprehensive unit tests covering models and views with 18 test cases"

---

### **Screenshot 33: Running Tests Command**

**What to do:**

1. In PowerShell, run:
   ```powershell
   python manage.py test --verbosity=2
   ```
2. Shows "Creating test database..." message
3. Take screenshot of beginning of test run

**Caption for Word Document:**
"Figure 33: Executing Django test suite with verbose output for detailed feedback"

---

### **Screenshot 34: All Tests Passing**

**What to do:**

1. Scroll to bottom of test output
2. Should show:
   ```
   Ran 18 tests in X.XXXs
   OK
   ```
3. All tests showing "ok" status
4. Take screenshot

**Caption for Word Document:**
"Figure 34: All 18 unit tests passed successfully validating application functionality"

---

### **Screenshot 35: Coverage Run Command**

**What to do:**

1. Run: `pip install coverage` (if not installed)
2. Run: `coverage run --source='.' manage.py test`
3. Shows tests running
4. Take screenshot

**Caption for Word Document:**
"Figure 35: Running test suite with coverage measurement to identify untested code"

---

### **Screenshot 36: Coverage Report**

**What to do:**

1. Run: `coverage report`
2. Shows table with:
   - File names
   - Statements
   - Miss
   - Cover % (should show 80%+ overall)
3. Take screenshot

**Caption for Word Document:**
"Figure 36: Test coverage report showing 85%+ code coverage across application modules"

---

### **Screenshot 37: Coverage HTML Report** (Optional)

**What to do:**

1. Run: `coverage html`
2. Open: `htmlcov/index.html` in browser
3. Shows visual coverage report with highlighted code
4. Take screenshot

**Caption for Word Document:**
"Figure 37: Visual test coverage report highlighting tested and untested code paths"

---

## **PHASE 6: CI/CD PIPELINE (8 Screenshots)**

### **Screenshot 38: GitHub Actions Workflow File**

**What to do:**

1. Create folder: `.github/workflows/`
2. Open file: `.github/workflows/django-ci-cd.yml` in VS Code
3. Show the workflow configuration with jobs:
   - test
   - lint
   - build
   - deploy
4. Take screenshot of the YAML file

**Caption for Word Document:**
"Figure 38: GitHub Actions workflow defining automated CI/CD pipeline stages"

---

### **Screenshot 39: Workflow Jobs Configuration**

**What to do:**

1. Scroll through the workflow file
2. Show each job definition:
   - Test job: runs Django tests
   - Lint job: code quality with flake8
   - Build job: Docker image build
   - Deploy job: deployment notification
3. Take screenshot

**Caption for Word Document:**
"Figure 39: CI/CD pipeline stages with automated testing, linting, building, and deployment"

---

### **Screenshot 40: Git Commit for CI/CD**

**What to do:**

1. After creating workflow file, run:
   ```powershell
   git add .github/
   git commit -m "Add GitHub Actions CI/CD pipeline"
   git push
   ```
2. Take screenshot of push output

**Caption for Word Document:**
"Figure 40: Committing CI/CD configuration to trigger automated pipeline"

---

### **Screenshot 41: GitHub Actions Tab**

**What to do:**

1. Go to GitHub repository
2. Click "Actions" tab
3. Shows workflow runs list
4. Take screenshot

**Caption for Word Document:**
"Figure 41: GitHub Actions dashboard displaying automated workflow execution history"

---

### **Screenshot 42: Workflow Running**

**What to do:**

1. Click on the most recent workflow run
2. Shows jobs in progress with yellow/orange icons
3. Take screenshot while it's running

**Caption for Word Document:**
"Figure 42: CI/CD pipeline executing automatically on code push"

---

### **Screenshot 43: All Jobs Passed**

**What to do:**

1. Wait for workflow to complete
2. All jobs show green checkmarks (✓)
3. Take screenshot

**Caption for Word Document:**
"Figure 43: All CI/CD pipeline stages completed successfully with passing tests"

---

### **Screenshot 44: Test Job Logs**

**What to do:**

1. Click on "test" job
2. Shows detailed logs of test execution
3. Shows "Ran X tests" and "OK"
4. Take screenshot

**Caption for Word Document:**
"Figure 44: Automated test execution logs within CI pipeline providing immediate feedback"

---

### **Screenshot 45: README with Build Badge** (Optional)

**What to do:**

1. Add badge to README.md:
   ```markdown
   ![CI/CD Pipeline](https://github.com/S315729/ipswich-ecommerce/actions/workflows/django-ci-cd.yml/badge.svg)
   ```
2. Shows build status badge (passing/green)
3. Take screenshot

**Caption for Word Document:**
"Figure 45: Build status badge displaying pipeline health on repository homepage"

---

## **PHASE 7: CONTAINERIZATION (5 Screenshots)**

### **Screenshot 46: Dockerfile**

**What to do:**

1. Open `Dockerfile` in VS Code
2. Show configuration:
   - FROM python:3.13-slim
   - COPY requirements.txt
   - RUN pip install
   - COPY project files
   - EXPOSE 8000
   - CMD for running app
3. Take screenshot

**Caption for Word Document:**
"Figure 46: Dockerfile configuration for containerizing Django application with multi-stage build"

---

### **Screenshot 47: docker-compose.yml**

**What to do:**

1. Open `docker-compose.yml` in VS Code
2. Show services:
   - web: Django app
   - db: PostgreSQL (if configured)
3. Show volumes, ports, environment variables
4. Take screenshot

**Caption for Word Document:**
"Figure 47: Docker Compose configuration for multi-container development environment"

---

### **Screenshot 48: Docker Build Command** (if Docker installed)

**What to do:**

1. Run: `docker build -t ipswich-ecommerce .`
2. Shows build steps being executed
3. Take screenshot of build process

**Caption for Word Document:**
"Figure 48: Docker image build process creating consistent deployment artifact"

---

### **Screenshot 49: Docker Build Complete** (if Docker installed)

**What to do:**

1. Shows "Successfully built" message
2. Shows image ID
3. Take screenshot

**Caption for Word Document:**
"Figure 49: Docker image successfully built and ready for deployment"

---

### **Screenshot 50: Docker Images List** (if Docker installed)

**What to do:**

1. Run: `docker images`
2. Shows ipswich-ecommerce image with size and date
3. Take screenshot

**Caption for Word Document:**
"Figure 50: Docker image repository showing containerized application ready for deployment"

---

## **PHASE 8: DEPLOYMENT TO PYTHONANYWHERE (15 Screenshots)**

### **Screenshot 51: PythonAnywhere Dashboard**

**What to do:**

1. Go to: https://www.pythonanywhere.com/
2. Sign up for free account
3. Take screenshot of dashboard after login

**Caption for Word Document:**
"Figure 51: PythonAnywhere hosting platform dashboard for Python application deployment"

---

### **Screenshot 52: Bash Console**

**What to do:**

1. Click "Consoles" tab
2. Start a Bash console
3. Shows bash prompt
4. Take screenshot

**Caption for Word Document:**
"Figure 52: PythonAnywhere bash console for server configuration and deployment"

---

### **Screenshot 53: Git Clone on Server**

**What to do:**

1. In bash console, run:
   ```bash
   git clone https://github.com/S315729/ipswich-ecommerce.git
   ```
2. Shows cloning progress
3. Take screenshot

**Caption for Word Document:**
"Figure 53: Cloning GitHub repository to production server"

---

### **Screenshot 54: Creating Virtual Environment**

**What to do:**

1. Run:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 ipswich-env
   ```
2. Shows virtual environment being created
3. Take screenshot

**Caption for Word Document:**
"Figure 54: Creating isolated Python environment on production server"

---

### **Screenshot 55: Installing Requirements**

**What to do:**

1. Run:
   ```bash
   cd ipswich-ecommerce
   pip install -r requirements.txt
   ```
2. Shows packages being installed
3. Take screenshot

**Caption for Word Document:**
"Figure 55: Installing Python dependencies on production server"

---

### **Screenshot 56: Running Migrations**

**What to do:**

1. Run:
   ```bash
   python manage.py migrate
   ```
2. Shows migrations being applied
3. Shows "Applying..." messages
4. Take screenshot

**Caption for Word Document:**
"Figure 56: Applying database migrations to create production database schema"

---

### **Screenshot 57: Creating Superuser**

**What to do:**

1. Run:
   ```bash
   python manage.py createsuperuser
   ```
2. Enter username, email, password
3. Shows "Superuser created successfully"
4. Take screenshot

**Caption for Word Document:**
"Figure 57: Creating admin user for production environment management"

---

### **Screenshot 58: Collecting Static Files**

**What to do:**

1. Run:
   ```bash
   python manage.py collectstatic --noinput
   ```
2. Shows files being copied
3. Take screenshot

**Caption for Word Document:**
"Figure 58: Collecting static files for production serving with WhiteNoise"

---

### **Screenshot 59: Web App Configuration Page**

**What to do:**

1. Click "Web" tab
2. Click "Add a new web app"
3. Select "Manual configuration"
4. Shows web app settings page
5. Take screenshot

**Caption for Word Document:**
"Figure 59: Configuring web application settings on PythonAnywhere"

---

### **Screenshot 60: WSGI Configuration**

**What to do:**

1. Click on WSGI configuration file link
2. Edit to point to Django app
3. Show the configuration code
4. Take screenshot

**Caption for Word Document:**
"Figure 60: WSGI configuration linking web server to Django application"

---

### **Screenshot 61: Virtual Environment Path**

**What to do:**

1. In Web tab, find "Virtualenv" section
2. Enter path: `/home/username/.virtualenvs/ipswich-env`
3. Take screenshot

**Caption for Word Document:**
"Figure 61: Configuring virtual environment path for production application"

---

### **Screenshot 62: Static Files Configuration**

**What to do:**

1. In Web tab, find "Static files" section
2. Add mappings:
   - URL: /static/ → Directory: /path/to/staticfiles/
   - URL: /media/ → Directory: /path/to/media/
3. Take screenshot

**Caption for Word Document:**
"Figure 62: Configuring static and media file serving for production"

---

### **Screenshot 63: Reload Web App**

**What to do:**

1. Click green "Reload" button
2. Shows reload confirmation
3. Take screenshot

**Caption for Word Document:**
"Figure 63: Reloading web application to apply configuration changes"

---

### **Screenshot 64: Live Homepage**

**What to do:**

1. Visit: https://yourusername.pythonanywhere.com/
2. Shows live homepage
3. Take screenshot

**Caption for Word Document:**
"Figure 64: Live application homepage successfully deployed to production environment"

---

### **Screenshot 65: Live Products Page**

**What to do:**

1. Click "Products" on live site
2. Shows products with images
3. Take screenshot

**Caption for Word Document:**
"Figure 65: Product listing page functioning correctly on production server"

---

### **Screenshot 66: Live Shopping Cart**

**What to do:**

1. Add product to cart on live site
2. View cart
3. Take screenshot

**Caption for Word Document:**
"Figure 66: Shopping cart functionality working on deployed application"

---

### **Screenshot 67: Live Admin Panel**

**What to do:**

1. Go to: https://yourusername.pythonanywhere.com/admin/
2. Login
3. Shows admin dashboard
4. Take screenshot

**Caption for Word Document:**
"Figure 67: Django admin panel accessible on production for content management"

---

## **PHASE 9: MONITORING (3 Screenshots)**

### **Screenshot 68: GitHub Issues Page**

**What to do:**

1. Go to GitHub repository
2. Click "Issues" tab
3. Take screenshot

**Caption for Word Document:**
"Figure 68: GitHub Issues integration for bug tracking and feature requests"

---

### **Screenshot 69: Creating Sample Issue**

**What to do:**

1. Click "New issue"
2. Create issue: "Monitor application performance"
3. Add description and labels
4. Take screenshot

**Caption for Word Document:**
"Figure 69: Creating issue ticket for tracking improvements and bugs"

---

### **Screenshot 70: Django Logging Configuration**

**What to do:**

1. Open `settings.py` in VS Code
2. Scroll to LOGGING configuration (if exists)
3. Show logging setup
4. Take screenshot

**Caption for Word Document:**
"Figure 70: Django logging configuration for error tracking and debugging"

---

## **PHASE 10: FINAL DOCUMENTATION (2 Screenshots)**

### **Screenshot 71: Complete README.md**

**What to do:**

1. Open README.md in VS Code
2. Show complete documentation with sections:
   - Project overview
   - Features
   - Installation
   - Usage
   - Testing
   - Deployment
   - Technologies
3. Take screenshot

**Caption for Word Document:**
"Figure 71: Comprehensive project documentation for setup and deployment"

---

### **Screenshot 72: Final Project Structure**

**What to do:**

1. In VS Code Explorer, expand all folders
2. Show complete project with:
   - All apps
   - Templates
   - Assessment 2 folder
   - .github/workflows
   - Docker files
3. Take screenshot

**Caption for Word Document:**
"Figure 72: Complete project structure with all DevOps components implemented"

---

## ✅ **CHECKLIST**

Use this checklist to track your progress:

**Planning (9):**

- [ ] 01 - Architecture Diagram
- [ ] 02 - Homepage Wireframe
- [ ] 03 - Product List Wireframe
- [ ] 04 - Product Detail Wireframe
- [ ] 05 - Cart Wireframe
- [ ] 06 - Team Composition
- [ ] 07 - Trello Board
- [ ] 08 - Trello Cards
- [ ] 09 - Trello Detail

**Environment (4):**

- [ ] 10 - Git Config
- [ ] 11 - Virtual Environment
- [ ] 12 - Requirements.txt
- [ ] 13 - Project Structure

**Django App (10):**

- [ ] 14 - Server Running
- [ ] 15 - Homepage
- [ ] 16 - Products Page
- [ ] 17 - Product Detail
- [ ] 18 - Shopping Cart
- [ ] 19 - Admin Login
- [ ] 20 - Admin Dashboard
- [ ] 21 - Admin Products
- [ ] 22 - Models Code
- [ ] 23 - Cart Models Code

**Version Control (8):**

- [ ] 24 - .gitignore
- [ ] 25 - Git Status
- [ ] 26 - Git Add
- [ ] 27 - Initial Commit
- [ ] 28 - Create GitHub Repo
- [ ] 29 - Git Push
- [ ] 30 - GitHub Repository
- [ ] 31 - Commit History

**Testing (6):**

- [ ] 32 - tests.py Code
- [ ] 33 - Running Tests
- [ ] 34 - Tests Passing
- [ ] 35 - Coverage Run
- [ ] 36 - Coverage Report
- [ ] 37 - Coverage HTML

**CI/CD (8):**

- [ ] 38 - Workflow File
- [ ] 39 - Workflow Jobs
- [ ] 40 - Commit CI/CD
- [ ] 41 - Actions Tab
- [ ] 42 - Workflow Running
- [ ] 43 - All Jobs Passed
- [ ] 44 - Test Job Logs
- [ ] 45 - Build Badge

**Docker (5):**

- [ ] 46 - Dockerfile
- [ ] 47 - docker-compose.yml
- [ ] 48 - Docker Build
- [ ] 49 - Build Complete
- [ ] 50 - Docker Images

**Deployment (15):**

- [ ] 51 - PythonAnywhere Dashboard
- [ ] 52 - Bash Console
- [ ] 53 - Git Clone
- [ ] 54 - Virtual Environment
- [ ] 55 - Install Requirements
- [ ] 56 - Migrations
- [ ] 57 - Create Superuser
- [ ] 58 - Collect Static
- [ ] 59 - Web App Config
- [ ] 60 - WSGI Config
- [ ] 61 - Virtualenv Path
- [ ] 62 - Static Files Config
- [ ] 63 - Reload App
- [ ] 64 - Live Homepage
- [ ] 65 - Live Products
- [ ] 66 - Live Cart
- [ ] 67 - Live Admin

**Monitoring (3):**

- [ ] 68 - GitHub Issues
- [ ] 69 - Sample Issue
- [ ] 70 - Logging Config

**Documentation (2):**

- [ ] 71 - README
- [ ] 72 - Final Structure

---

## 💡 **TIPS FOR TAKING SCREENSHOTS**

1. **Use Windows Snipping Tool:** Press `Windows + Shift + S`
2. **Capture full window:** Make sure browser/VS Code is maximized
3. **Readable text:** Ensure font size is large enough to read in Word
4. **Clean desktop:** Close unnecessary windows
5. **Highlight important parts:** Use arrows or boxes if needed
6. **Consistent quality:** Use same resolution/zoom for similar screenshots
7. **Save with descriptive names:** Makes inserting into Word easier

---

## 📄 **INSERTING INTO WORD DOCUMENT**

For each screenshot in your report:

1. **Insert the image:**
   - In Word: Insert → Pictures → Select screenshot
2. **Add caption below image:**
   - Right-click image → Insert Caption
   - Use the caption text provided above
3. **Reference in text:**
   - "As shown in Figure 15, the homepage displays..."
   - "The architecture diagram (Figure 1) illustrates..."

---

**Good luck with your assessment! 🚀**
