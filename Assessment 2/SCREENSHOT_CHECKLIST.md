# SCREENSHOT CHECKLIST FOR DEVOPS ASSESSMENT

**Student ID:** S315729  
**Project:** Ipswich Retail E-commerce DevOps Implementation  
**Deadline:** November 14, 2025 @ 12:00 noon

---

## ORGANIZATION STRUCTURE

Save all screenshots in: `Assessment 2/screenshots/`

Naming convention: `##_description.png` (e.g., `01_architecture_diagram.png`)

---

## PHASE 1: PLANNING (Screenshots 01-09)

### Architecture & Design

- [ ] **01_architecture_diagram.png** - Complete system architecture from Draw.io

  - Caption: "Figure 1: System Architecture showing MVT pattern, DevOps pipeline, and deployment"

- [ ] **02_wireframe_homepage.png** - Homepage wireframe

  - Caption: "Figure 2: Homepage wireframe with featured products and categories"

- [ ] **03_wireframe_products.png** - Product list page wireframe

  - Caption: "Figure 3: Product listing page with filter options"

- [ ] **04_wireframe_product_detail.png** - Product detail wireframe

  - Caption: "Figure 4: Product detail page showing specifications and add to cart"

- [ ] **05_wireframe_cart.png** - Shopping cart wireframe
  - Caption: "Figure 5: Shopping cart with quantity management and checkout"

### Team & Project Management

- [ ] **06_team_composition.png** - Team structure diagram

  - Caption: "Figure 6: Cross-functional DevOps team breaking traditional silos"

- [ ] **07_trello_board_overview.png** - Trello board with all columns

  - Caption: "Figure 7: Agile project management board with sprint planning"

- [ ] **08_trello_cards.png** - Sample cards in different columns

  - Caption: "Figure 8: User stories and tasks organized by workflow stage"

- [ ] **09_trello_card_detail.png** - Detailed card view
  - Caption: "Figure 9: Task detail showing checklist, assignee, and comments"

---

## PHASE 2: ENVIRONMENT SETUP (Screenshots 10-13)

### Git Configuration

- [ ] **10_git_config.png** - Terminal showing git config for S315729 account

  - Command: `git config user.name` and `git config user.email`
  - Caption: "Figure 10: Git configured for S315729 student account (not PC login)"

- [ ] **11_virtual_environment.png** - Activated Python virtual environment
  - Command: `.venv\Scripts\activate`
  - Caption: "Figure 11: Python virtual environment activated for project isolation"

### Dependency Installation

- [ ] **12_pip_install.png** - pip install output showing Django and packages

  - Command: `pip install Django==4.2 Pillow python-decouple whitenoise gunicorn`
  - Caption: "Figure 12: Installing Django and production dependencies"

- [ ] **13_requirements_txt.png** - Generated requirements.txt file
  - Command: `pip freeze > requirements.txt`
  - Caption: "Figure 13: Requirements file with all dependencies and versions"

---

## PHASE 3: DJANGO PROJECT STRUCTURE (Screenshots 14-20)

### Project Files

- [ ] **14_project_structure.png** - VS Code Explorer showing complete file structure

  - Caption: "Figure 14: Django MVT project structure with three apps"

- [ ] **15_products_models.png** - products/models.py code

  - Caption: "Figure 15: Product and Category models with relationships"

- [ ] **16_cart_models.png** - cart/models.py code

  - Caption: "Figure 16: Cart and CartItem models for shopping functionality"

- [ ] **17_orders_models.png** - orders/models.py code
  - Caption: "Figure 17: Order and OrderItem models for order management"

### Local Development

- [ ] **18_runserver_terminal.png** - Terminal showing `python manage.py runserver` output

  - Caption: "Figure 18: Django development server running on localhost:8000"

- [ ] **19_homepage_local.png** - Browser showing homepage at http://127.0.0.1:8000/

  - Caption: "Figure 19: Homepage with featured products and navigation"

- [ ] **20_products_page_local.png** - Products listing page

  - Caption: "Figure 20: Product listing with grid layout and categories"

- [ ] **21_product_detail_local.png** - Individual product detail page

  - Caption: "Figure 21: Product detail showing price, stock, and add to cart"

- [ ] **22_cart_page_local.png** - Shopping cart page

  - Caption: "Figure 22: Shopping cart with quantity adjustment and total calculation"

- [ ] **23_admin_panel.png** - Django admin at http://127.0.0.1:8000/admin/

  - Caption: "Figure 23: Django admin panel for content management"

- [ ] **24_admin_products.png** - Admin products list
  - Caption: "Figure 24: Managing products through Django admin interface"

