from django.shortcuts import render
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import MQTTData
from .serializers import MQTTDataSerializer
from datetime import datetime
from .consumers import *
import websocket

# Create your views here.

def dashboard(request):
    channel_layer = get_channel_layer()
    print(channel_layer)
    async_to_sync(channel_layer.group_send)("dashboard_updates", {"type": "send.update","data": {"timestamp":"6-10-2023","value":50}})
    return render(request, 'dashboard.html')

def chec(request):
    channel_layer = get_channel_layer()
    timestamp=datetime.now().strftime("%d-%m-%Y")
    # async_to_sync(channel_layer.group_send)("dashboard_updates", {"type": "send.notification","data": {"timestamp":timestamp,"value":50}})
    # async_to_sync(channel_layer.group_send)("dashboard_updates", {"type": "send.update","data": {"timestamp":timestamp,"value":50}})
    # async_to_sync(channel_layer.group_send)("dashboard_updates", {"type": "send_update","data": {"timestamp":timestamp,"value":50}})
    # async_to_sync(channel_layer.group_send)("dashboard_updates", {"type": "send_notification","data": {"timestamp":timestamp,"value":50}})
    websocket_url = "ws://127.0.0.1:8000/ws/dashboard/"

    # Create a WebSocket connection
    ws = websocket.WebSocket()

    # Connect to the WebSocket 
    print("before")
    ws.connect(websocket_url)
    print("after")

    # Define the data you want to send
    data = {
        "timestamp": timestamp,
        "value": 50
    }

    # Convert the data to a JSON string
    data_json = json.dumps(data)

    # Send the data to the WebSocket server
    ws.send(data_json)

    # Close the WebSocket connection when done
    ws.close()
    # das=DashboardConsumer()
    # das.send_update({"data":{"timestamp":timestamp,"value":50}})
    return JsonResponse({"data":{"timestamp":timestamp,"value":50}},status=200)

# @async_to_sync
# async def mqtt_consumer(message):
#     data = message['data']
#     await message.reply_channel.send({
#         'type': 'send_data',
#         'data': data,
#     })

# @async_to_sync
# async def send_data(message):
#     data = message['data']
#     timestamp = data['timestamp']
#     value = data['value']

#     # Save MQTT data to the database
#     MQTTData.objects.create(timestamp=timestamp, value=value)

#     # Broadcast data to WebSocket clients
#     channel_layer = get_channel_layer()
#     await channel_layer.group_send("mqtt_data", {
#         'type': 'display_data',
#         'data': data,
#     })
