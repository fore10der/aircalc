from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync

class NotificationConsumer(JsonWebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            f'group-{self.scope["user"].id}',
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        print("Closed websocket with code: ", close_code)
        async_to_sync(self.channel_layer.group_discard)(
            f'group-{self.scope["user"].id}',
            self.channel_name
        )
        self.close()

    def load_success(self, event):
        self.send_json(
            {
                'type': 'load.success',
                'content': event['content']
            }
        )
    
    def report_success(self, event):
        self.send_json(
            {
                'type': 'report.success',
                'content': event['content']
            }
        )