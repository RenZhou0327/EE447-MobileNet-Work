from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


# 搜索表单
class SearchForm(FlaskForm):
    searchInput = StringField(
        label='名称',
        validators=[
            DataRequired()
        ],
        description='搜索关键词',
        render_kw={
            "type": "search",
            "placeholder": "Search",
            "class": "form-item",
            "id": "searchInput",
            "value": "",
            "size": "30",
            "maxlength": "80",
            "required": "required"
        }
    )
    submit = SubmitField(
        "Submit",
        render_kw={
            "class": "btn btn-primary",
            "type": "submit",
            "id": "submit"
        }
    )


# 顶部搜索表单
class TopSearchForm(FlaskForm):
    searchInput = StringField(
        label='名称',
        validators=[
            DataRequired()
        ],
        description='搜索关键词',
        render_kw={
            "type": "search",
            "placeholder": "Search",
            "class": "topsearch-form-item",
            "id": "searchInput",
            "value": "",
            "size": "30",
            "maxlength": "80",
            "required": "required"
        }
    )
    submit = SubmitField(
        "Submit",
        render_kw={
            "class": "btn btn-primary",
            "type": "submit",
            "id": "submit"
        }
    )



# 侧边栏搜索
class EasySearchForm(FlaskForm):
    SideSearch = StringField(
        label='名称',
        validators=[
            DataRequired()
        ],
        description='搜索关键词',
        render_kw={
            "type": "search",
            "placeholder": "Search",
            "class": "search-field",
            "id": "SideSearch",
            "value": "",
        }
    )
    submit = SubmitField(
        "Submit",
        render_kw={
            "class": "search-submit",
            "type": "submit",
            "id": "SideSubmit"
        }
    )
    # s = StringField(
    #     label='名称',
    #     validators=[
    #         DataRequired()
    #     ],
    #     description='搜索关键词',
    #     render_kw={
    #         "type": "search",
    #         "placeholder": "Search",
    #         "class": "search-field",
    #         # "name": "s",
    #         "id": "SideSearch",
    #         "value": "",
    #         # "size": "30",
    #         # "maxlength": "80",
    #         # "required": "required"
    #     }
    # )


# 登陆表单
class LoginForm(FlaskForm):
    account = StringField(
        label="用户名",
        validators=[
            DataRequired()
        ],
        description="账号",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入账号！",
        }

    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired()
        ],
        description="密码",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请输入密码！",
            "lay-verify": "required",
        }
    )
    verify_code = StringField(
        label='验证码',
        validators=[
            DataRequired()
        ],
        description="验证码",
        render_kw={
            "id": "my_verify_code",
            # "type": "text",
            "lay-verify": "required",
            "class": "layui-input-inline",
            "placeholder": "请输入验证码！",
        }
    )
    submit = SubmitField(
        "登录",
        render_kw={
            "type": "submit",
            "lay-filter": "login",
            "style": "width:100%;",
            # "onclick": "mesg()"
        }
    )


class RegisterForm(FlaskForm):
    account = StringField(
        label="请输入用户名",
        validators=[
            DataRequired()
        ],
        description="注册用户名输入框",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入用户名！",
        }
    )
    pwd = PasswordField(
        label="请输入密码",
        validators=[
            DataRequired()
        ],
        description="注册密码输入框",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请输入密码！",
            "lay-verify": "required",
        }
    )
    repeat_pwd = PasswordField(
        label="请确认密码",
        validators=[
            DataRequired()
        ],
        description="请确认密码",
        render_kw={
            "type": "password",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请确认密码！",
        }
    )
    verify_code = StringField(
        label='验证码',
        validators=[
            DataRequired()
        ],
        description="验证码",
        render_kw={
            "id": "my_verify_code",
            "lay-verify": "required",
            "class": "layui-input-inline",
            "width": "40%",
            "placeholder": "请输入验证码！",
        }
    )
    submit = SubmitField(
        "注册",
        render_kw={
            "type": "submit",
            "lay-filter": "login",
            "style": "width:100%;",
            # "onclick": "mesg()"
        }
    )
