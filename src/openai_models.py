from openai import OpenAI

def employee_info_chatbot(model_engine, user_prompt, info):

    # Replace with your desired model
    client = OpenAI()

    # Construct the prompt using formatted strings

    prompt = f"""You need to answer what the user asks based on the following information: {info}
                 the user says: {user_prompt}
              """

    system_prompt = f"""You're a useful assistant that helps employees find information about the company,
                        their status in the company or make requests. I fthey make a request that is not just
                        finding information and that requires additional information for it to be processed
                        you will ask them that required information.
                    """

    messages = [
    {"role": "system",
     "content": system_prompt},
    {"role": "user",
     "content": prompt}
    ]


    response = client.chat.completions.create(
        model=model_engine,
        messages=messages,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )

    response = response.choices[0].message.content

    #print(response)
    #print("Adult Rewrite Response " + str(count))
    return response

def employee_sensitive_info_chatbot(model_engine, user_prompt, info):

    # Replace with your desired model
    client = OpenAI()

    # Construct the prompt using formatted strings

    prompt = f"""You need to answer what the user asks based on the following information: {info}
                 the user says: {user_prompt}
              """

    messages = [
    {"role": "system",
     "content": "You're a useful assistant that helps employees know if they can certain information about them is available fro them to see. This could be 401k, PTO balance amounts etc"},
    {"role": "user",
     "content": prompt}
    ]


    response = client.chat.completions.create(
        model=model_engine,
        messages=messages,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )

    response = response.choices[0].message.content

    #print(response)
    #print("Adult Rewrite Response " + str(count))
    return response
