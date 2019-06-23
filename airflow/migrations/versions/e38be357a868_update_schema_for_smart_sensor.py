#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""update schema for smart sensor

Revision ID: e38be357a868
Revises: 939bb1e647c8
Create Date: 2019-06-07 04:03:17.003939

"""
from alembic import op
import sqlalchemy as sa
import dill


# revision identifiers, used by Alembic.
revision = 'e38be357a868'
down_revision = '939bb1e647c8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('task_instance', sa.Column('attr_dict', sa.Text(), nullable=True))
    op.add_column('task_instance', sa.Column('hashcode', sa.BigInteger(), nullable=True))
    op.add_column('task_instance', sa.Column('shardcode', sa.Integer(), nullable=True))

    op.create_index('ti_hashcode', 'task_instance', ['hashcode'], unique=False)
    op.create_index('ti_shardcode', 'task_instance', ['shardcode'], unique=False)


def downgrade():
    op.drop_index('ti_hashcode', table_name='task_instance')
    op.drop_index('ti_shardcode', table_name='task_instance')

    op.drop_column('task_instance', 'attr_dict')
    op.drop_column('task_instance', 'hashcode')
    op.drop_column('task_instance', 'shardcode')

