import grpc

import event_pb2
import event_pb2_grpc

"""
Simulates user mobiles sending coordinates to gRPC
"""

print("Coordinates sending...")

channel = grpc.insecure_channel("127.0.0.1:5005")
stub = event_pb2_grpc.ItemServiceStub(channel)

# Update this with desired payload
user_coordinates = event_pb2.EventCoordinatesMessage(
    userId=300,
    latitude=-100,
    longitude=30
)

user_coordinates_2 = event_pb2.EventCoordinatesMessage(
    userId=400,
    latitude=-100,
    longitude=30
)

response_1 = stub.Create(user_coordinates)
response_2 = stub.Create(user_coordinates_2)


print("Coordinates sent...")
print(user_coordinates, user_coordinates_2)