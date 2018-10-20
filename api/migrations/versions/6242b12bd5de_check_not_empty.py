"""check not empty

Revision ID: 6242b12bd5de
Revises: 224160d5991e
Create Date: 2018-10-20 17:37:06.284677

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import column, func


# revision identifiers, used by Alembic.
revision = '6242b12bd5de'
down_revision = '224160d5991e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_check_constraint('ck_question_body_len',
                               'question',
                               func.length(column('body')) > 0)

    op.create_check_constraint('ck_question_title_len',
                               'question',
                               func.length(column('title')) > 0)

    op.create_check_constraint('ck_question_user_len',
                               'question',
                               func.length(column('user')) > 0)

    op.create_check_constraint('ck_answer_body_len',
                               'answer',
                               func.length(column('body')) > 0)

    op.create_check_constraint('ck_answer_user_len',
                               'answer',
                               func.length(column('user')) > 0)

    op.create_check_constraint('ck_vote_user_len',
                               'vote',
                               func.length(column('user')) > 0)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('ck_question_body_len', 'question')

    op.drop_constraint('ck_question_title_len', 'question')

    op.drop_constraint('ck_question_user_len', 'question')

    op.drop_constraint('ck_answer_body_len', 'answer')

    op.drop_constraint('ck_answer_user_len', 'answer')

    op.drop_constraint('ck_vote_user_len', 'vote')
    # ### end Alembic commands ###