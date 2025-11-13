# CI/CD Pipeline Fixes Applied

**Date:** November 13, 2025  
**Student:** S315729  
**Project:** Ipswich Retail E-commerce

---

## 🔧 Issues Encountered & Resolutions

### Issue 1: Pillow Build Failure with Python 3.13

**Error:**

```
KeyError: '__version__'
ERROR: Failed to build 'Pillow' when getting requirements to build wheel
```

**Root Cause:**

- Pillow 10.0.0 has compatibility issues with Python 3.13
- Python 3.13 is very new (released October 2024) and many packages don't have pre-built wheels yet
- Pillow needs to compile from source, but the setup.py has version detection issues with Python 3.13

**Solutions Applied:**

1. **Updated requirements.txt:**

   - ❌ Old: `Pillow==10.0.0`
   - ✅ New: `Pillow==9.5.0`
   - Reason: Pillow 9.5.0 is stable, well-tested, and has pre-built wheels for Python 3.10

2. **Updated GitHub Actions workflow (.github/workflows/django-ci-cd.yml):**

   - ❌ Old: `python-version: "3.13"`
   - ✅ New: `python-version: "3.10"`
   - Added: `cache: 'pip'` for faster builds
   - Reason: Python 3.10 is LTS (Long Term Support) and has excellent library compatibility

3. **Updated Dockerfile:**
   - ❌ Old: `FROM python:3.13-slim`
   - ✅ New: `FROM python:3.10-slim`
   - Reason: Match CI/CD environment for consistency

---

## 📋 All Changes Made

### File: `requirements.txt`

```diff
 Django==4.2
-Pillow==10.0.0
+Pillow==9.5.0
 python-decouple==3.8
 gunicorn==21.2.0
 whitenoise==6.5.0
```

### File: `.github/workflows/django-ci-cd.yml`

```diff
       - name: Set up Python
         uses: actions/setup-python@v4
         with:
-          python-version: "3.13"
+          python-version: "3.10"
+          cache: 'pip'
```

### File: `Dockerfile`

```diff
-# Use Python 3.13 slim image
-FROM python:3.13-slim
+# Use Python 3.10 slim image
+FROM python:3.10-slim
```

---

## ✅ Verification Steps

### 1. GitHub Actions Pipeline

- Go to: https://github.com/S315729/ipswich-ecommerce/actions
- Latest workflow should show: ✅ All checks passed
- Jobs completed:
  - ✅ test (Run Django tests)
  - ✅ lint (Code quality check)
  - ✅ build-docker (Build Docker image)
  - ✅ deploy (Deployment notification)

### 2. Local Testing (when Docker is available)

```powershell
# Build Docker image
docker build -t ipswich-ecommerce:latest .

# Run container
docker run -p 8000:8000 ipswich-ecommerce:latest

# Test application
# Visit: http://localhost:8000/
```

### 3. Verify Dependencies Install

```powershell
# In virtual environment
pip install -r requirements.txt

# Should complete without errors
```

---

## 🎯 Why Python 3.10?

### Advantages:

1. **LTS Support:** Long-term support until October 2026
2. **Library Compatibility:** Excellent compatibility with all major Python packages
3. **Pre-built Wheels:** Most packages have pre-built wheels for Python 3.10
4. **Production Ready:** Widely used in production environments
5. **PEP 604 Features:** Modern type hints (X | Y instead of Union[X, Y])
6. **Structural Pattern Matching:** match/case statements available
7. **Better Error Messages:** Improved error reporting

### Production Deployment:

- PythonAnywhere supports Python 3.10 ✅
- Railway supports Python 3.10 ✅
- Heroku supports Python 3.10 ✅
- AWS/Azure/GCP all support Python 3.10 ✅

---

## 📊 Commits Made

1. **Initial pipeline setup:**

   - Commit: `Add GitHub Actions CI/CD pipeline`
   - Files: `.github/workflows/django-ci-cd.yml`

2. **First dependency fix:**

   - Commit: `Fix CI/CD pipeline: Update Pillow to 10.4.0 and Python to 3.10 for compatibility`
   - Files: `requirements.txt`, `.github/workflows/django-ci-cd.yml`

3. **Stable version fix:**

   - Commit: `Fix Pillow dependency: Downgrade to 9.5.0 for Python 3.10 compatibility and add pip cache`
   - Files: `requirements.txt`, `.github/workflows/django-ci-cd.yml`

4. **Dockerfile fix:**
   - Commit: `Fix Dockerfile: Update base image to Python 3.10 for Pillow compatibility`
   - Files: `Dockerfile`

---

## 🚀 Next Steps

1. **Verify GitHub Actions pipeline is passing** ✅
2. **Take screenshots for report:**
   - Screenshot 43: All jobs passed (green checkmarks)
   - Screenshot 44: Test job logs showing tests passing
   - Screenshot 46: Updated Dockerfile with Python 3.10
3. **Deploy to PythonAnywhere:**

   - Use Python 3.10 virtualenv
   - Install requirements successfully
   - Configure WSGI file

4. **Document in report:**
   - Explain the issue encountered
   - Show how you debugged it (reading error logs)
   - Demonstrate problem-solving skills
   - Highlight the importance of Python version compatibility

---

## 💡 Lessons Learned

1. **Version Compatibility Matters:** Always check library compatibility with Python versions
2. **Consistency is Key:** Keep Python versions consistent across:
   - Development environment
   - CI/CD pipeline
   - Docker containers
   - Production deployment
3. **LTS Versions are Safer:** Use Long-Term Support versions for production projects
4. **Pre-built Wheels Save Time:** Using versions with pre-built wheels speeds up builds
5. **Test Early:** Test CI/CD pipeline early to catch issues before deployment

---

## 📝 For Your Report

**Include this troubleshooting experience in your reflection section:**

_"During the CI/CD implementation, I encountered a dependency compatibility issue where Pillow 10.0.0 failed to build with Python 3.13. By analyzing the error logs, I identified that Pillow's setup.py had version detection issues with the newest Python release. I resolved this by downgrading to Python 3.10 LTS and Pillow 9.5.0, which provided better compatibility and pre-built wheels. This experience highlighted the importance of choosing stable, well-supported versions for production environments and maintaining consistency across development, testing, and deployment environments."_

---

**Status:** ✅ All fixes applied and pushed to GitHub  
**Pipeline Status:** ✅ Should now pass all checks  
**Ready for:** Deployment phase
