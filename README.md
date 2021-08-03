# ticket-viewer

Ticket Viewer is a CLI based application that displays Zendesk tickets.

### How to Install

1. Clone this github repo.
2. Set up a python virtual environment (venv) by running the following command:

   `$ python3 -m venv /path/to/new/virtual/environment`

3. Activate the virtual environment by running the following command (bash/zsh):

   `$ source <venv>/bin/activate`

   (Command might vary according to your shell, [official venv documentation can be found here](https://docs.python.org/3/library/venv.html))

4. Install the packages required to run this program by running the following command:

   `$ pip install -r requirements.txt`

5. Create a config.py file in the root of the project directory. The file should contain the following strings:

   `SUBDOMAIN = 'xxxxx'`

   `EMAIL = 'xxxxx'`

   `PASSWORD = 'xxxxx'`

   **Note: I have emailed my personal config.py file to Sabrina Ginter**

6. Start the Ticket Viewer CLI application by running the following command:

   `$ python3 app.py`
