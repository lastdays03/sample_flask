import pytest
from app.models import User


def test_password_setter():
    """비밀번호 설정 테스트.
    
    비밀번호를 설정하면 해시값이 생성되어 저장되는지 확인합니다.
    """
    u = User(password="cat")
    assert u.password_hash is not None


def test_no_password_getter():
    """비밀번호 읽기 방지 테스트.
    
    password 속성을 읽으려 할 때 AttributeError가 발생하는지 확인합니다.
    (비밀번호는 해시로만 저장되며 평문으로 접근 불가해야 함)
    """
    u = User(password="cat")
    with pytest.raises(AttributeError):
        u.password


def test_password_verification():
    """비밀번호 검증 테스트.
    
    verify_password 메서드가 올바른 비밀번호에는 True, 
    틀린 비밀번호에는 False를 반환하는지 확인합니다.
    """
    u = User(password="cat")
    assert u.verify_password("cat")
    assert not u.verify_password("dog")


def test_password_salts_are_random():
    """솔트(Salt) 무작위성 테스트.
    
    같은 비밀번호라도 서로 다른 사용자 객체(다른 시점 생성)에서는
    서로 다른 해시값을 가져야 함을 확인합니다 (솔트 사용 확인).
    """
    u = User(password="cat")
    u2 = User(password="cat")
    assert u.password_hash != u2.password_hash

