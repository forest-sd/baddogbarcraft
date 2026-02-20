#!/usr/bin/env python3
"""Generate static site for baddogbarcraft.com — Dark moody copper/amber bar theme"""
import os, json

DOMAIN = "baddogbarcraft.com"
PAGES_URL = "baddogbarcraft.pages.dev"
SITE_NAME = "Bad Dog Bar Craft"
TAGLINE = "Unleash the Flavors of Crafted Cocktail Elixirs"

img_dir = "images"
all_images = sorted([f for f in os.listdir(img_dir) if f.endswith('.webp')])
logo_img = "favicon.png"

posts = [
    {"slug": "unlocking-the-art-of-craft-cocktails-techniques-recipes", "title": "Unlocking The Art of Craft Cocktails: Techniques & Recipes", "date": "2024-11-30", "excerpt": "Craft Cocktails are a celebration of creativity and nuance in the world of mixology, where every drink tells a story."},
    {"slug": "mastering-mixology-essential-skills-for-aspiring-bartenders", "title": "Mastering Mixology: Essential Skills for Aspiring Bartenders", "date": "2024-11-30", "excerpt": "Mixology is not merely the act of mixing drinks; it is an intricate art form that combines precision, creativity, and knowledge."},
    {"slug": "how-wifi-connected-smart-bar-tools-elevate-your-cocktail-craft-at-home", "title": "How WiFi-Connected Smart Bar Tools Elevate Your Cocktail Craft at Home", "date": "2025-08-19", "excerpt": "WiFi-connected smart bar tools are revolutionizing home cocktail making with precision and convenience."},
    {"slug": "explore-artisanal-elixirs-for-unique-beverage-experiences", "title": "Explore Artisanal Elixirs for Unique Beverage Experiences", "date": "2024-11-30", "excerpt": "Artisanal Elixirs are handcrafted beverages that offer a unique blend of flavors and wellness benefits."},
    {"slug": "enhancing-your-drinks-with-cocktail-bitters-a-comprehensive-guide", "title": "Enhancing Your Drinks with Cocktail Bitters: A Comprehensive Guide", "date": "2024-11-30", "excerpt": "Cocktail Bitters are the quintessential ingredient that can elevate any drink, contributing complexity and depth."},
    {"slug": "creating-flavor-infusions-transforming-drinks-into-cocktails", "title": "Creating Flavor Infusions: Transforming Drinks into Cocktails", "date": "2024-11-30", "excerpt": "Cocktail infusion techniques are an innovative approach to enhance the flavor profile of beverages."},
    {"slug": "diy-bitters-step-by-step-tutorials-with-bad-dog-barcraft", "title": "DIY Bitters: Step-by-Step Tutorials with Bad Dog Barcraft", "date": "2024-11-30", "excerpt": "Learn how to create your own cocktail bitters at home with our comprehensive step-by-step guide."},
    {"slug": "the-ultimate-guide-to-curating-your-signature-cocktail-menu-with-artisanal-elixirs", "title": "The Ultimate Guide to Curating Your Signature Cocktail Menu with Artisanal Elixirs", "date": "2025-08-19", "excerpt": "Artisanal elixirs are specialized, often small-batch liqueurs and syrups perfect for signature cocktails."},
]

NAV = [("Home", "/"), ("About", "/about/"), ("Posts", "/posts/"), ("Contact", "/contact-us/")]

def header(title, desc="", canonical="/"):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc or title}">
<link rel="canonical" href="https://{PAGES_URL}{canonical}">
<link rel="icon" href="/images/favicon.png">
<link rel="stylesheet" href="/css/style.css">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc or title}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://{PAGES_URL}{canonical}">
</head>
<body>
<header class="header">
  <div class="header__inner">
    <a href="/" class="header__logo">🐕 {SITE_NAME}</a>
    <nav class="header__nav">
      <button class="menu-toggle" aria-label="Menu">&#9776;</button>
      <ul class="nav__list">
        {''.join(f'<li><a href="{url}">{name}</a></li>' for name, url in NAV)}
      </ul>
    </nav>
  </div>
