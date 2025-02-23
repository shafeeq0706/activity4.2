from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to fetch main options
def get_main_options():
    conn = sqlite3.connect('categories.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM main_options")
    main_options = cursor.fetchall()
    conn.close()
    return main_options

# Function to fetch sub option details based on main_option_id
def get_sub_option_details(main_option_id):
    conn = sqlite3.connect('categories.db')
    cursor = conn.cursor()
    cursor.execute("SELECT eligibility, access, duration FROM sub_options WHERE main_option_id=?", (main_option_id,))
    sub_option = cursor.fetchone()
    conn.close()
    return sub_option

@app.route('/', methods=['GET', 'POST'])
def index():
    main_options = get_main_options()  # Get the main options from the DB
    sub_option = None

    if request.method == 'POST':
        try:
            main_option_id = int(request.form['main_option_id'])  # Get selected ID from the form
            sub_option = get_sub_option_details(main_option_id)  # Get the sub option details for the selected ID
        except ValueError:
            error_message = "Invalid input, please select a valid user category."
            return render_template('index.html', main_options=main_options, error_message=error_message)

    return render_template('index.html', main_options=main_options, sub_option=sub_option)

if __name__ == '__main__':
    app.run(debug=True)
