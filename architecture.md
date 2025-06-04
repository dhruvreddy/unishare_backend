## Architecture

```markdown
.
├── architecture.md
├── main.py
├── models
│   ├── __init__.py
│   ├── base_model.py
│   ├── post_model.py
│   ├── subscription_model.py
│   └── user_model.py
├── README.md
├── repositories
│   ├── __init__.py
│   ├── auth_repository.py
│   ├── post_repository.py
│   └── user_repository.py
├── requirments.txt
├── routers
│   ├── __init__.py
│   ├── post.py
│   └── token.py
├── schemas
│   ├── __init__.py
│   ├── post_return_schemas.py
│   ├── post_schema.py
│   ├── subscription_schema.py
│   └── user_schema.py
└── utils
    ├── __init__.py
    ├── database.py
    ├── get_env.py
    ├── password_hash.py
    └── token.py

6 directories, 26 files
```