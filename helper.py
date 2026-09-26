def generate_content(client, messages, verbose):

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
    )

    if (response.usage is None):
        raise RuntimeError("Failed API Request")

    if verbose:
        print("User prompt: ", arguments.user_prompt)
        print("Prompt tokens: ", response.usage.prompt_tokens)
        print("Response tokens: ", response.usage.completion_tokens)
        print("Response: ", response.choices[0].message.content)
    else:
        print("Response: ", response.choices[0].message.content)


