from application import application, db

if __name__ == "__main__":
    db.create_all()
    application.run(debug=True)