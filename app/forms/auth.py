"""
Created by Liangraorao on 2019/8/5 21:32
 __author__  : Liangraorao
filename : auth.py
"""
from wtforms import Form, StringField, validators, PasswordField
from wtforms.validators import ValidationError, DataRequired, Length, Email
from app.model.user import User

class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'), Length(6,32)])
    nickname = StringField(validators=[DataRequired(), Length(2, 10 ,message='昵称至少需要两个字符，最多10个汉字')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已存在')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])