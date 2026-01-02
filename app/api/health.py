from flask.views import MethodView
from flask_smorest import Blueprint

blp = Blueprint('health', 'health', url_prefix='/health', description='Health Check')

@blp.route('')
class HealthCheck(MethodView):
    def get(self):
        """Health check endpoint
        
        Returns the health status of the application.
        """
        return {"status": "ok", "version": "1.0.0"}
