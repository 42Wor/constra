import os
import re
import glob

files_to_update = glob.glob('src/*.html')

for file in files_to_update:
    filepath = os.path.join(r'd:\1\constra', file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Meta tags
    content = re.sub(
        r'<title>Snohomish Construction</title>.*?(<meta name="viewport")',
        r'<title>International Estimating | Accurate Construction Estimates</title>\n  <meta name="description" content="Accurate, fast and reliable construction estimating services for contractors, developers and builders across the USA.">\n  \1',
        content, flags=re.DOTALL
    )

    # Top bar info
    content = re.sub(
        r'<p class="info-text">The Northwest\'s #1 Deepwoods Cabin Construction Company</p>',
        r'<p class="info-text">Professional Construction Estimating Services</p>',
        content
    )

    # Logo
    content = re.sub(
        r'<img loading="lazy" src="assets/images/cabin.svg" alt="Constra">\s*<br />\s*<span>Snohomish Construction</span>',
        r'<img loading="lazy" src="assets/images/scraped/logo.png" alt="International Estimating">',
        content
    )

    # Email
    content = re.sub(
        r'snohomishconstruction@protonmail\.com',
        r'info@internationalestimating.com',
        content
    )

    # Footer logo and about
    content = re.sub(
        r'<img loading="lazy" width="200px" class="footer-logo" src="assets/images/cabin-white\.svg" alt="Constra">\s*<br />\s*<span id="contact"></span>\s*<strong>Snohomish Construction</strong>\s*<p>The best option for your off-grid dreamhome\. No matter the location, you can count on us\.</p>',
        r'<img loading="lazy" width="200px" class="footer-logo" src="assets/images/scraped/logo.png" alt="International Estimating">\n            <br />\n            <span id="contact\"></span>\n            <strong>International Estimating</strong>\n            <p>Accurate, fast and reliable construction estimating services for contractors, developers and builders across the USA.</p>',
        content
    )

    # Footer Services
    content = re.sub(
        r'<li><a>Pre-Construction</a></li>\s*<li><a>General Contracting</a></li>\s*<li><a>Construction Management</a></li>\s*<li><a>Design and Build</a></li>\s*<li><a>Self-Perform Construction</a></li>',
        r'<li><a>Plumbing Estimating</a></li>\n              <li><a>Electrical Estimating</a></li>\n              <li><a>Mechanical Estimating</a></li>\n              <li><a>Take-Off Estimating</a></li>',
        content
    )
    
    # Update facts area
    content = re.sub(
        r'<div class="col-md-3 col-sm-6 ts-facts">\s*<div class="ts-facts-img">\s*<img loading="lazy" src="assets/images/icon-image/fact1\.png" alt="facts-img">\s*</div>\s*<div class="ts-facts-content">\s*<h2 class="ts-facts-num"><span class="counterUp" data-count="110">0</span></h2>\s*<h3 class="ts-facts-title">Total Projects</h3>\s*</div>\s*</div><!-- Col end -->\s*<div class="col-md-3 col-sm-6 ts-facts mt-5 mt-sm-0">\s*<div class="ts-facts-img">\s*<img loading="lazy" src="assets/images/icon-image/fact2\.png" alt="facts-img">\s*</div>\s*<div class="ts-facts-content">\s*<h2 class="ts-facts-num"><span class="counterUp" data-count="23">0</span></h2>\s*<h3 class="ts-facts-title">Staff Members</h3>\s*</div>\s*</div><!-- Col end -->\s*<div class="col-md-3 col-sm-6 ts-facts mt-5 mt-md-0">\s*<div class="ts-facts-img">\s*<img loading="lazy" src="assets/images/icon-image/fact3\.png" alt="facts-img">\s*</div>\s*<div class="ts-facts-content">\s*<h2 class="ts-facts-num"><span class="counterUp" data-count="1253">0</span></h2>\s*<h3 class="ts-facts-title">Hours of Work</h3>\s*</div>\s*</div><!-- Col end -->\s*<div class="col-md-3 col-sm-6 ts-facts mt-5 mt-md-0">\s*<div class="ts-facts-img">\s*<img loading="lazy" src="assets/images/icon-image/fact4\.png" alt="facts-img">\s*</div>\s*<div class="ts-facts-content">\s*<h2 class="ts-facts-num"><span class="counterUp" data-count="4">0</span></h2>\s*<h3 class="ts-facts-title">Countries Experience</h3>\s*</div>\s*</div><!-- Col end -->',
        r'<div class="col-md-3 col-sm-6 ts-facts">\n              <div class="ts-facts-img">\n                <img loading="lazy" src="assets/images/icon-image/fact1.png" alt="facts-img">\n              </div>\n              <div class="ts-facts-content">\n                <h2 class="ts-facts-num"><span class="counterUp" data-count="98">0</span>%</h2>\n                <h3 class="ts-facts-title">Accuracy</h3>\n              </div>\n          </div><!-- Col end -->\n\n          <div class="col-md-3 col-sm-6 ts-facts mt-5 mt-sm-0">\n              <div class="ts-facts-img">\n                <img loading="lazy" src="assets/images/icon-image/fact2.png" alt="facts-img">\n              </div>\n              <div class="ts-facts-content">\n                <h2 class="ts-facts-num"><span class="counterUp" data-count="5000">0</span>+</h2>\n                <h3 class="ts-facts-title">Projects</h3>\n              </div>\n          </div><!-- Col end -->\n\n          <div class="col-md-3 col-sm-6 ts-facts mt-5 mt-md-0">\n              <div class="ts-facts-img">\n                <img loading="lazy" src="assets/images/icon-image/fact3.png" alt="facts-img">\n              </div>\n              <div class="ts-facts-content">\n                <h2 class="ts-facts-num"><span class="counterUp" data-count="10">0</span>+</h2>\n                <h3 class="ts-facts-title">Years Experience</h3>\n              </div>\n          </div><!-- Col end -->\n\n          <div class="col-md-3 col-sm-6 ts-facts mt-5 mt-md-0">\n              <div class="ts-facts-img">\n                <img loading="lazy" src="assets/images/icon-image/fact4.png" alt="facts-img">\n              </div>\n              <div class="ts-facts-content">\n                <h2 class="ts-facts-num"><span class="counterUp" data-count="50">0</span></h2>\n                <h3 class="ts-facts-title">States Experience</h3>\n              </div>\n          </div><!-- Col end -->',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print('Common replacements completed')
