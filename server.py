from lib import run_server, get
from lib import read_html

@get('/')
def index():
     return read_html('templates/index.html')

run_server(2222)
