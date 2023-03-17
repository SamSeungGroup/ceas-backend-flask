from flask import Blueprint

from modules.comment_db import get_content, get_comment_positive, set_comment_positive
from modules.ceas_comment_sentiment_anlaysis import comment_sentiment_analysis

bp = Blueprint('comments', __name__, url_prefix='/comment-positive')

@bp.route('/<int:comment_id>')
def comment_positive(comment_id):
    comment_content = get_content(comment_id)
    comment_positive = comment_sentiment_analysis(comment_content['content'])
    set_comment_positive(comment_id, comment_positive['comment_positive'])
    return get_comment_positive(comment_id)