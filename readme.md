Subreddit Image Downloader
================================

Sometimes I like to collect large galleries of images, but I don't
want to manually save them all, or even do quality control.

This can be invoked like so:
    from scrape_images import Scrape_images

    Scrape_images('gunporn','/home/brandon/Downloads')

The first parameter is the subreddit you want to download from, the
second is the path. The script automagically creates a folder like 
"reddit_gunporn-10-2012". The script also doesn't duplicate images,
based on the file name.