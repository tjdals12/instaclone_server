from flask_restful import Resource
from models.Post import Post


class SampleList(Resource):
    def get(self):
        posts = Post.query.all()

        return [post.to_dict() for post in posts]


class Sample(Resource):
    def get(self, id):
        post = Post.query.get(id)

        return post.to_dict()
