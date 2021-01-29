
@app.route('/index', methods = ['GET', 'POST'])
def index():
    str_url = 'https://lovobin.github.io'
    my_list = ['羽毛球', '足球', '篮球', '羽毛球']
    return render_template('index.html', str_url = str_url, my_list = my_list)

