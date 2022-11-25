from flask import Flask, render_template
# 开发中的三个设置：debug、host、port的设置
# 创建一个flask对象
# url：http[port:80]/https[port:443]://yv_ming:port/path
# url与视图（path与路由）
app = Flask(__name__)


@app.route('/') # 装饰器
def hello_world():  # put application's code here
    return render_template("index.html")

# 带参数的url，将参数加入path。查询字符串的方式传参更灵活。
@app.route("/detail/<id>")
def detail_id(id):
    return "当前访问id是：%s" % id

@app.route("/datail/<blog_id>")
def detail_blog(blog_id):
    return render_template("detail_blog.html", blog_id=blog_id)

@app.route("/control")
def control_statement():
    age = 20
    books = [{"name":"三国演义",
             "author":"罗贯中"},
            {"name": "红楼梦",
             "author": "曹雪芹"}
            ]
    return render_template("control.html", age=age, books=books)

@app.route('/child1')
def child1():
    return render_template("child1.html")

@app.route('/child2')
def child2():
    return render_template("child2.html")
@app.route("/base")
def inherit_demo():
    return render_template("base.html")


if __name__ == '__main__':
    app.run()
