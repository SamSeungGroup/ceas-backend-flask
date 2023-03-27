from flask import Blueprint, send_file, request

from modules.comment_db import get_comments
from modules.word_cloud import get_word_cloud

import os

bp = Blueprint('word-cloud', __name__, url_prefix='/word-cloud')

@bp.route('/<int:product_id>', methods=["GET", "DELETE"])
def comments(product_id):
    file_name = f'images\wordcloud{product_id}.jpeg'
    if request.method == "GET":
        result = get_comments(product_id)
        if not result.get("comments"):
            return {"error": "No comments exist"}
        else:
            total_string = ""
            for comment in result['comments']:
                total_string += comment[0]
            word_cloud = get_word_cloud(total_string)

            if not os.path.isdir("ceas\images"):
                os.mkdir("ceas\images")
            word_cloud.to_file(f'ceas/{file_name}')

        return send_file(file_name, mimetype='image/jpeg')
    if request.method == "DELETE":
        if os.path.isfile(f'ceas/{file_name}'):
            os.remove(f'ceas/{file_name}')
            return "1"
        else:
            return "0"