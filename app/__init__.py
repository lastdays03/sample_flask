from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app(config_name="default"):
    """Flask 애플리케이션 팩토리 함수.
    
    지정된 설정 이름을 기반으로 Flask 애플리케이션을 생성하고 초기화합니다.
    데이터베이스, 마이그레이션, 로그인 매니저 및 로깅 설정을 수행하고
    블루프린트를 등록합니다.

    Args:
        config_name (str): 적용할 설정 구성의 이름 (기본값: "default").

    Returns:
        Flask: 설정이 완료된 Flask 애플리케이션 인스턴스.
    """

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # 로깅 설정
    import logging
    from logging.handlers import RotatingFileHandler
    import os

    if not app.debug and not app.testing:
        if not os.path.exists("logs"):
            os.mkdir("logs")
        file_handler = RotatingFileHandler("logs/antigravity.log", maxBytes=10240, backupCount=10)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]")
        )
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info("Antigravity startup")

    # 개발/테스트 환경에서도 로그가 콘솔에 출력되도록 보장합니다
    # (Flask 기본 설정이 이를 처리하지만, 필요시 명시적으로 설정 가능)
    # 현재는 운영 환경 유사 모드에서의 파일 로깅이 핵심입니다.

    from app import models

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .errors import errors as errors_blueprint

    app.register_blueprint(errors_blueprint)

    return app
