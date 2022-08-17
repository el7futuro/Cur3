import json

class CommentsDao:

    def __init__(self, path):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path = path


    def load_comments(self):
        """ Загружает данные из файла и возвращает обычный list"""
        with open(self.path, "r", encoding="utf-8") as file:
            comments_list = json.load(file)
        return comments_list


    def get_comments(self):
        """ Возвращает список всех постов"""
        comments = self.load_comments()
        return comments

    def get_comments_by_post_id(self, post_id):  # возвращает комментарии определенного поста.
        # Функция должна вызывать ошибку `ValueError` если такого поста нет и пустой список, если у поста нет комментов.
        try:
            comments_by_post_id = []
            for i in self.get_comments():
                if post_id == i['post_id']:
                    comments_by_post_id.append(i)

            return comments_by_post_id

        except ValueError:
            return f'Нет такого поста'