"""alter table user

Revision ID: f0512ef1cad9
Revises: 
Create Date: 2025-10-24 10:58:15.916550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0512ef1cad9'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    ALTER TABLE users
    ADD COLUMN userType varchar(100) DEFAULT 'student'
""")
    pass 


def downgrade() -> None:
    op.execute("""ALTER TABLE users
    DROP COLUMN userType
""")
    pass