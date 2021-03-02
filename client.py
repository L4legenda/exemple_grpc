import grpc

import data_pb2_grpc
import data_pb2
channel = grpc.insecure_channel("localhost:6066")
stub = data_pb2_grpc.DataHashStub(channel)
md5 = data_pb2.Text(data="hello")
res = stub.greeting(md5)
print(res.data)





