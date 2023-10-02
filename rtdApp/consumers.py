import json
from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer

class DashboardConsumer(WebsocketConsumer):
    def connect(self):
        # Add the client to the "dashboard_updates" group
        self.group_name = "dashboard_updates"
        self.channel_layer.group_add(self.group_name, self.channel_name)
        self.accept()
        self.send(text_data=json.dumps({"timestamp":"5-10-2023","value":45}))

    def receive(self , text_data):
        print("DAta Received .......")
        print(text_data)
        self.channel_layer.group_send(
            self.group_name,
            {
                "type":"sendUpdate",
                "data":text_data
            }
        )
        # self.send(text_data=json.dumps(text_data))

    def disconnect(self, close_code):
        # Remove the client from the group when they disconnect
        self.channel_layer.group_discard(self.group_name, self.channel_name)

    def sendUpdate(self, event):
        print("update event gets called")
        data = event['data']
        print(data)

        # Send the real-time update to the WebSocket client
        self.send(text_data=json.dumps(data))

    def send_notification(self , event):
        print("Send Notification function get called")
        print(event)
        # print("The event value is" ,event.get('value'))
        data_values = event.get('value')
        # encoded_dict = data_values.encode()
        print("THis event data value will be send to the fronted and the event values are......." , data_values)
        # self.send(text_data = json.dumps({"payload" : data_values }))

        # self.send({
        #     # "type":"websocket.send",
        #     "text": "encoded_dict" ,
        #     })
        
        self.send(text_data=json.dumps({"data" : data_values}))

# class DashboardConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#         await self.send(text_data=json.dumps({"timestamp":"5-10-2023","value":45}))

#     async def disconnect(self, close_code):
#         pass

#     async def send_update(self, event):
#         print(event)
#         data = event['data']

#         # Send the real-time update to the WebSocket client
#         await self.send(text_data=json.dumps(data))
