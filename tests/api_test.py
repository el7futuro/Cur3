from app.posts.views import DATA_PATH_POSTS
import main
import pytest

key_list = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
            "pk"}
class Test_api:

    @pytest.fixture
    def app_instance(self):
        app = main.app
        app.config["DATA_PATH_POSTS"] = DATA_PATH_POSTS
        test_client = app.test_client()

        return test_client

    def test_post_page(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        assert result.status_code == 200, "неправильный статус "
        assert type(result.json) == list, "неверный тип данных"


    def test_page_post_pk(self, app_instance):
        result = app_instance.get("/api/posts/2", follow_redirects=True)
        assert result.status_code == 200
        assert type(result.json) == dict, "неверный тип данных"


    # def test_api_post(self, get_post_all):
    #     response = app.test_client().get('/api/posts/<pk>')
    #
    #     assert isinstance(response.json, dict) is True
    #     assert set(response[0].keys()) == keys_should_be