from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    """사용자 모델.
    
    사용자 정보를 저장하고 인증 관련 기능을 제공합니다.
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(256))

    @property
    def password(self):
        """비밀번호 속성 접근자.
        
        비밀번호는 읽을 수 없는 속성임을 알립니다.
        
        Raises:
            AttributeError: 비밀번호를 읽으려 할 때 발생합니다.
        """
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        """비밀번호 설정자.
        
        비밀번호를 해시화하여 저장합니다.
        
        Args:
            password (str): 평문 비밀번호.
        """
        self.password_hash = generate_password_hash(password, method="pbkdf2:sha256")

    def verify_password(self, password):
        """비밀번호 검증.
        
        입력된 비밀번호가 저장된 해시와 일치하는지 확인합니다.
        
        Args:
            password (str): 검증할 평문 비밀번호.
            
        Returns:
            bool: 비밀번호가 일치하면 True, 그렇지 않으면 False.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User %r>" % self.username


from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    """사용자 로더 콜백.
    
    Flask-Login이 세션에서 사용자 ID를 통해 사용자 객체를 로드할 때 호출됩니다.
    
    Args:
        user_id (str): 사용자 ID (유니코드 문자열).
        
    Returns:
        User: 해당 ID를 가진 사용자 객체, 또는 없으면 None.
    """
    return User.query.get(int(user_id))

