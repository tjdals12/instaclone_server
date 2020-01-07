from flask import Blueprint
from flask_restful import Api
from controllers.sample_controller import SampleList, Sample

sample_blueprint = Blueprint("sample", __name__, url_prefix="/samples")
sample_blueprint_api = Api(sample_blueprint)

sample_blueprint_api.add_resource(SampleList, "/")
sample_blueprint_api.add_resource(Sample, "/<int:id>")
