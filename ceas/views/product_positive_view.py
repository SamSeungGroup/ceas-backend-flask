from flask import Blueprint

from modules.comment_db import get_comments_positive, set_product_positive, get_product_positive

bp = Blueprint('products', __name__, url_prefix='/product-positive')

@bp.route('/<int:product_id>')
def comments_positive(product_id):
    positive_list = get_comments_positive(product_id)
    set_product_positive(product_id, positive_list)
    return get_product_positive(product_id)