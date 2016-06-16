from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_btc = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%('rpc_user', 'rpc_password'))
blockchain = open('blockchain.txt', 'ab+') #you will need to make this blank file in your python folder before running the program
for i in range(1,416570,1): #the range of blocks to grab data for, in this case blocks 1 to 416570, incrementing 1 block at a time
        get_block_hash = rpc_btc.getblockhash(i)
        block = rpc_btc.getblock(get_block_hash)
        coinbase = rpc_btc.decoderawtransaction(rpc_btc.getrawtransaction(block['tx'][0]))
        value = coinbase['vout'][0]['value'] #this gets total block reward
        print(i)
        blockchain.write(str(block['height'])+', '+str(value)+', '+str(block['hash'])+', '+str(block['size'])+', '+str(len(block['tx']))+', '+str(block['version'])+', '+str(block['merkleroot'])+', '+str(block['time'])+', '+str(block['nonce'])+', '+str(block['bits'])+', '+str(block['difficulty'])+', '+str(block['chainwork'])+'\n')
blockchain.close()
print('done')
