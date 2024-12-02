# Magis Air ✈️
Prototype Web Application for Magis Air's booking system. Final requirement for ADMU's CSCI 41: Information Management.

<!-- <h3 align="center">
    🧑‍💻 Visit the site: <a href="" target="_blank">Magis Air </a> 🧑‍💻
</h3> -->

# Installation
1. Make a python virtual environment
    ```
    python -m venv .venv
    ```
2. Activate venv
    ```
    # Windows command prompt
    .venv\Scripts\activate.bat

    # Windows PowerShell
    .venv\Scripts\Activate.ps1

    # macOS and Linux
    source .venv/bin/activate
    ```
3. Install requirements
    ```
    pip install -r requirements.txt
    ```
4. Setup database
    ```
    \i 'SQL setup.sql'
    \i 'add data.sql'
    ```
5. Run the app locally
    ```
    streamlit run app.py
    ```


