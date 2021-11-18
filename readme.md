# Demo App
---

For Run this Application

1. change the name of `.env.example` to `.env` and give the values for Env variables
2. Create Virual environment using 
    ```python -m venv venv``` on windows
    `python3 -m venv venv` on linux and mac
3. Activate Virtual env
    `venv\Scripts\activate` on windows
    `source venv\bin\activate` on linux and mac

4. Install Requirements
    `pip install -r requirements.txt`

5. Set Flask app env variable
    `set FLASK_APP=app` on windows
    `export Flask_APP=app` on linux and mac
6. Run the Application by running the command `flask run`