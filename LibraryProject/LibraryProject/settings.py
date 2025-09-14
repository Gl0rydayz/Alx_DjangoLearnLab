# Set DEBUG to False in production
DEBUG = False

# Add secure browser-side protections
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enforce HTTPS for cookies
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Add allowed hosts for production
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Content Security Policy (CSP) middleware (optional)
INSTALLED_APPS += ['csp']  # Add django-csp if installed
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'")
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")