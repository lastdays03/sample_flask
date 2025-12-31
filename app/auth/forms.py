from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class LoginForm(FlaskForm):
    """로그인 폼.
    
    사용자 이메일과 비밀번호를 입력받아 로그인을 처리합니다.
    """
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Log In")


class RegistrationForm(FlaskForm):
    """회원가입 폼.
    
    새로운 사용자 등록을 위해 필요한 정보를 입력받습니다.
    (이메일, 사용자명, 비밀번호, 비밀번호 확인)
    """
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(1, 64),
            Regexp("^[A-Za-z][A-Za-z0-9_.]*$", 0, "Usernames must have only letters, numbers, dots or underscores"),
        ],
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), EqualTo("confirm_password", message="Passwords must match")]
    )
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Register")