</header>
'''

FOOTER = f'''
<footer class="footer">
  <div class="footer__inner">
    <div class="footer__col">
      <h3>🐕 {SITE_NAME}</h3>
      <p>Your premier destination for crafted beverages. We pride ourselves on offering an exceptional selection of handcrafted cocktails, local brews, and a welcoming atmosphere.</p>
    </div>
    <div class="footer__col">
      <h3>Explore</h3>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about/">About Us</a></li>
        <li><a href="/posts/">Articles</a></li>
        <li><a href="/contact-us/">Contact</a></li>
      </ul>
    </div>
    <div class="footer__col">
      <h3>Legal</h3>
      <ul>
        <li><a href="/privacy/">Privacy Policy</a></li>
        <li><a href="/terms/">Terms of Service</a></li>
      </ul>
    </div>
  </div>
  <div class="footer__bottom">
    <p>&copy; 2024 {SITE_NAME}. All rights reserved. Must be 21+ to consume alcohol.</p>
  </div>
</footer>
<script>
document.querySelector('.menu-toggle').addEventListener('click', function() {{
  document.querySelector('.nav__list').classList.toggle('active');
}});
</script>
</body>
</html>'''

def post_card(post, idx):
    img = all_images[idx % len(all_images)] if all_images else ""
    return f'''<article class="card">
  <a href="/posts/{post['slug']}/">
    {f'<img src="/images/{img}" alt="{post["title"]}" class="card__img" loading="lazy">' if img else ''}
    <div class="card__body">
      <h2 class="card__title">{post['title']}</h2>
      <time class="card__date">{post['date']}</time>
      <p class="card__excerpt">{post['excerpt']}</p>
    </div>
  </a>
