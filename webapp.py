from gifexplode import GifExplode
from flask import Flask, render_template, request, abort, jsonify

DEBUG=True

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@app.route("/<path:image_url>")
def index(image_url=None):
    
    if not image_url and request.form:
        image_url = request.form['image_url']
        
    if image_url:
        
        frames = _explode_image_url(image_url)
                                
        return render_template('index.html', 
                               frames=frames,
                               image_url=image_url)
                                          
    else:
        return render_template('index.html')

@app.route("/api")
def api():
    return render_template('api.html')
    
@app.route("/api/explode", methods=['GET'])
def api_explode():
    
    image_url = request.args['image_url']
    frames = _explode_image_url(image_url)
    
    return jsonify(frames=frames)

def _explode_image_url(image_url):
    
    try:
        exploder = GifExplode(image_url)
        frames = exploder.explode()
    except ValueError:
        abort(500)
    
    return frames


if __name__ == "__main__":
    app.run(debug=DEBUG, host='0.0.0.0')