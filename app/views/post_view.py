from flask import Blueprint, request, redirect
from flask import render_template, g, Blueprint
from api.user_api import UserDB
from api.post_api import Post, PostDB

post_list_blueprint = Blueprint("post_list_blueprint", __name__)

@post_list_blueprint.route('/', methods = ["GET", "POST"])
def index():
    database = PostDB(g.mysql_db, g.mysql_cursor)

    if request.method == "POST":
        post_ids = request.form.getlist("post_item")
        for id in post_ids:
            database.delete_post_by_id(id)

    return render_template('index.html', timeline = database.select_all_posts())


@post_list_blueprint.route('/post-entry')
def post_entry():
   return render_template("post-entry.html")


@post_list_blueprint.route('/add-post', methods = ["POST"])
def add_post():
    title = request.form.get("post_title")
    content = request.form.get("post_content")
    username = request.form.get("post_username")
    
    userdb = UserDB(g.mysql_db, g.mysql_cursor)
    user_id = userdb.select_user_by_username(username)
    
    new_post = Post(title, content, user_id)
    database = PostDB(g.mysql_db, g.mysql_cursor)

    database.insert_post(new_post)

    return redirect('/')


@post_list_blueprint.route('/post-edit')
def post_edit():
   return render_template("post-edit.html")


@post_list_blueprint.route('/edit-post', methods = ["PUT"])
def edit_post():
    title = request.form.get('post_title')

    new_title = request.form.get("post_new_title")
    new_content = request.form.get("post_new_content")
    username = request.form.get("post_username")

    userdb = UserDB(g.mysql_db, g.mysql_cursor)
    user_id = userdb.select_user_by_username(username)

    new_post = Post(new_title, new_content, user_id)
    database = PostDB(g.mysql_db, g.mysql_cursor)
    post = database.select_post_by_title(title)

    database.update_post(post, new_post)

    return redirect('/')


@post_list_blueprint.route('/delete-post', methods = ["DELETE"])
def delete_post():
    title = request.form.get('post_title')

    database = PostDB(g.mysql_db, g.mysql_cursor)
    post = database.select_post_by_title(title)

    database.delete_post_by_id(post)

    return redirect('/')


@post_list_blueprint.route('/user-profile', methods = ["GET", "POST"])
def user_index():
    userdb = UserDB(g.mysql_db, g.mysql_cursor)
    database = PostDB(g.mysql_db, g.mysql_cursor)

    username = request.form.get("post_username")
    user_id = userdb.select_user_by_username(username)

    if request.method == "POST":
        post_ids = request.form.getlist("post_item")
        for id in post_ids:
            database.delete_post_by_id(id)

    return render_template('user-profile.html', user_profile = database.select_posts_by_user_id(user_id))