</article>'''

def write(path, content):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# Homepage
home_schema = json.dumps({"@context":"https://schema.org","@type":"BarOrPub","name":SITE_NAME,"url":f"https://{PAGES_URL}/","description":TAGLINE}, indent=2)
home = header(f"{SITE_NAME} — {TAGLINE}", TAGLINE, "/")
home += f'<script type="application/ld+json">{home_schema}</script>\n'
home += '<main class="main">\n<section class="hero">\n'
home += f'<h1>{SITE_NAME}</h1>\n<p class="hero__tagline">{TAGLINE}</p>\n'
home += '<p>Bad Dog Bar Craft is your premier destination for all things related to crafted beverages. Nestled in the heart of the community, we pride ourselves on offering an exceptional selection of handcrafted cocktails, local brews, and a welcoming atmosphere that encourages gathering and celebration.</p>\n'
home += '<p>At Bad Dog Bar Craft, we believe that every drink tells a story. Our skilled bartenders are passionate about mixology and are dedicated to using only the freshest ingredients and locally sourced products to create unforgettable drinking experiences.</p>\n'
home += '<a href="/posts/" class="btn">Explore Our Articles</a>\n</section>\n'
home += '<section class="posts-grid">\n<h2>Featured Articles</h2>\n<div class="grid">\n'
for i, p in enumerate(posts[:6]):
    home += post_card(p, i)
home += '</div>\n</section>\n</main>\n'
home += FOOTER
write("index.html", home)

# About page
about = header("About Bad Dog Bar Craft", "Learn about Bad Dog Bar Craft and our passion for mixology.", "/about/")
about += '''<main class="main"><article class="page">
<h1>About Bad Dog Bar Craft</h1>
<p>Bad Dog Bar Craft is your premier destination for all things related to crafted beverages. We pride ourselves on offering an exceptional selection of handcrafted cocktails, local brews, and a welcoming atmosphere that encourages gathering and celebration.</p>
<h2>Our Story</h2>
<p>Born from a passion for exceptional cocktails and the art of mixology, Bad Dog Bar Craft has established itself as a cornerstone of the local beverage scene. Our journey began with a simple belief: every drink should be an experience, not just a beverage. From our carefully curated spirits collection to our house-made syrups and bitters, every element is chosen with intention and care.</p>
<h2>Our Philosophy</h2>
<p>At Bad Dog Bar Craft, we believe that every drink tells a story. Our skilled bartenders are passionate about mixology and are dedicated to using only the freshest ingredients and locally sourced products. We work with local farms, distilleries, and producers to ensure that every cocktail we serve reflects the best of what our community has to offer.</p>
<h2>The Experience</h2>
<p>Step into Bad Dog Bar Craft and you'll find more than just great drinks. Our space is designed to be a gathering place — somewhere you can relax after work, celebrate special occasions, or simply enjoy good conversation over a perfectly crafted cocktail. Our knowledgeable staff is always happy to recommend drinks, explain our ingredients, or create something custom tailored to your taste.</p>
<h2>Craft & Community</h2>
<p>We're more than a bar — we're a community hub for cocktail enthusiasts, home bartenders, and anyone who appreciates the art of a well-made drink. Through our articles, tutorials, and events, we share our knowledge and passion for mixology with everyone who walks through our doors or visits our site.</p>
</article></main>
''' + FOOTER
write("about/index.html", about)

# Posts index
posts_page = header("Articles — Bad Dog Bar Craft", "Explore our collection of cocktail and mixology articles.", "/posts/")
posts_page += '<main class="main"><h1>All Articles</h1><div class="grid">\n'
for i, p in enumerate(posts):
    posts_page += post_card(p, i)
posts_page += '</div></main>\n' + FOOTER
write("posts/index.html", posts_page)

# Contact page
contact = header("Contact Us — Bad Dog Bar Craft", "Get in touch with Bad Dog Bar Craft.", "/contact-us/")
contact += '''<main class="main"><article class="page">
<h1>Contact Us</h1>
<p>We'd love to hear from you! Whether you have questions about our cocktail recipes, want to learn more about our ingredients, or are interested in hosting a private event, we're here to help.</p>
<div class="contact-info">
<h2>Get in Touch</h2>
<ul>
<li><strong>Email:</strong> hello@baddogbarcraft.com</li>
<li><strong>Hours:</strong> Tuesday–Sunday, 4 PM – Midnight</li>
</ul>
</div>
<h2>Visit Us</h2>
<p>Come experience Bad Dog Bar Craft in person. Our warm, inviting space is the perfect setting for everything from casual after-work drinks to special celebrations. We recommend making a reservation for parties of 6 or more.</p>
<h2>Private Events</h2>
<p>Bad Dog Bar Craft is available for private events, cocktail classes, and corporate gatherings. Our team can create custom cocktail menus and experiences tailored to your event. Contact us to learn more about our event packages and availability.</p>
<h2>Collaborations</h2>
<p>We're always interested in collaborating with local distillers, farmers, artisans, and fellow beverage enthusiasts. If you have an idea for a collaboration, we'd love to hear about it.</p>
</article></main>
''' + FOOTER
write("contact-us/index.html", contact)

# Privacy page
privacy = header("Privacy Policy — Bad Dog Bar Craft", "Bad Dog Bar Craft privacy policy.", "/privacy/")
privacy += '''<main class="main"><article class="page">
<h1>Privacy Policy</h1>
<p>At Bad Dog Bar Craft, we are committed to protecting your privacy. This Privacy Policy describes how we collect, use, and share information when you visit our website.</p>
<h2>Information Collection</h2>
<p>We may collect information you provide directly to us, such as when you contact us, subscribe to our newsletter, or make a reservation. This may include your name, email address, and phone number.</p>
<h2>Use of Information</h2>
<p>We use the information we collect to provide and improve our services, communicate with you about events and promotions, and respond to your inquiries.</p>
<h2>Cookies</h2>
<p>Our website may use cookies and similar tracking technologies to enhance your browsing experience and analyze website traffic.</p>
<h2>Contact</h2>
<p>If you have questions about this Privacy Policy, please contact us at hello@baddogbarcraft.com.</p>
</article></main>
''' + FOOTER
write("privacy/index.html", privacy)

# Terms page
terms = header("Terms of Service — Bad Dog Bar Craft", "Bad Dog Bar Craft terms of service.", "/terms/")
terms += '''<main class="main"><article class="page">
<h1>Terms of Service</h1>
<p>Welcome to Bad Dog Bar Craft. By accessing or using our website, you agree to be bound by these Terms of Service.</p>
<h2>Use of Website</h2>
<p>You may use our website for lawful purposes only. You must not use our website in any way that may cause damage to the website or impair the availability or accessibility of the website.</p>
<h2>Content</h2>
<p>All content on this website, including text, images, and recipes, is the property of Bad Dog Bar Craft and is protected by copyright laws. You may not reproduce, distribute, or create derivative works without our written permission.</p>
<h2>Age Restriction</h2>
<p>Our content is intended for individuals of legal drinking age (21+ in the United States). By using our website, you confirm that you are of legal drinking age in your jurisdiction.</p>
<h2>Disclaimer</h2>
<p>The cocktail recipes and techniques shared on our website are for informational purposes. Please drink responsibly.</p>
</article></main>
''' + FOOTER
write("terms/index.html", terms)

# Post content
generic_bar_content = """<h2>The Art of Craft Beverages</h2>
<p>The world of craft cocktails is a rich tapestry of flavors, techniques, and traditions. At Bad Dog Bar Craft, we're passionate about exploring every facet of this art form, from classic recipes that have stood the test of time to innovative new creations that push the boundaries of what's possible in a glass.</p>
<h2>Ingredients Matter</h2>
<p>The foundation of any great cocktail is the quality of its ingredients. We believe in sourcing the finest spirits, fresh produce, and artisanal components to create drinks that are truly exceptional. From house-made syrups and tinctures to locally foraged herbs and botanicals, every element in our cocktails is chosen with care and intention.</p>
<h2>Technique and Craft</h2>
<p>Great cocktails aren't just about what goes in the glass — they're about how it gets there. Proper technique is essential to bringing out the best in your ingredients. Whether it's the precise dilution achieved through stirring, the aeration created by shaking, or the aromatics released by muddling, each technique serves a specific purpose in crafting the perfect drink.</p>
<h2>Experimentation and Discovery</h2>
<p>One of the most exciting aspects of mixology is the endless potential for experimentation. New flavor combinations, unusual ingredients, and innovative techniques keep the craft fresh and exciting. We encourage everyone — from professional bartenders to home enthusiasts — to explore, experiment, and discover their own signature style.</p>
<h2>Sharing the Knowledge</h2>
<p>At Bad Dog Bar Craft, we believe that great cocktail knowledge should be shared. Through our articles, tutorials, and events, we aim to demystify the world of mixology and empower everyone to create exceptional drinks at home or behind the bar.</p>"""

for i, post in enumerate(posts):
    img = all_images[i % len(all_images)] if all_images else ""
    content = generic_bar_content
    schema = json.dumps({"@context":"https://schema.org","@type":"Article","headline":post['title'],"datePublished":post['date'],"publisher":{"@type":"Organization","name":SITE_NAME}}, indent=2)
    
    related = [p for p in posts if p['slug'] != post['slug']][:3]
    related_html = '<div class="related"><h2>More Articles</h2><div class="related__grid">'
    for r in related:
        related_html += f'<a href="/posts/{r["slug"]}/" class="related__item"><h3>{r["title"]}</h3><time>{r["date"]}</time></a>'
    related_html += '</div></div>'
    
    page = header(post['title'], post['excerpt'], f"/posts/{post['slug']}/")
    page += f'<script type="application/ld+json">{schema}</script>\n'
    page += f'<main class="main"><article class="post">\n'
    page += f'<h1>{post["title"]}</h1>\n<time class="post__date">{post["date"]}</time>\n'
    if img:
        page += f'<img src="/images/{img}" alt="{post["title"]}" class="post__img" loading="lazy">\n'
    page += f'<div class="content">{content}</div>\n'
    page += related_html
    page += '</article></main>\n'
    page += FOOTER
    write(f"posts/{post['slug']}/index.html", page)

# Sitemap
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
urls = ["/", "/about/", "/posts/", "/contact-us/", "/privacy/", "/terms/"]
urls += [f"/posts/{p['slug']}/" for p in posts]
for u in urls:
    sitemap += f'  <url><loc>https://{PAGES_URL}{u}</loc></url>\n'
sitemap += '</urlset>'
write("sitemap.xml", sitemap)

write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: https://{PAGES_URL}/sitemap.xml\n")

print(f"Generated {len(urls)} pages for {SITE_NAME}")
