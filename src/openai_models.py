#from openai import OpenAI
from openai import AzureOpenAI
def employee_info_chatbot(model_engine, added_messages, info):

    client = AzureOpenAI(api_key="4d165b8e531c49ec8ac0c256aa73d4bd", api_version="2024-02-01", azure_endpoint = "https://azo-iknow-ku-eus-01.openai.azure.com/")
    #client = OpenAI()

    # Construct the prompt using formatted strings
    system_prompt = f"""You're a useful assistant that helps employees find information about the company,
                        their status in the company or make requests. I fthey make a request that is not just
                        finding information and that requires additional information for it to be processed
                        you will ask them that required information.
                    """

    messages = [
    {"role": "system",
     "content": system_prompt}
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

    return response

def employee_sensitive_info_chatbot(model_engine, added_messages, info):

    client = AzureOpenAI(api_key="4d165b8e531c49ec8ac0c256aa73d4bd", api_version="2024-02-01", azure_endpoint = "https://azo-iknow-ku-eus-01.openai.azure.com/")
    #client = OpenAI()

    # Construct the prompt using formatted strings
    messages = [
    {"role": "system",
     "content": "You're a useful assistant that helps employees know if certain information about them is available for them to see. This could be 401k, PTO balance amounts etc"}
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

    return response
