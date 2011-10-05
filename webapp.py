import urllib2
from base64 import b64encode
from PIL import Image, ImageFile, ImageFileIO
import StringIO

from flask import Flask, render_template, request

DEBUG=True

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
    
@app.route("/process", methods=['POST'])
def process():
    
    # Fetch Image Data from Remote Server
    image_url = request.form['image_url']
    response = urllib2.urlopen(image_url)
    
    #TODO: check for error fetching image

    #Create image file in memory so PIL can use it
    memory_image = StringIO.StringIO(response.read())
        
    # Save frames of GIF as base64 encoded data
    frames = []
    im = Image.open(memory_image)
    
    try:
        while 1:
            im.seek(im.tell()+1)
            
            memory_frame = StringIO.StringIO()
            im.save(memory_frame, format='GIF')
            
            base64_encoded_frame = b64encode(memory_frame.getvalue())
            frames.append(base64_encoded_frame)
            
    except EOFError:
        # called at end of every gif frame sequence:
        memory_image.close()
        
    return render_template('index.html', frames=frames)
    

if __name__ == "__main__":
    app.run(debug=DEBUG, host='0.0.0.0')