from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = "YOUR_API_KEY"

# AI model configuration
models = {
    "GPT": "text-davinci-002",
    "Claude": "claude-v1",
    "GEMINI": "gemini-v1"
}

# Set the default model to GPT
default_model = "GPT"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json["prompt"]
    selected_model = request.json.get("model", default_model)

    # Get the model name based on the selection
    model_name = models.get(selected_model, models[default_model])

    # Send the user input to the AI model for processing
    response = openai.Completion.create(
        engine=model_name,
        prompt=user_input,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Get the generated response from the AI model
    ai_response = response.choices[0].text.strip()

    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)