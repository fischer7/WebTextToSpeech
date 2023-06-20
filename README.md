# Installation and Execution Guide
This guide explains how to install the required dependencies in a virtual environment (venv) and how to run the provided Python code.

## Installation
Please follow the steps below to install the necessary requirements inside a virtual environment:

1. Make sure you have Python installed on your system. If Python is not installed, you can download and install it from the official Python website (https://www.python.org).

2. Open a terminal or command prompt.

3. Create a new directory for your project (optional, but recommended for organization purposes) and navigate to it using the cd command.

4. Create a virtual environment by executing the following command:

    ```shell
    python -m venv myenv
    ```

5. This will create a new directory named myenv, which contains the virtual environment files.

6. Activate the virtual environment. The commands to activate the virtual environment depend on your operating system:

    - On Windows:

        ```shell
        myenv\Scripts\activate
        ```
    - On macOS and Linux:

        ```shell
        source myenv/bin/activate
        ```
6. With the virtual environment activated, you can proceed to install the required packages. Execute the following command:

``` shell
pip install -r requirements.txt
```
This will install the necessary dependencies: pyttsx3, selenium, and beautifulsoup4.

7.Additionally, you need to have the Chrome browser installed on your system. If it is not installed, please download and install Chrome from the official website (https://www.google.com/chrome/).

### Running the Code
Once you have completed the installation steps, you can run the provided Python code. Here's how:

1. Ensure that your virtual environment is still activated.

2. Open a text editor or an integrated development environment (IDE) of your choice.

    2.1. If you are using VS Code, just press f5 and run the file: text_to_speech.py

3. Execute the Python script by running the following command:

```shell
python text_to_speech.py
```

4. This will run the script and start processing the web page located at "https://platform.openai.com/docs/guides/gpt-best-practices". The script extracts visible text from the page and converts it to speech using the pyttsx3 library.

5. As the script runs, it will print the current index and the spoken text to the console. The synthesized speech will also be audible if your system's audio is enabled.

6. Wait for the script to complete its execution. It will stop automatically after reading all the visible text on the web page.

