from flask import Flask,render_template_string
import logging


# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = Flask(__name__)

# Simple template with inline styles
BASE_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cognito Auth Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: white;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .card {
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin-right: 10px;
        }
        .btn-secondary {
            background: #6c757d;
        }
        .text-center {
            text-align: center;
        }
        nav {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            margin-bottom: 20px;
            border-bottom: 1px solid #ddd;
        }
        nav ul {
            display: flex;
            list-style: none;
            padding: 0;
            margin: 0;
        }
        nav ul li {
            margin-left: 20px;
        }
        nav a {
            text-decoration: none;
            color: #007bff;
        }
    </style>
</head>
<body>
    <div class="container">
        <nav>
            <a href="/" style="font-weight: bold;">Cognito Auth Demo</a>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/signin">Sign In</a></li>
                <li><a href="/signup">Sign Up</a></li>
            </ul>
        </nav>

        {% block content %}{% endblock %}
    </div>
</body>
</html>"""

INDEX_TEMPLATE = BASE_TEMPLATE.replace("{% block content %}{% endblock %}", """
<div class="card text-center">
    <h1>Welcome to Cognito Auth Demo</h1>
    <p>This is a simple demonstration of AWS Cognito authentication with Flask.</p>

    <div>
        <a href="/signin" class="btn">Sign In</a>
        <a href="/signup" class="btn btn-secondary">Sign Up</a>
    </div>
</div>
""")

SIGNUP_TEMPLATE = BASE_TEMPLATE.replace("{% block content %}{% endblock %}", """
<div class="card">
    <h2>Sign Up</h2>
    <p>This is a simplified signup form for demonstration.</p>
    <p>In the complete application, this would connect to AWS Cognito.</p>
</div>
""")

SIGNIN_TEMPLATE = BASE_TEMPLATE.replace("{% block content %}{% endblock %}", """
<div class="card">
    <h2>Sign In</h2>
    <p>This is a simplified signin form for demonstration.</p>
    <p>In the complete application, this would connect to AWS Cognito.</p>
</div>
""")


@app.route('/')
def index():
    """Home page route"""
    logger.info("Rendering index template...")
    try:
        return render_template_string(INDEX_TEMPLATE)
    except Exception as e:
        logger.error(f"Error rendering index template: {str(e)}")
        return f"Error rendering template: {str(e)}", 500


@app.route('/signup')
def signup():
    """Signup page route"""
    logger.info("Rendering signup template...")
    try:
        return render_template_string(SIGNUP_TEMPLATE)
    except Exception as e:
        logger.error(f"Error rendering signup template: {str(e)}")
        return f"Error rendering template: {str(e)}", 500


@app.route('/signin')
def signin():
    """Signin page route"""
    logger.info("Rendering signin template...")
    try:
        return render_template_string(SIGNIN_TEMPLATE)
    except Exception as e:
        logger.error(f"Error rendering signin template: {str(e)}")
        return f"Error rendering template: {str(e)}", 500


@app.route('/test')
def test():
    """Test route"""
    logger.info("Test route accessed")
    return "Simplified app is working!"


if __name__ == '__main__':
    logger.info("Starting simplified Flask application on port 5003...")
    app.run(debug=True, host='0.0.0.0', port=5003)
