# raspberry_pi_webcam_py


Python code for taking photos with webcam and Raspberry Pi, and
uploading it to Flickr.


# Purpose

This code can be run on a Raspberry Pi to command it to take pictures using 
a webcam.

I used a USB webcam, the same webcam I normally use for video calls.

I wanted to check on my aquarium/potato plants while we're away traveling.
With this code, the Raspberry Pi will take a photo once every hour and then
upload the photos to my Flickr account.

The script itself will take a photo and upload the photo to Flickr.
On the Raspberry Pi, I set up a cron job for running the script every hour.

Check the crontab.txt to see the cronjob setup.


More info about this project on my Mastodon thread:

https://fosstodon.org/@mariatta/110622646018088303


# Dependencies

flickr Python API: https://stuvel.eu/software/flickrapi/

```
pip install -U flickrapi
```


# How to run

Get API keys from Flickr. Store the API keys as environment variables
on the Raspberry Pi ``FLICKR_KEY`` and ``FLICKR_SECRET``.

Get Access to Flickr API [here](https://www.flickr.com/services/api/)

You may need to change the code and change the path of where you want the images
to be saved.

First time you run it (on the Raspberry Pi), it will open a web browser for the
OAuth web authentication flow. After that, the script should run without needing
to re-auth.


# Why Flickr

I wanted to use Google Photos API because I'm on Android and already have pretty
much all my photos on Google Photos. However they don't seem to have Python
client library available, and after trying to access the API with little success,
I decided to look into different solutions.

I've considered Flickr, or uploading as a file on GitHub.


# Other ideas

Some other ideas:

- [It was suggested to post the photos to Mastodon](https://fosstodon.org/@orsinium/110623304649763084).
  I think it's a great  idea. I won't do it on my personal account, so I need a
  different server that would allow bot accounts. Looks like [botsin.space](https://botsin.space/about) would
  work, but they have not approved my account.
  
- Instead of a cron job, I was thinking to set up web server and an API
  endpoint, something I could invoke anytime instead of having it run once every
  hour. Looking into it, it seems that I need a static IP and a domain address.
  Seems more complicated than what I have in mind, but perhaps that's my future
  project.
  
# Hardware setup

- Raspberry Pi 4 (8 GB)
- power supply
- Logitech USB webcam
- SD card

Additional hardware for development purpose:

- Monitor. I didn't buy a separate display for the Raspberry Pi, so I attached
  my own 49'' ultrawide monitor to it. My monitor is 49'' Samsung Odyssey. It has
  multiple inputs and has the ability to do split screen. So I could connect
  two different devices to the same monitor and it could display both. This monitor
  has 2 Display Port inputs, and 1 HDMI input. I attached the HDMI to the Raspberry Pi,
  and one of the Display Port to my laptop. See the setup [here](https://fosstodon.org/@mariatta/110622646018088303)
  
- Mouse. Any USB mouse will work. I use Evoluent Vertical Mouse.
  
- Keyboard. Any USB keyboard will work. I use Apple Magic Keyboard.

# Working with Raspberry Pi

Other than working on it directly, I've connected to it using my laptop
using SSH and SCP.

SSH terminal session:
```
ssh mariatta@raspberrpy.local
```

SCP to copy files over:
```
scp mariatta@raspberrypy.local:/filename ./
```

# The Flickr stream

https://www.flickr.com/photos/134275259@N03/

I took some photos of my aquarium at first.
Seeing it successful, my husband then wants it to monitor the potato
garden instead.

You could use it for anything, even as a security camera maybe?

Thanks for checking this out.

If you like it, please consider [sponsoring me](https://github.com/sponsors/Mariatta) on GitHub.
