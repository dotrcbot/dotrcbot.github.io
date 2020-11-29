import os
from mutagen.mp4 import MP4

xmlfile = '''<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:wfw="http://wellformedweb.org/CommentAPI/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:atom="http://www.w3.org/2005/Atom"
    xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"
    xmlns:slash="http://purl.org/rss/1.0/modules/slash/"
    xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
    xmlns:feedburner="http://rssnamespace.org/feedburner/ext/1.0" version="2.0">
    <channel>
        <title>蒋勋细说红楼梦</title>
        <link>https://dotrcbot.github.io/</link>
        <language>zh-CN</language>
        <atom:link href="https://dotrcbot.github.io/feed.xml" rel="self" type="application/rss+xml"/>
        <copyright>Dotrcbot</copyright>
        <itunes:subtitle>蒋勋细说红楼梦</itunes:subtitle>
        <itunes:author>Dotrcbot</itunes:author>
        <itunes:summary>蒋勋细说红楼梦</itunes:summary>
        <itunes:keywords>sounds</itunes:keywords>
        <description>蒋勋细说红楼梦</description>
        <itunes:owner>
            <itunes:name>Dotrcbot</itunes:name>
            <itunes:email>dotrcbot@protonmail.com</itunes:email>
        </itunes:owner>
        <itunes:image href="https://dotrcbot.github.io/cover.webp"/>
        <itunes:category text="Education">
            <itunes:category text="Self-Improvement"/>
        </itunes:category>
        <itunes:explicit>no</itunes:explicit>
'''

os.chdir("audio/")

for file in sorted(os.listdir()):
    if file.endswith('.m4a'):
        statinfo = os.stat(file)
        size = str(statinfo.st_size)
        audio = MP4(file)
        length = str(audio.info.length)
        
        xmlfile += "<item>\n"
        xmlfile += "<link>https://dotrcbot.github.io/</link>\n"
        xmlfile += "<title>{}</title>\n".format(file.split('.m4a')[0])
        xmlfile += "<enclosure url='https://dotrcbot.github.io/audio/{}' length='{}' type='audio/mpeg'/>\n".format(file,size)
        xmlfile += '<itunes:image href="https://dotrcbot.github.io/cover.webp"/>\n'
        xmlfile += "<itunes:duration>{}</itunes:duration>\n".format(length)
        xmlfile += "<guid isPermaLink='false'>https://dotrcbot.github.io/audio/{}</guid>\n".format(file)
        xmlfile += "</item>\n"

xmlfile += '''</channel>
</rss>
'''

with open('../feed.xml', 'w') as feed:
    feed.write(xmlfile)


print(xmlfile)

