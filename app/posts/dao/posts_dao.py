import json


class PostsDao:

    def __init__(self, path):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path = path


    def load_posts(self):
        """ Загружает данные из файла и возвращает обычный list"""
        with open(self.path, "r", encoding="utf-8") as file:
            posts_list = json.load(file)
        return posts_list

    def get_posts_all(self):
        """ Возвращает список всех постов"""
        posts = self.load_posts()
        return posts


    def search_for_posts(self, query): # возвращает список постов по ключевому слову
        posts_by_tag = []
        for i in self.get_posts_all():
            if query in i['content']:
                posts_by_tag.append(i)

        return posts_by_tag


    def get_post_by_pk(self, pk): #возвращает один пост по его идентификатору.

        for post in self.get_posts_all():
            if pk == post['pk']:
                break

        return post


    def get_post_by_username(self, username): #возвращает один пост по автору.
        posts_by_username = []
        for i in self.get_posts_all():
            if username == i['poster_name']:
                posts_by_username.append(i)


        return posts_by_username