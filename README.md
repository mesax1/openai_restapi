# openai_restapi
Django Restful API that communicates with OpenAI API via POST

A Restful API written in Django that communicates with OpenAI API via POST

## Overall Installation

* First ensure you have python 3 installed. If not, get python [here](https://www.python.org). Preferably Python 3.10.

* Install virtualenv:

    ```bash
        pip install virtualenv
    ```

* Then, Git clone this repo to your PC

    ```bash
        git clone https://github.com/mesax1/openai_restapi.git
    ```
    
* #### Dependencies installation
    1. Cd into your cloned repo:
        ```bash
            cd openai_restapi
        ```
    2. Create and activate a virtual environment:
        ```bash
            virtualenv  venv -p python3
            source venv/bin/activate
        ```
    3. Install all the required dependencies:
        ```bash
            pip install -r requirements.txt
        ```
    4. Run the Django migrations of the project
        ```bash
            python manage.py makemigrations
            python manage.py migrate
        ```
* #### Generate and use your own OpenAI API Key
    Login into your OpenAI account (or create an account if you don't have one yet)
   
    [https://platform.openai.com/](https://platform.openai.com/)

    Access your API keys

    [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
    
    Click on + Create new secret key

    Copy the API key temporarily into a .txt file or somewhere where you can copy it later.

    * ##### On Windows
    Run the following in the cmd prompt, replacing <yourkey> with your OpenAI API key:
    ```bash
        setx OPENAI_API_KEY “<yourkey>”
    ```
    Open a new cmd prompt, validate that the environment variable has been set by typing
    ```bash
        echo %OPENAI_API_KEY%
    ```

    * ##### On Linux
    Run the following in the terminal, replacing <yourkey> with your OpenAI API key:
    ```bash
        echo "export OPENAI_API_KEY='yourkey'" >> ~/.zshrc
    ```
    Update the shell variable
    ```bash
        source ~/.zshrc
    ```
    Open a new terminal, validate that the environment variable has been set by typing
    ```bash
        echo $OPENAI_API_KEY
    ```
* #### Launch API and use it
    Launch the server using:
    ```bash
        python manage.py runserver
    ```
    Access the API service on your browser by using
    ```
        http://localhost:8000/chat-free/
    ```
* #### Make a POST request
    The POST request requires at least 2 inputs: model and prompt.
   * **model** can be either
    ``` text
        "gpt-3.5-turbo-0301"
    ```
    or
    ``` text
        "text-davinci-003"
    ```
    
    * **prompt** would be the question that you would like to ask to the AI
    ``` text
        "¿Que precio tiene el kellogs?"
    ```
    
    *Some additional parameters can be sent in the POST request, that affect the execution of the AI model.
    * Example of a prompt with multiple optional parameters
    ```text
        {
        "model": "gpt-3.5-turbo-0301",
        "prompt": "Respondeme cualquier cosa en francés, en 1 párrafo",
        "temperature": 1.0,
        "max_tokens": 200,
        "frequency_penalty": 1,
        "presence_penalty": 1
    }
    ```
