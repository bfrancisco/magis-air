# Magis Air ✈️
Prototype Web Application for Magis Air's booking system. Final requirement for ADMU's CSCI 41: Information Management.

**Note that this prototype is only tested in Windows 10/11.**

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
5. Setup `secrets.toml` file
    - Rename `secrets.toml.example` to `secrets.toml`
    - Add your postgres password in the said file.
6. Run the app locally
    ```
    streamlit run app.py
    ```



