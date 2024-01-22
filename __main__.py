from server import app, db

if __name__ == "__main__":
  # DB Setup
  app.app_context().push()
  db.create_all()
  
  # Launch App
  app.run(debug=True)
