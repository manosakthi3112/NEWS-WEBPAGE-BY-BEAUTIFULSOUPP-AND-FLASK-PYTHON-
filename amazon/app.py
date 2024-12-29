
from flask import Flask, render_template, request, redirect, url_for, session
import scrap
app = Flask(__name__)
app.secret_key = "3112"  



@app.route('/')
def index():
    try:
        f=scrap.tot()
        d=scrap.tamilnadu()
        cinema=scrap.cinema()
        lifestyle=scrap.lifestyle()
        sports=scrap.sports()
        business=scrap.business()
        india=scrap.india()
        world=scrap.world()
        spiritual=scrap.spiritual()
        return render_template('base.html',data=f,tamilnadu=d,cinema=cinema,lifestyle=lifestyle,sports=sports,business=business,india=india,world=world,spiritual=spiritual)
    except:
        return render_template('ERROR.html')
@app.route('/link', methods=["GET", "POST"])
def link():
    try:
        if request.method == "POST":
            result = request.form.get('fname')
            img=request.form.get('jname')
            link_page=scrap.cinema_1(result)
            return render_template('link.html',data=link_page,img_src=img)
        elif request.method == "GET":
            print("Received a GET request")
        return render_template('base.html')
    except:
        return render_template('ERROR.html')
@app.route('/more/<data_>', methods=["GET", "POST"])
def more(data_):
    try:
        if data_ == "trending":
            data = scrap.tot()
            name = "TRENDING"
        elif data_ == "tamilnadu":
            data = scrap.tamilnadu()
            name = "TAMIL NADU"
        elif data_ == 'cinema':
            data = scrap.cinema()
            name = "CINEMA"
        elif data_ == 'lifestyle':
            data = scrap.lifestyle()
            name = "LIFESTYLE"
        elif data_ == 'sports':
            data = scrap.sports()
            name = "SPORTS"
        elif data_ == 'bussiness':
            data = scrap.bussiness()
            name = "BUSINESS"
        elif data_ == 'india':
            data = scrap.india()
            name = "INDIA"
        elif data_ == 'world':
            data = scrap.world()
            name = "WORLD"
        elif data_ == 'spiritual':
            data = scrap.spiritual()
            name = "SPIRITUAL"
        else:
            data = scrap.tot()
            name = "TRENDING"
        print(data)
        return render_template('more.html',data=data,name=name+"\t"+"NEWS")
    except:
        return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
