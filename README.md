# Bank Branch API 🏦

A Django REST API for Indian bank branch data deployed on Render.

## Features
- REST endpoints for bank/branch information
- PostgreSQL database support
- Bulk CSV data import
- Optimized queries with `select_related`

## Project Structure
bankapi/
├── branches/
│ ├── management/commands/import_banks.py
│ ├── migrations/
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── bankapi/
│ ├── settings.py
│ └── urls.py
├── build.sh
├── requirements.txt
└── runtime.txt


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
1.Connect GitHub repo to Render

2.Auto-deploy via render.yaml

3.Monitor via Render dashboard logs
