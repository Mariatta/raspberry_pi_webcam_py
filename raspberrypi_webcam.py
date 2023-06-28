# Write your code here :-)
import os

import subprocess

import flickrapi
import webbrowser

from datetime import datetime


FLICKR_KEY = os.environ.get("FLICKR_KEY")
FLICKR_SECRET = os.environ.get("FLICKR_SECRET")


def authorize_flickr():
    """Obtain Flickr Auth"""
    flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET)
    if not flickr.token_valid(perms="write"):
        flickr.get_request_token(oauth_callback="oob")
        authorize_url = flickr.auth_url(perms="write")
        webbrowser.open_new_tab(authorize_url)
        verifier = str(input("Verifier code: "))
        flickr.get_access_token(verifier)
    return flickr


def capture_photo(filename):
    """Call fswebcam"""
    subprocess.run(["fswebcam",
        "--no-banner",
        filename
        ]
   )

# copied from flickr api docs
class FileWithCallback(object):
    def __init__(self, filename, callback):
        self.file = open(filename, 'rb')
        self.callback = callback
        # the following attributes and methods are required
        self.len = os.path.getsize(filename)
        self.fileno = self.file.fileno
        self.tell = self.file.tell

    def read(self, size):
        if self.callback:
            self.callback(self.tell() * 100 // self.len)
        return self.file.read(size)


def callback(progress):
    print(progress)


def main():
    flickr = authorize_flickr()
    # Change this to your liking
    filename = f"/home/mariatta/mu_code/images/image_{datetime.now():%Y-%m-%d:%H:%M:%S}.jpg"
    capture_photo(filename)
    params = {"filename": filename}
    params["fileobj"] = FileWithCallback(params["filename"], callback)
    flickr.upload(filename=filename)


if __name__ == "__main__":
    main()