---

## PHASE 4: VERSION CONTROL (Screenshots 25-30)

### Git Repository

- [ ] **25_gitignore.png** - .gitignore file content

  - Caption: "Figure 25: Git ignore file excluding cache, database, and environment files"

- [ ] **26_git_status.png** - Terminal showing `git status` before commit

  - Caption: "Figure 26: Git status showing tracked and untracked files"

- [ ] **27_initial_commit.png** - Terminal showing first commit
  - Command: `git add .` and `git commit -m "message"`
  - Caption: "Figure 27: Initial commit with descriptive message"

### GitHub Repository

- [ ] **28_github_create_repo.png** - GitHub new repository page

  - Caption: "Figure 28: Creating public GitHub repository for S315729 account"

- [ ] **29_git_push.png** - Terminal showing git push output

  - Command: `git push -u origin main`
  - Caption: "Figure 29: Pushing local repository to GitHub remote"

- [ ] **30_github_repo_view.png** - GitHub repository showing files

  - Caption: "Figure 30: GitHub repository with all project files visible"

- [ ] **31_commit_history.png** - GitHub commits page
  - Caption: "Figure 31: Commit history showing development progression"

---

## PHASE 5: TESTING (Screenshots 32-36)

### Test Code

- [ ] **32_tests_py_code.png** - tests.py file showing test cases
  - Caption: "Figure 32: Unit tests for models and views (18 test cases)"

### Test Execution

- [ ] **33_running_tests.png** - Terminal showing `python manage.py test --verbosity=2`

  - Caption: "Figure 33: Running Django test suite with verbose output"

- [ ] **34_tests_passing.png** - Terminal showing all tests passed
  - Caption: "Figure 34: All 18 tests passed successfully"

### Coverage Report

- [ ] **35_coverage_run.png** - Terminal showing `coverage run` command

  - Caption: "Figure 35: Running tests with coverage measurement"

- [ ] **36_coverage_report.png** - Terminal showing `coverage report` output

  - Caption: "Figure 36: Test coverage report showing 85%+ coverage"

- [ ] **37_coverage_html.png** - HTML coverage report in browser (optional)
  - Caption: "Figure 37: Visual coverage report highlighting tested code"

---

## PHASE 6: CI/CD PIPELINE (Screenshots 38-44)

### GitHub Actions Workflow

- [ ] **38_workflow_yml.png** - .github/workflows/django-ci-cd.yml file

  - Caption: "Figure 38: GitHub Actions workflow configuration for CI/CD"

- [ ] **39_workflow_jobs.png** - Workflow file showing test, lint, build, deploy jobs
  - Caption: "Figure 39: CI/CD pipeline stages with automated testing and deployment"

### Pipeline Execution

- [ ] **40_actions_tab.png** - GitHub Actions tab showing workflow runs

  - Caption: "Figure 40: GitHub Actions dashboard with pipeline history"

- [ ] **41_workflow_running.png** - Workflow in progress with yellow icons

  - Caption: "Figure 41: CI/CD pipeline running automatically on git push"

- [ ] **42_all_jobs_passed.png** - All jobs completed with green checkmarks

  - Caption: "Figure 42: All CI/CD pipeline stages passed successfully"

- [ ] **43_test_job_logs.png** - Test job detailed logs

  - Caption: "Figure 43: Automated test execution logs in CI pipeline"

- [ ] **44_build_badge.png** - README with build status badge
  - Caption: "Figure 44: Build status badge showing pipeline health"

---

## PHASE 7: CONTAINERIZATION (Screenshots 45-49)

### Docker Configuration

- [ ] **45_dockerfile.png** - Dockerfile content

  - Caption: "Figure 45: Dockerfile with multi-stage build for Django app"

- [ ] **46_docker_compose.png** - docker-compose.yml file
  - Caption: "Figure 46: Docker Compose configuration with app and database services"

### Docker Build (if available)

- [ ] **47_docker_build_start.png** - Terminal showing `docker build` starting

  - Caption: "Figure 47: Docker image build process initiated"

- [ ] **48_docker_build_complete.png** - Docker build completed successfully

  - Caption: "Figure 48: Docker image built successfully"

- [ ] **49_docker_images.png** - Terminal showing `docker images` list
  - Caption: "Figure 49: Docker image available for deployment"

---

## PHASE 8: DEPLOYMENT (Screenshots 50-60)

### PythonAnywhere Setup

- [ ] **50_pythonanywhere_dashboard.png** - PythonAnywhere dashboard

  - Caption: "Figure 50: PythonAnywhere free hosting platform dashboard"

