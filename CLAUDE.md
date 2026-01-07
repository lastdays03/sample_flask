# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Educational/template Flask web application demonstrating best practices for standardized development workflows and AI agent collaboration patterns. This is a reference implementation, not a production application.

**Tech Stack**: Flask 2.x, SQLAlchemy ORM, Flask-Login, flask-smorest (OpenAPI), Marshmallow, Flask-Talisman, pytest

## Common Commands

```bash
# Development
make all           # Run format + lint + coverage in sequence
make test          # Run all tests
make lint          # Check code style (flake8)
make format        # Auto-format code (black)
make coverage      # Run tests with coverage report

# Testing specific
python -m pytest tests/unit              # Unit tests only
python -m pytest tests/integration       # Integration tests only
python -m pytest -v                      # Verbose output

# Database migrations
flask db migrate -m "message"            # Create migration
flask db upgrade                         # Apply migrations

# Running
flask run                                # Development server (port 5000)
```

## Architecture

### Application Factory Pattern
Entry point: `app/__init__.py::create_app(config_name="default")`

### Blueprint Organization
- **Auth Blueprint** (`/auth`): Login, register, logout routes
- **Main Blueprint** (`/`): Dashboard and data APIs (district, building, predict)
- **API Blueprints** (`/api`): flask-smorest REST APIs (example, health)
- **Errors Blueprint**: 404, 500, CSRF, CoreException handlers

### Exception Hierarchy
```
CoreException (base)
├── BusinessException → HTTP 400 (user-facing logical errors)
└── SystemException → HTTP 500 (infrastructure errors)
```

### Response Format
```python
# Use helpers from app/utils/__init__.py
success_response(data, message=None)  # {"status": "success", "data": {...}}
error_response(message, payload=None) # {"status": "error", "message": "..."}
```

### Request Processing Flow
Request → RequestIDMiddleware (X-Request-ID) → Blueprint Router → View Handler → Error Handlers (if needed) → Response with Request ID

### Security Layers
- CSRF: Flask-WTF tokens in forms
- CSP: Flask-Talisman headers
- Rate Limiting: flask-limiter (200 req/day default)
- Password: PBKDF2-SHA256 hashing

## Code Conventions

- **Variables/Functions**: English `snake_case`
- **Classes**: English `PascalCase`
- **Docstrings**: Google Style format (Korean descriptions accepted)
- **Line Length**: 120 characters (Black and Flake8 configured)

## Testing

Tests are organized in `tests/unit/` and `tests/integration/`. Use fixtures from `conftest.py`:
- `app`: Flask app in testing mode
- `client`: HTTP test client
- `runner`: CLI command runner

Test database uses in-memory SQLite with CSRF disabled.

## Git Conventions

- **Commit Messages**: Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`)
- **Branch Naming**: `feature/{issue-number}-{description}`

## Key Files

- `config.py`: Environment configs (Development, Testing, Production)
- `app/models.py`: SQLAlchemy models (User with Flask-Login UserMixin)
- `app/exceptions.py`: Custom exception classes
- `app/utils/logging.py`: Request ID middleware and logging filters
- `docs/architecture.md`: System architecture diagrams