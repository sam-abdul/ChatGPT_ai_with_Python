import openai

openai.api_key = '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'

def ask_question(question):
    prompt = f"Question: {question}\nAnswer:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )

    answer = response.choices[0].text.strip()
    return answer

while True:
    user_question = input("Enter your question (or 'q' to quit): ")

    if user_question.lower() == 'q':
        break

    answer = ask_question(user_question)

    print(answer)
