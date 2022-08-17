import os
import pytest
from app.posts.dao.posts_dao import PostsDao



class TestPostDao:

    @pytest.fixture
    def posts_dao(self):
        posts_dao = PostsDao(os.path.join("data", "data.json"))
        return posts_dao



    def test_get_all_types(self, posts_dao):
        posts = posts_dao.get_posts_all()
        assert type(posts) == list, "возвращается не список"

    def test_get_by_pk(self, posts_dao):
        posts = posts_dao.get_posts_all()
        pk_list = {1, 2, 3, 4, 5, 6, 7, 8}
        pk = set([post["pk"] for post in posts])
        assert pk == pk_list, "Не совпадает получение pk"

    def test_search(self, posts_dao):
        posts = posts_dao.search_for_posts("тарелка")
        assert type(posts) == list, "Вернулся не список"

