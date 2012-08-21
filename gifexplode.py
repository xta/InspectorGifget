import urllib2
import StringIO
from base64 import b64encode
from PIL import Image, ImageSequence

class GifExplode:
    def __init__(self, image_url):
        self._image_url = image_url
        self._image = None
        self._frames = []
        
    def explode(self):
        """ Returns list of base64 encoded frames """
        
        if not self._frames:

            self.__fetch_image()

            im = Image.open(self._image)

            prevFrame = None

            for i, frame in enumerate(ImageSequence.Iterator(im)):

                mask = frame.convert('RGBA')

                if prevFrame:
                    prevFrame.paste(frame, None, mask = mask.split()[3])
                else:
                    # At first frame, set as prevFrame
                    prevFrame = frame.copy()

                base64_encoded_frame = self.__encode_frame(prevFrame)
                self._frames.append(base64_encoded_frame)

        return self._frames
        
    def __fetch_image(self):
        """ Fetches the image from the web, saves to instance var"""
        
        # Note: this can raise a Value Error
        response = urllib2.urlopen(self._image_url)
        
        # Create image file in memory so PIL can use it
        self._image = StringIO.StringIO(response.read())
        
    def __encode_frame(self, frame):
        
        # Save frame to file-like object
        memory_frame = StringIO.StringIO()
        frame.save(memory_frame, format="PNG", **frame.info)

        # Encode
        base64_encoded_frame = b64encode(memory_frame.getvalue())
        
        memory_frame.close()
        
        return base64_encoded_frame