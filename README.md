# getblockdata

First you'll need to install jgarzik's python-bitcoinrpc with:

    git clone https://github.com/jgarzik/python-bitcoinrpc
    python setup.py install 

You'll also need to run your node with these in the bitcoin.conf file:

    server=1
    listen=1
    txindex=1
    rpcallowip=127.0.0.1
    rpctimeout=30
    rpcuser=rpcusername
    rpcpassword=chooserpcpassword

If you don't usually run with `txindex=1`, then when you restart it you'll need to run with `-reindex` as well, and it will take about 24 hours (depending on CPU) to rebuild your index, and you'll have all transactions on the blockchain indexed after it's done.
Then, make a blank `blockchain.txt` file in your python folder. And then you can run the program.
