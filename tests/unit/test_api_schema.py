from marshmallow import Schema, fields
import pytest

def test_schema_definition():
    """Marshmallow 스키마 정의 테스트"""
    class TestSchema(Schema):
        id = fields.Int(dump_only=True)
        name = fields.Str(required=True)

    schema = TestSchema()
    data = {"name": "test"}
    result = schema.load(data)
    assert result["name"] == "test"

    with pytest.raises(Exception): # marshmallow.exceptions.ValidationError but checking general exception first
        schema.load({})

# 향후 flask-smorest 의존성이 추가되면 Api 객체 테스트 추가
