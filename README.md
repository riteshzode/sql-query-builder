# SQL Query Builder

This is a web application that generates SQL code based on a user's input using OpenAI's GPT-3.5 model. The application
uses the Gradio library to create a user-friendly interface, allowing users to input a paragraph of text and receive SQL
code as output.

## Getting Started

1. Register for an API key from OpenAI.

   ```https://openai.com/```

2. Create a .env file in the project directory and add your API key as follows:

   ```OPENAI_API_KEY=YOUR_API_KEY```

3. Install the required packages:

   ```pip install -r requirements.txt```

4. Run the script main.py:

   ```python main.py```

5. Access the web application at http://localhost:7860 in your browser.

## How to Use

1. Enter a paragraph of text that describes the desired SQL query in the "Enter SQL raw text" input field.

2. Click on the "Submit" button to generate SQL code based on the input.

3. The SQL code will be displayed in the "Output" section below the input field.

4. You can try the application with different input text to get different SQL code.

Note: The quality of the generated SQL code may vary based on the complexity of the input text and the capabilities of
the GPT-3.5 model.