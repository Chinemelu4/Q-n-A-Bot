# Q&A Bot

This is a simple Q&A Bot built using Streamlit and the OpenAI language model. The purpose of this project is to provide a user-friendly interface for interacting with the OpenAI language model to generate responses to user questions.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/Q-n-A-Bot.git
   cd Q-n-A-Bot
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key by creating a `.env` file in the project directory and adding your key:

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the Streamlit app using the following command:

```bash
streamlit run app.py
```

Access the Q&A Bot interface in your web browser at [http://localhost:8501](http://localhost:8501).

## How to Use

1. Input your question in the text box provided.
2. Click the "Submit" button to generate an answer.
3. The bot will display the generated answer based on the input question.

## Example

![Q&A Bot Interface](/images/qa_bot_interface.png)

### Use Case

Let's say you have a set of questions related to a specific topic, and you want quick and accurate responses. You can use this Q&A Bot to streamline the process. For instance:

1. **Question:** "What is the capital of France?"
   
   **Bot Response:** "The capital of France is Paris."

2. **Question:** "Who wrote 'Romeo and Juliet'?"

   **Bot Response:** "The play 'Romeo and Juliet' was written by William Shakespeare."

Feel free to customize the code and adapt it to your specific use case or integrate it into other projects that require natural language understanding.
