from flask import Blueprint, render_template, request, jsonify, current_app
from flask_wtf.csrf import CSRFError
from app.exceptions import CoreException
from app.utils import error_response

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(CSRFError)
def handle_csrf_error(error):
    """CSRF 토큰 누락 또는 불일치 에러 처리.

    Args:
        error (CSRFError): 발생한 CSRF 에러.

    Returns:
        tuple[Response|str, int]: JSON 응답 또는 HTML 템플릿과 400 상태 코드.
    """
    if request.path.startswith("/api/") or request.is_json:
        return error_response(error.description, 400)
    return render_template("errors/core_error.html", error=error), 400


@errors.app_errorhandler(CoreException)
def handle_core_exception(error):
    """애플리케이션 정의 예외(CoreException) 처리.

    비즈니스 에러와 시스템 에러를 구분하여 처리합니다.

    Args:
        error (CoreException): 발생한 커스텀 예외.

    Returns:
        tuple[Response|str, int]: JSON 응답 또는 HTML 템플릿과 적절한 상태 코드.
    """
    current_app.logger.error(f"CoreException caught: {error.message} (Code: {error.code})")

    # 요청에 따라 JSON 또는 HTML 응답 결정
    if request.path.startswith("/api/") or request.is_json:
        return error_response(error.message, 400 if error.code == "BUSINESS_ERROR" else 500, payload=error.payload)

    # 에러 템플릿 렌더링
    return render_template("errors/core_error.html", error=error), 400 if error.code == "BUSINESS_ERROR" else 500


@errors.app_errorhandler(404)
def not_found_error(error):
    """404 Not Found 에러 처리.

    Args:
        error: 발생한 404 에러.

    Returns:
        tuple[Response|str, int]: JSON 응답 또는 404 HTML 템플릿과 404 상태 코드.
    """
    if request.path.startswith("/api/") or request.is_json:
        return error_response("Not Found", 404)
    return render_template("errors/404.html"), 404


@errors.app_errorhandler(500)
def internal_error(error):
    """500 Internal Server Error 처리.

    DB 세션을 롤백하고 에러 응답을 반환합니다.

    Args:
        error: 발생한 500 에러.

    Returns:
        tuple[Response|str, int]: JSON 응답 또는 500 HTML 템플릿과 500 상태 코드.
    """
    from app import db

    db.session.rollback()

    if request.path.startswith("/api/") or request.is_json:
        return error_response("Internal Server Error", 500)
    return render_template("errors/500.html"), 500

