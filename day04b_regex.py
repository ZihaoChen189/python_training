import re

message = "MeshAnything: Artist-Created Mesh Generation with Autoregressive Transformers"

result = re.match("with", message)
print(result)

result_1 = re.search("with", message)
print(result_1)
print(result_1.span())
print(result_1.group())


