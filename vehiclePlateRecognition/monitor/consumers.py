import json, logging
from urllib.parse import parse_qs
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from channels.layers import get_channel_layer


POSSIBLE_GROUPS = frozenset(["agent", "monitor"])

log_format = '%(asctime)s---%(levelname)s---%(filename)s---%(message)s'
logging.basicConfig(filename='tcc.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)
logger = logging.getLogger('root')


agents = dict()

class monitorConsumer(AsyncWebsocketConsumer):

    async def connect(self):        
        self.params = parse_qs(self.scope["query_string"].decode()) #pega o query_string        
        self.group = self.params.get('group', 'no_suplied')[0] #guarda o grupo (monitor). [0] pega só o nome sem os ['']
        self.name = self.params.get('name', 'no_suplied')[0] # guarda o name (id)
        self.room_group_name = self.group        

        if self.group in POSSIBLE_GROUPS and self.name != 'Not Supplied': 
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept() #aceita a conexão
                        
            if self.group == 'agent':
                camera_running = int(self.params.get('camera_running', ('0'))[0])
                agents[self.name] = camera_running
                logger.info(f'=====> AGENTS {agents}')
                logger.info(f'=====> agents_name {agents[self.name]}')
                await self.channel_layer.group_send("monitor", {
                    'type': 'send_message',
                    "event": "agent-connect",
                    'who': self.name, 
                    'camera_running': camera_running
                })
                
            elif self.group == 'monitor':
                logger.info(f'=====> AGENTS_inventory {agents.items()}')
                await self.channel_layer.group_send(self.room_group_name, {
                    'type': 'send_message',
                    "event": "inventory",
                    'agents': list(agents.items())
                })

        else:
            await self.close()

        
    async def disconnect(self, close_code):
        if self.group == 'agent':

            await self.channel_layer.group_send('monitor', {
                    'type': 'send_message',
                    "event": "agent-disconnect",
                    'who': self.name
                })

            del agents[self.name]

            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )


    async def receive(self, text_data): 
        
        response = json.loads(text_data)
        self.event = response.get("event", None)
        logger.info(f'=====> tag_slug {text_data}')
        
        if self.event == 'agent-update':
                message = response.get("camera_running", None)
                tag_slug = response.get("who", None)
                camera_running = response.get("camera_running", None)
                agents[self.name] = camera_running
                logger.info(f'=====> AGENTS_list_update {agents}')
                await self.channel_layer.group_send("monitor", {
                    'type': 'send_message',
                    "event": "agent-update",
                    'who': tag_slug,
                    'message': message
                })        

        if self.event == 'stop-request':
                tag_slug = response.get("message", None)
                await self.channel_layer.group_send("agent", {
                    'type': 'send_message',
                    "event": "stop-request",
                    'message': tag_slug
                })
                
        
        if self.event == 'ask-processing-rate':
                message = response.get("message", None)
                monitor_id = response.get("target", None)
                await self.channel_layer.group_send("agent", {
                    'type': 'send_message',
                    "event": "processing-rate-request",
                    'who': monitor_id,
                    'message': message
                })

        if self.event == 'agent-processing-rate':
            monitor_id = response.get("target", None)
            tag_slug = response.get("who", None)
            processing_rate = response.get("processing_rate", None)
            await self.channel_layer.group_send("monitor", {
                'type': 'send_message',
                "event": "agent-processing-rate",
                'target': monitor_id,
                'who': tag_slug,
                'message': processing_rate
            })

        if self.event == 'stop-agent':
            monitor = response.get("target-groups", None)
            tag_slug = response.get("who", None)
            camera_running = response.get("camera_running", None)
            await self.channel_layer.group_send("monitor", {
                'type': 'send_message',
                "event": "stop-agent",
                'target-groups': monitor,
                'who': tag_slug,
                'camera_running': camera_running
            })
        
        
    async def send_message(self, msg):
        await self.send(text_data=json.dumps({
            "payload": msg
        }))



