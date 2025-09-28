import os

ENV = os.getenv("ENV", "dev").lower()

if ENV == "dev":
    from .dev import config
elif ENV == "stage":
    from .stage import config
elif ENV == "prod":
    from .prod import config
else:
    raise ValueError(f"Unknown ENV: {ENV}")
