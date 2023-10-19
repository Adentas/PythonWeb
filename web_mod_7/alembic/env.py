from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from your_application.models import Base

# ...

def run_migrations_online():
    # Інші налаштування...
    
    target_metadata = Base.metadata

    config = context.config
    config.set_main_option('sqlalchemy.url', 'sqlite:///university.db')  # Вказати правильний URL для вашої бази даних SQLite

    with context.begin_transaction():
        context.run_migrations(engine_name='your_engine_name', target='head')

# ...
