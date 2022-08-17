from flask import Blueprint, render_template, send_from_directory, request
from app.posts.dao.posts_dao import PostsDao
from app.posts.dao.comments_dao import CommentsDao
import os

DATA_PATH_POSTS = os.path.join("data", "data.json")
DATA_PATH_COMMENT = os.path.join("data", "comments.json")

# Создаем блупринт
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")


# Создаем DAO
posts_dao = PostsDao(DATA_PATH_POSTS)
comments_dao = CommentsDao(DATA_PATH_COMMENT)


# Создаем вьюшку для ленты
@posts_blueprint.route('/')
def index_page():
    posts = posts_dao.get_posts_all()
    return render_template("index.html", posts=posts)


@posts_blueprint.route("/posts/<int:pk>")
def post_page(pk):
    post = posts_dao.get_post_by_pk(pk)
    comments = comments_dao.get_comments_by_post_id(pk)
    comments_len = len(comments)
    return render_template("post.html", post=post, comments=comments, comments_len=comments_len)


@posts_blueprint.route("/search/")
def page_search():

    result = request.args.get("s")
    posts = posts_dao.search_for_posts(result)

    if posts:

        return render_template('search.html', posts=posts)
    return f"Вы ничего не ввели или слова такого нет"


@posts_blueprint.route("/users/<username>")
def user_page(username):
    posts = posts_dao.get_post_by_username(username)
    return render_template("user-feed.html", posts=posts, username=username)



@posts_blueprint.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

