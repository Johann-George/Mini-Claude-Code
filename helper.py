import json
from call_function import available_functions, call_function

def generate_content(client, messages, verbose):

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=available_functions,
    )

    if (response.usage is None):
        raise RuntimeError("Failed API Request")

    message = response.choices[0].message 

    if message.tool_calls:
        messages.append(message.model_dump(exclude_none=True))

        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose)
            messages.append(result_message)

            if not result_message['content']:
                raise TypeError("The LLM response is None")

            if verbose:
                print(f"-> {result_message['content']}")
    else:
        print("Response: ", message.content)
        return

    return messages


