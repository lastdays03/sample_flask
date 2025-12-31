"""
인증 블루프린트 설정.

로그인, 회원가입, 로그아웃 등 사용자 인증과 관련된 라우트 및 관련 기능을 포함합니다.
"""
from flask import Blueprint

auth = Blueprint("auth", __name__)

from . import views

