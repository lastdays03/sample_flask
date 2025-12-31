from . import auth
from app import db
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.exceptions import BusinessException
from app.utils import error_response


@auth.route("/login", methods=["GET", "POST"])
def login():
    """로그인 라우트.
    
    GET: 로그인 폼을 렌더링합니다.
    POST: 폼 데이터를 검증하고 사용자 인증을 처리합니다.
    
    성공 시 'next' 파라미터가 있으면 해당 페이지로, 없으면 메인 인덱스로 리다이렉트합니다.
    실패 시 BusinessException을 발생시킵니다 (API 클라이언트 대응).
    
    Returns:
        str|Response: 렌더링된 템플릿(GET) 또는 리다이렉트 응답(POST 성공), 또는 에러 응답(실패 시).
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(request.args.get("next") or url_for("main.index"))
        raise BusinessException("Invalid email or password.")
    
    if request.is_json and form.errors:
        return error_response("Validation Error", 400, payload=form.errors)

    return render_template("auth/login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    """회원가입 라우트.
    
    GET: 회원가입 폼을 렌더링합니다.
    POST: 사용자 입력을 검증하고 새로운 사용자를 생성합니다.
    
    성공 시 로그인 페이지로 리다이렉트합니다.
    실패 시 BusinessException을 발생시킵니다.
    
    Returns:
        str|Response: 렌더링된 템플릿(GET) 또는 리다이렉트 응답(POST 성공).
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            raise BusinessException("Email already registered.")

        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You can now login.")
        return redirect(url_for("auth.login"))
    
    if request.is_json and form.errors:
        return error_response("Validation Error", 400, payload=form.errors)

    return render_template("auth/register.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    """로그아웃 라우트.
    
    현재 사용자를 로그아웃 처리하고 세션을 정리합니다.
    
    Returns:
        Response: 메인 인덱스로 리다이렉트.
    """
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("main.index"))

