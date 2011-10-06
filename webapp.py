from gifexplode import GifExplode
from flask import Flask, render_template, request, abort

DEBUG=True

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.form:
        return process()
    else:
        return render_template('index.html')

    
def process():
    
    image_url = request.form['image_url']
    try:
        exploder = GifExplode(image_url)
        frames = exploder.explode()
    except ValueError:
        abort(500)
        
    return render_template('index.html', frames=frames,
                            image_url=image_url)
    

if __name__ == "__main__":
    app.run(debug=DEBUG, host='0.0.0.0')