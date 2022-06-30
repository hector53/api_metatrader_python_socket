#Api creada por Héctor Acosta :D
import json
import zmq

class apiMT:
    def __init__(self):
        self.version: str = '1' 
        self.message: str = ''

    def Connect(self, port: int = 2345) -> bool:
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(f"tcp://127.0.0.1:{port}")
    
    def send_msg(self, msg: str=''):
        self.socket.send_string(msg)
        self.message = self.socket.recv()   
        return self.message.decode()
    
    def get_balance(self):
        balance = self.send_msg("code_1")
        return balance

    def get_candles(self, symbol: str='GBPUSD', periodo: int = 1, start: int = 0, end: int = 100):
        candles = self.send_msg(f"code_2_symbol_{symbol}_periodo_{periodo}_start_{start}_end_{end}")
        converToJson = json.loads(candles.replace("'", '"'))
        return converToJson

    def send_order(self, symbol: str='GBPUSD', type:int = 0, lotaje:float = 0.01, slipage:int = 0, 
                    sl:int=0, tp:int=0, comment:str =''):
        order = self.send_msg(f"code_3_symbol_{symbol}_type_{type}_lotaje_{lotaje}_slipage_{slipage}_sl_{sl}_tp_{tp}_comment_{comment}")
        converToJson = json.loads(order.replace("'", '"'))
        return converToJson

    def close_order(self, order:int = 0):
        order = self.send_msg(f"code_4_order_{order}")
        converToJson = json.loads(order.replace("'", '"'))
        return converToJson

    def get_open_positions_total(self):
        totalOpens = self.send_msg(f"code_5")
        return int(totalOpens)
    
    def get_order_history_by_id(self, id:int = 0):
        order = self.send_msg(f"code_6_order_{id}")
        #print("respuesta", order)
        converToJson = json.loads(order.replace("'", '"'))
        return converToJson


