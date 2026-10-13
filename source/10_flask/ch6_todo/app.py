from flask import Flask, request, render_template, redirect, url_for
from database.repository import (get_todos,

from models import Todo
from flask import session # 로그인/로그아웃 여부 체ㅡ

app = Flask(__name__)
app.secret_key = "secret" # 세션을 사용할 경우 필수 

@app.route("/")
def index():
    "로그인 성공 로직 후 / todos(할일 목록 todos함수)로 이동"
    session["user_id"] = "hong" # 세션에 유저 아이디 저장
    session["user_name"] = "홍길동" # 세션에 유저 이름 저장
    # return redirect("/todos") # /todos 요청경로로 이동
    return redirect(url_for("todos")) # todos함수로 이동

@app.route('/logout')
def logout():
    "로그아웃 성공 로직 후 / 할일 목록 페이지로 이동"
    session.pop("user_id", None) # 세션에 유저 아이디 저장
    session.pop("user_name", None) # 세션에 유저 이름 저장
    return redirect(url_for("index")) # /index 요청경로로 이동

@app.route('/todos')
def todos():
    "할일 목록 페이지"
    order = request.args.get("order", "asc") # 정렬 순서 받아오기
    todos = get_todos(order) # 정렬 순서 적용한 할일 목록 반환
    return render_template("todo/todos.html", todos=todos, order=order)

@app.route('/create', methods=["POST"])
def create():
    "새로운 할일 추가"
    # todo = Todo(content=request.form.get("content")) 
    todo = Todo(**request.form.to_dict())
    print(todo)
    return "TEST"
# flask run --debug 실행시 로컬 환경에서 실행되는 것을 확인할 수 있음