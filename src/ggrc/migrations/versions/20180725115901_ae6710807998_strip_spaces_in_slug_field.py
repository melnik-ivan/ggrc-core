# Copyright (C) 2018 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

"""
strip spaces in slug field

Create Date: 2018-07-25 11:59:01.282407
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name


from alembic import op

from ggrc.migrations.utils.strip_text_field import strip_spaces_ensure_uniq

# revision identifiers, used by Alembic.
revision = 'ae6710807998'
down_revision = '20ca15a10d12'


def upgrade():
  """Upgrade database schema and/or data, creating a new revision."""
  tables_with_slug = {
      'access_groups', 'assessment_templates', 'assessments', 'audits',
      'clauses', 'controls', 'cycle_task_group_object_tasks',
      'cycle_task_groups', 'cycles', 'data_assets', 'directives', 'documents',
      'evidence', 'facilities', 'issues', 'markets', 'metrics', 'objectives',
      'org_groups', 'products', 'programs', 'projects', 'risk_assessments',
      'risks', 'sections', 'systems', 'task_group_tasks', 'task_groups',
      'threats', 'vendors', 'workflows',
  }
  connection = op.get_bind()
  tables_in_current_db = set(
      table[0] for table in connection.execute("SHOW TABLES")
      if table[0] in tables_with_slug
  )
  strip_spaces_ensure_uniq(tables_in_current_db, 'slug', tables_in_current_db)


def downgrade():
  """Downgrade database schema and/or data back to the previous revision."""
  pass
