from openai import OpenAI
from sklearn.metrics import mean_squared_error as mse

def get_embedding(text):
  client = OpenAI()
  response = client.embeddings.create(
      input = text,
      model= "text-embedding-3-large"
  )
  return response.data[0].embedding


def retrieve_info(input, info_embeddings, info_list):
  embedding = get_embedding(input)
  mse_list = []
  for i, item in enumerate(info_embeddings):
    mse_list.append([mse(item, embedding), i])
    
  sorted_list = sorted(mse_list, key=lambda x: x[0])
  index = sorted_list[0][1]
  result = info_list[index]
  return result
