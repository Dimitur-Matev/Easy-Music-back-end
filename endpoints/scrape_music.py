from models import Article, ArticleLink
from svc import Service


from flask import jsonify, make_response, request
from flask_restx import Resource, fields

ns = Service().get_ns()

scrape = Service().api.model('scrape_music', {
    'article_link_id': fields.Integer(required=True, example=1)
})


@ns.route('/getMusic')
class ScrapeMusic(Resource):

    @ns.expect(scrape, validate=True)
    def get(self):
        
