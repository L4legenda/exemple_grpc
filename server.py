from concurrent import futures

import grpc

import data_pb2
import data_pb2_grpc


class DataServicer(data_pb2_grpc.DataHashServicer):
    def greeting(self, req, context):
        res = data_pb2.Text()
        print("res", req.data)
        res.data = "HASH"
        return res


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_DataHashServicer_to_server(DataServicer(), server)

    print("Server start on port 6066")
    server.add_insecure_port('[::]:6066')
    server.start()

    server.wait_for_termination()


if __name__ == "__main__":
    serve()