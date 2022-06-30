from apiMetatrader import apiMT  #importar api
mt = apiMT() #instanciar api
mt.Connect(port=9999)  #conectar api con metatrader a traves del puerto xxxx usando sockets

#get velas, obtiene velas desde la posicion 0 hasta "x" vela anterior en este ejemplo 500 velas
#candles = mt.get_candles(symbol="GBPUSD", periodo=5, start=0, end=500); 
#print(len(candles))#imprimo la cantidad q trae el array
#print(candles[0])#solo imprimo la primera
#output
#500
#{'time': '2022.05.13 16:40', 'open': 1.21677, 'high': 1.21696, 'low': 1.21634, 'close': 1.21679, 'volume': 254}


#buy or sell
#type 0 = buy, type 1 = sell
#tp y sl estan en ticks , ese valor se sumara o restara al openprice
#order buy 
#order = mt.send_order(symbol='GBPUSD', type=0, lotaje=0.1, slipage=10, sl=500, tp=500, comment='enviando buy')
#order sell
#order = mt.send_order(symbol='GBPUSD', type=1, lotaje=0.1, slipage=10, sl=500, tp=500, comment='enviando sell')
#print(order)
#output
#{'order': 372606562, 'openPrice': 1.2173, 'sl': 1.2223, 'tp': 1.2123, 'type': 1, 'lotaje': 0.1}


#close order by order id
#order = mt.close_order(372615870)
#print(order)
#output 
#{'status': 1, 'msg': 'order closed successfully'}



##get total opens
#totalOpens = mt.get_open_positions_total()
#print("total opens ", totalOpens)

#get order history by id 
#order = mt.get_order_history_by_id(364400783)
#output 
#total opens  4

#get balance 
balance = mt.get_balance()
print(balance)
#output 
#17320.78000000