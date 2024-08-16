import ollama
response = ollama.chat(
    model='gemma2:27b', 
    messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?'
        }
    ],
    options={
        "max_tokens": 256,
          "temperature": 0.3,
          "top_p": 0.9,
          "top_k": 40,
          "presence_penalty": 0.0,
          "frequency_penalty": 0.0,
          "repeat_penalty": 1.1,
          "mirostat_mode": 0,
          "mirostat_tau": 5.0,
          "mirostat_eta": 0.1
    }
)
print(response['message']['content'])