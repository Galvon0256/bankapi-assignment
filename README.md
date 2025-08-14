# Bank Branch API 🏦

A Django REST API for Indian bank branch data deployed on Render.

## Features
- REST endpoints for bank/branch information
- PostgreSQL database support
- Bulk CSV data import
- Optimized queries with `select_related`

## Project Structure
``bankapi-assignment/
│
├── bankapi/                       # Django project root
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                # Production config with Render settings
│   ├── urls.py                    # Main URL routing
│   └── wsgi.py
│
├── branches/                      # Main app
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                  # Bank & Branch models
│   ├── serializers.py             # DRF serializers
│   ├── tests.py                   # API test cases
│   ├── urls.py                    # App-specific routes
│   ├── views.py                   # API view classes
│   │
│   └── management/
│       └── commands/
│           ├── __init__.py
│           └── import_banks.py    # Custom CSV import command
│
├── data/                          # Sample data (not in repo)
│   ├── bank_branches.csv
│   └── banks.csv
│
├── .env                           # Local environment vars (ignored)
├── .gitignore
├── build.sh                       # Render deployment script
├── manage.py
├── README.md
├── requirements.txt               # Dependencies
└── runtime.txt                    # Python version for Render
``

## Key Development Challenges & Solutions

### 1. Data Import Issues
**Problem**: `UNIQUE constraint failed` on IFSC codes  
**Fix**:
```python
# In import_banks.py
with transaction.atomic():
    Branch.objects.all().delete()  # Clear existing data
    # ... bulk create logic ...
```

### 2. Security
Generated 50+ character SECRET_KEY using:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

API Endpoints

`GET /banks/` - List all banks

`GET /branches/<ifsc>/` - Branch details

`GET /banks/<id>/branches/` - Filter by bank

## Deployment

1. Connect GitHub repo to Render

2. Auto-deploy via render.yaml

3. Monitor via Render dashboard logs
