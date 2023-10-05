from website import create_app

# INITIALIZE WEB APPLICATION 
app = create_app()

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=8000)
    