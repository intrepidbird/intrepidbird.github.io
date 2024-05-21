from flask import Flask, Response
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/rss')
def rss_feed():
    posts = [
        {
            'title': 'First Blog Post',
            'link': 'https://intrepidbird.me/blog/posts/premier-blog-post/',
            'description': 'This is my very first blog post. Please read my statement on having a blog and sharing my thoughts.',
            'pubDate': datetime(2024, 1, 20, 0, 0, 0, tzinfo=pytz.UTC)
        },
        {
            'title': 'MAA 2024 AMC 8 Leaks Need to be Investigated',
            'link': 'https://intrepidbird.me/blog/posts/maa-needs-to-react-to-2024-amc-8-leaks/',
            'description': 'The 2024 AMC 8 was leaked. I think that MAA needs to investigate this and protect the integrity of the competition.',
            'pubDate': datetime(2024, 1, 21, 0, 0, 0, tzinfo=pytz.UTC)
        },
        {
            'title': 'MathCounts 2024',
            'link': 'https://intrepidbird.me/blog/posts/mathcounts-2024-was-a-win/',
            'description': 'I placed 9th out of ~300 people in my Chapter and captained my school this year in MathCounts. It was a well-planned and great event this year.',
            'pubDate': datetime(2024, 2, 4, 0, 0, 0, tzinfo=pytz.UTC)
        },
        {
            'title': 'Science Bowl 2024',
            'link': 'https://intrepidbird.me/blog/posts/new-jersey-regional-science-bowl-2024-pppl-sheng-brms/',
            'description': 'My experiences participating in and captaining my school to 2nd Place at the 2024 NJ MS Science Bowl! We had a great time at PPPL this year!',
            'pubDate': datetime(2024, 2, 24, 0, 0, 0, tzinfo=pytz.UTC)
        },
        {
            'title': 'BRCSs First Year',
            'link': 'https://intrepidbird.me/blog/posts/premier-blog-post/',
            'description': 'My thoughts on being a co-founder and the Bridgewater-Raritan Computer Science Clubs wonderful inaugural year.',
            'pubDate': datetime(2024, 3, 12, 0, 0, 0, tzinfo=pytz.UTC)
        },
        {
            'title': 'RidgeHacks 2024',
            'link': 'https://intrepidbird.me/blog/posts/how-we-cooked-so-hard-at-ridgehacks-with-graze/',
            'description': 'We won 2nd Place overall out of 22 teams at RidgeHacks 2024 with our HTML, CSS, and Flask application named 'Graze'.',
            'pubDate': datetime(2024, 4, 6, 0, 0, 0, tzinfo=pytz.UTC)
        },
        {
            'title': 'Po-Shen Lohs Math Talk',
            'link': 'https://intrepidbird.me/blog/posts/watching-po-shen-loh-at-a-math-conference/',
            'description': 'Reflections on hearing Professor Po-Shen Loh's talk about mathematics, competitions, and AI's role in math.',
            'pubDate': datetime(2024, 4, 7, 0, 0, 0, tzinfo=pytz.UTC)
        },
        {
            'title': '2024 NHL Playoffs',
            'link': 'https://intrepidbird.me/blog/posts/how-we-cooked-so-hard-at-ridgehacks-with-graze/',
            'description': 'Live Blog of the 2024 National Hockey League Stanley Cup Playoffs.',
            'pubDate': datetime(2024, 4, 20, 0, 0, 0, tzinfo=pytz.UTC)
        },
        {
            'title': 'MontyHacks VII',
            'link': 'https://intrepidbird.me/blog/posts/making-blaze-at-montyhacks-vii/',
            'description': 'My journey and experiences at MontyHacks VII building the HTML and CSS for our Flask application named 'Blaze'.',
            'pubDate': datetime(2024, 5, 18, 0, 0, 0, tzinfo=pytz.UTC)
        }, 
    ]

    rss_items = ''
    for post in posts:
        rss_items += f"""
        <item>
            <title>{post['title']}</title>
            <link>{post['link']}</link>
            <description>{post['description']}</description>
            <pubDate>{post['pubDate'].strftime('%a, %d %b %Y %H:%M:%S %z')}</pubDate>
        </item>
        """

    rss_feed = f"""<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
      <channel>
        <title>IntrepidBird | Blog</title>
        <link>https://intrepidbird.me/blog/</link>
        <description>IntrepidBird's Blog</description>
        {rss_items}
      </channel>
    </rss>
    """
    
    return Response(rss_feed, mimetype='application/rss+xml')

if __name__ == '__main__':
    app.run(debug=True)