- [ ] **51_bash_console.png** - Bash console in PythonAnywhere

  - Caption: "Figure 51: PythonAnywhere bash console for server configuration"

- [ ] **52_git_clone_pythonanywhere.png** - Git clone command on server

  - Command: `git clone https://github.com/S315729/ipswich-ecommerce.git`
  - Caption: "Figure 52: Cloning GitHub repository to production server"

- [ ] **53_virtualenv_create.png** - Creating virtual environment on server

  - Command: `mkvirtualenv --python=/usr/bin/python3.10 ipswich-env`
  - Caption: "Figure 53: Creating Python virtual environment on server"

- [ ] **54_pip_install_server.png** - Installing requirements on server

  - Command: `pip install -r requirements.txt`
  - Caption: "Figure 54: Installing dependencies on production server"

- [ ] **55_migrations.png** - Running database migrations

  - Command: `python manage.py migrate`
  - Caption: "Figure 55: Database migrations applied on production"

- [ ] **56_collectstatic.png** - Collecting static files

  - Command: `python manage.py collectstatic --noinput`
  - Caption: "Figure 56: Static files collected for production serving"

- [ ] **57_wsgi_config.png** - WSGI configuration file

  - Caption: "Figure 57: WSGI configuration linking Django app to web server"

- [ ] **58_web_app_config.png** - PythonAnywhere web app configuration page

  - Caption: "Figure 58: Web app settings with virtual environment and paths"

- [ ] **59_reload_web_app.png** - Reload button and confirmation
  - Caption: "Figure 59: Reloading web app to apply changes"

### Live Application

- [ ] **60_live_homepage.png** - Live site homepage

  - URL: https://yourusername.pythonanywhere.com/
  - Caption: "Figure 60: Live homepage deployed to production"

- [ ] **61_live_products.png** - Live products page

  - Caption: "Figure 61: Product listing on live production site"

- [ ] **62_live_product_detail.png** - Live product detail

  - Caption: "Figure 62: Product detail page with working add to cart"

- [ ] **63_live_cart.png** - Live shopping cart

  - Caption: "Figure 63: Shopping cart functionality on production"

- [ ] **64_live_admin.png** - Live admin panel

  - Caption: "Figure 64: Django admin accessible on production server"

- [ ] **65_live_order_confirmation.png** - Order placed successfully
  - Caption: "Figure 65: Order confirmation page showing successful transaction"

---

## PHASE 9: MONITORING (Screenshots 66-68)

### Issue Tracking

- [ ] **66_github_issues.png** - GitHub Issues tab

  - Caption: "Figure 66: GitHub Issues for bug tracking and feature requests"

- [ ] **67_sample_issue.png** - Created issue example
  - Caption: "Figure 67: Sample issue created for tracking improvements"

### Logging

- [ ] **68_django_logging.png** - Django logging configuration in settings.py

  - Caption: "Figure 68: Logging configuration for error tracking"

- [ ] **69_pythonanywhere_logs.png** - PythonAnywhere error logs
  - Caption: "Figure 69: Production error logs accessible in hosting dashboard"

---

## PHASE 10: DOCUMENTATION (Screenshots 70-72)

- [ ] **70_readme_complete.png** - Complete README.md file

  - Caption: "Figure 70: Comprehensive README with setup and deployment instructions"

- [ ] **71_readme_rendered.png** - README as rendered on GitHub

  - Caption: "Figure 71: README displaying properly on GitHub repository"

- [ ] **72_project_overview.png** - Full project structure final view
  - Caption: "Figure 72: Complete project file structure with all DevOps components"

---

## SUMMARY

**Total Screenshots Required:** 72  
**Organized into 10 Phases:** Planning through Documentation

### Screenshot Storage:

```
Assessment 2/
├── screenshots/
│   ├── 01_architecture_diagram.png
│   ├── 02_wireframe_homepage.png
│   ├── ...
│   └── 72_project_overview.png
└── SCREENSHOT_CHECKLIST.md (this file)
```

### Quality Guidelines:

- Resolution: At least 1920x1080 or high quality
- Include relevant context (URL bar, terminal prompt, file names)
- Highlight important sections if needed
- Clear, readable text
- Full window captures preferred over partial

### For Report:

- Insert screenshots in order throughout report
- Add figure captions below each image
- Reference figures in text: "As shown in Figure 12..."
- Ensure screenshots support your narrative
- Don't rely solely on screenshots - explain them in text

---

**Status:** Checklist created. Take screenshots during each implementation phase.

**Note:** You'll be prompted to take specific screenshots as we progress through each step. Keep this checklist handy!
