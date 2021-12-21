def create_routes(app):
    @app.route('/hello')
    def hello():
        return f"Hello, World!"
