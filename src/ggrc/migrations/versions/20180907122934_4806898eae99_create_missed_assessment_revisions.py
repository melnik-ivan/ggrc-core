# Copyright (C) 2018 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

"""
Create missed Assessment Revisions

Create Date: 2018-09-07 12:29:34.476813
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

from alembic import op

# revision identifiers, used by Alembic.
revision = '4806898eae99'
down_revision = '82db77ebdf55'


def upgrade():
  """Upgrade database schema and/or data, creating a new revision."""
  QUERY = (
      """
      INSERT INTO objects_without_revisions
        SELECT assessment_id, "Assessment", "created"  FROM (
          SELECT assessments.id AS assessment_id, revisions.id,
          revisions.resource_id, revisions.resource_type
          FROM assessments LEFT JOIN revisions ON
            revisions.resource_id = assessments.id
            AND revisions.resource_type = "Assessment"
        ) AS assessments_revisions WHERE resource_id IS NULL;
      """
  )
  op.execute(QUERY)


def downgrade():
  """Downgrade database schema and/or data back to the previous revision."""
