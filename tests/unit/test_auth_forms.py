import pytest


# This import is expected to fail initially
try:
    from app.auth.forms import LoginForm, RegistrationForm
except ImportError:
    LoginForm = None
    RegistrationForm = None


def test_login_form_import():
    """LoginForm 임포트 테스트.
    
    LoginForm 클래스가 정상적으로 임포트되는지 확인합니다.
    """
    assert LoginForm is not None, "LoginForm could not be imported"


def test_registration_form_import():
    """RegistrationForm 임포트 테스트.
    
    RegistrationForm 클래스가 정상적으로 임포트되는지 확인합니다.
    """
    assert RegistrationForm is not None, "RegistrationForm could not be imported"


def test_login_form_validation(app):
    """LoginForm 유효성 검사 로직 테스트.
    
    필수 필드 누락 및 잘못된 이메일 형식에 대해
    검증 실패가 발생하는지 확인합니다.
    """
    if LoginForm is None:
        pytest.fail("LoginForm not imported")

    with app.test_request_context():
        # Empty form
        form = LoginForm(data={})
        assert form.validate() is False
        assert "email" in form.errors
        assert "password" in form.errors

        # Invalid email
        form = LoginForm(data={"email": "invalid-email", "password": "password"})
        assert form.validate() is False
        assert "email" in form.errors


def test_registration_form_validation(app):
    """RegistrationForm 유효성 검사 로직 테스트.
    
    비밀번호와 비밀번호 확인 필드가 일치하지 않을 때
    검증 실패가 발생하는지 확인합니다.
    """
    if RegistrationForm is None:
        pytest.fail("RegistrationForm not imported")

    with app.test_request_context():
        # Passwords mismatch
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "password",
            "confirm_password": "mismatch",
        }
        form = RegistrationForm(data=data)
        assert form.validate() is False
        assert "password" in form.errors
