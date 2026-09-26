import json
from call_function import available_functions

def generate_content(client, messages, verbose):

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=available_functions,
    )

    if (response.usage is None):
        raise RuntimeError("Failed API Request")

    if verbose:
        print("User prompt: ", arguments.user_prompt)
        print("Prompt tokens: ", response.usage.prompt_tokens)
        print("Response tokens: ", response.usage.completion_tokens)
        print("Response: ", response.choices[0].message.content)
    else:
        message = response.choices[0].message 
        if message.tool_calls:
            for tool_call in message.tool_calls:
                function_args = json.loads(tool_call.function.arguments or "{}")
                print(f"Calling function: {tool_call.function.name}({function_args})")
        else:
            print("Response: ", message.content)


