from flask      import current_app
from sqlalchemy import text

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
    
def get_comments_positive(product_id):
    with current_app.database.connect() as conn:
        stmt = text("""
            SELECT
                comment_positive 
            FROM comment
            WHERE product_id = :product_id
        """).params(product_id = product_id)
        positive_list = conn.execute(stmt).fetchall()
        result = [positive[0] for positive in positive_list]
        return result

def set_product_positive(product_id, positive_list):
    total_positive = sum(positive_list)
    product_positive = total_positive/len(positive_list)
    with current_app.database.connect() as conn:
        stmt = text("""
            UPDATE
                product
            SET
                product_positive = :product_positive
            WHERE id = :product_id
        """).params(product_id = product_id, product_positive = product_positive)
        conn.execute(stmt)
        conn.commit()

def get_product_positive(product_id):
    with current_app.database.connect() as conn:
        stmt = text("""
            SELECT
                product_positive
            FROM product
            WHERE id = :product_id
        """).params(product_id = product_id)
        product_positive = conn.execute(stmt).fetchone()
        print(product_positive)
        return {
                'product_positive': product_positive[0]
            }