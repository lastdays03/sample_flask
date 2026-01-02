from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields

# API Blueprint 정의
api_bp = Blueprint("example_api", "example_api", url_prefix="/example", description="Example API Operations")

# Schema 정의
class MockItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

# In-memory database
items = []

@api_bp.route("/")
class ItemList(MethodView):
    @api_bp.response(200, MockItemSchema(many=True))
    def get(self):
        """List items"""
        return items

    @api_bp.arguments(MockItemSchema)
    @api_bp.response(201, MockItemSchema)
    def post(self, new_item):
        """Add a new item"""
        item_id = len(items) + 1
        new_item["id"] = item_id
        items.append(new_item)
        return new_item
