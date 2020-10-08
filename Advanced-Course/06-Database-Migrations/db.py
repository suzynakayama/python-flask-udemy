from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# op.f - https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.f
# importance of naming constraints - https://alembic.sqlalchemy.org/en/latest/naming.html
# Docs: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#using-custom-metadata-and-naming-conventions
convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s__%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
