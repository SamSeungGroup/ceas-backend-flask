from flask      import current_app
from sqlalchemy import text
import math

def get_content(comment_id):
    with current_app.database.connect() as conn:
        stmt = text("""
            SELECT
                content
            FROM comment
            WHERE id = :comment_id
        """).params(comment_id = comment_id)
        comment_content = conn.execute(stmt).fetchone()
        return {
            'content': comment_content[0]
            }

def get_comment_positive(comment_id):
    with current_app.database.connect() as conn:
        stmt = text("""
            SELECT
                comment_positive
            FROM comment
            WHERE id = :comment_id
        """).params(comment_id = comment_id)
        comment_positive = conn.execute(stmt).fetchone()
        return {
                'comment_positive': comment_positive[0]
            }

def set_comment_positive(comment_id, comment_positive):
    with current_app.database.connect() as conn:
        stmt = text("""
            UPDATE
                comment
            SET
                comment_positive = :comment_positive
            WHERE id = :comment_id
        """).params(comment_id = comment_id, comment_positive = comment_positive)
        conn.execute(stmt)
        conn.commit()

def get_comments(product_id):
    with current_app.database.connect() as conn:
        stmt = text("""
            SELECT
                content
            FROM comment
            WHERE product_id = :product_id
        """).params(product_id = product_id)
        comments = conn.execute(stmt).fetchall()
        return {
                'comments': comments
            }