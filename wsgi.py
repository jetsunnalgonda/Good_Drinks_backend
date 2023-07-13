
HELLO_WORLD = """<html>
<head>
    <title>PythonAnywhere hosted web application</title>
</head>
<body>
<h1>Good Drinks API</h1>
<p>
    Welcome to the Good Drinks API
</p>
<p>
    To ask the developer questions about the API, visit <a href="https://jetsunnalgonda.github.io">their portfolio.</a>
</p>
</body>
</html>"""

# import sys
# path = '/home/nalgonda/api'
# if path not in sys.path:
#     sys.path.insert(0, path)

# from application import app as application

from application import app

if __name__ == '__main__':
    app.run()

application = app  # Gunicorn entry point