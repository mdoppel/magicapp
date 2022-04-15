from FLASKAPP.application import application

if __name__ == "__main__":
    db.create_all()
    application.run(debug=True)