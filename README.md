To recreate the db files:
run in python console from base dir:
    from flaskblog import create_app
    app = create_app()
    app.app_context().push()
    from flaskblog import db
    db.create_all()
