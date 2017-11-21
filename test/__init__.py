import xvector as xvector
from xvector import ApiConfig

# auth_token = "54e299fd09634522bd0aa91ecc96c860"
api_key="60f4321055bb45a7b55b0a97385fc576"
base_url = "http://localhost:5000"
version = "api"
ApiConfig.set_api_base(base_url)
# ApiConfig.set_auth_token(auth_token)
# ApiConfig.set_version(version)
ApiConfig.set_api_key(api_key)
b = xvector.get_data_list()
print(b)
# c = xvector.get_metadata("4f7a461a-0ea1-434b-8aa5-c6e85fdfd2ed")
# print(c)
# d = xvector.get_table("4f7a461a-0ea1-434b-8aa5-c6e85fdfd2ed",rows=4000,page=1)
# print(d['df_stats'])
