from flask import Blueprint, jsonify
import logging

logging.basicConfig(filename='api.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s', encoding='utf-8')

from app.posts.views import posts_dao

bluepint_api = Blueprint("bluepint_api", __name__)

@bluepint_api.route("/api/posts")
def get_posts():
    posts = posts_dao.get_posts_all()
    logging.info("Запрос /api/posts")
    return jsonify(posts)


@bluepint_api.route("/api/posts/<int:pk>")
def get_posts_by_pk(pk):
    post = posts_dao.get_post_by_pk(pk)
    logging.info(f"Запрос /api/posts/{pk}")
    return jsonify(post)