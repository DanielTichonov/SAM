from datetime import datetime
import webbrowser
import time

html_content = f"<html> <head> <h1> SAM devops team first try </h1> </head> </html>"

with open("/var/www/html/index.nginx-debian.html", "w") as html_file:
        html_file.write(html_content)