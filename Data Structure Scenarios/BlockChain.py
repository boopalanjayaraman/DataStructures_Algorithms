import hashlib
import datetime

class Block():
    def __init__(self, timestamp, data, previous_hash, previous = None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = previous
        self.hash = self.calc_hash()

    def calc_hash(self, verification = False):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8'))
        sha.update(self.data.encode('utf-8'))
        if verification == True:
            if self.previous_block != None:
                sha.update(self.previous_block.calc_hash(verification).encode('utf-8'))
        else:
            if self.previous_hash != None:
                sha.update(self.previous_hash.encode('utf-8'))

        return sha.hexdigest()

    def __str__(self):
        content = ''
        content =  'Data: ' + self.data + '\n'
        content += 'Time: ' + self.timestamp + '\n'
        content += 'Hash: ' + str(self.hash) + '\n'
        content += 'Previous Hash: ' + str(self.previous_hash) + '\n'
        return content


class BlockChain():
    def __init__(self):
        self.tail = None

    def add(self, block_data):
        if self.tail == None:
            new_block = Block(datetime.datetime.now().isoformat(), block_data, previous_hash=None)
            self.tail = new_block
        else:
            previous_hash = self.tail.hash
            previous_node = self.tail
            new_block = Block(datetime.datetime.now().isoformat(), block_data, previous_hash=previous_hash, previous = previous_node)
            self.tail = new_block

    def get(self, index):
        block = self.tail
        block_index = 0
        last_block = None
        while(block != None):
            if(block_index == index):
                return block
            last_block = block
            block = block.previous_block
            block_index += 1 
        return last_block

    def length(self):
        if(self.tail == None):
            return 0
        block = self.tail
        block_count = 0
        while(block != None):
            block_count += 1 
            block = block.previous_block
        
        return block_count

    def is_valid(self):
        """
        Checks the chain of blocks for any possible modification in the hash value
        If there is a mismatch between assigned hash value and calculated hash value, 
        then it returns False and the relevant block which failed to match
        """
        if(self.tail == None):
            return (True, None)
        block = self.tail
        while(block != None):
            if block.hash != block.calc_hash(verification=True):
                return (False, block)
            block = block.previous_block
        return (True, None)

    def __str__(self):
        content = ''
        index = 0
        block = self.tail
        while(block != None):
            content += 'Block ' + str(index) + ':\n'
            content += str(block)
            block = block.previous_block
            index += 1
        return content

if __name__ == "__main__":

    blockchain = BlockChain()
    print(blockchain) #prints empty string

    blockchain.add("First Transaction | Sender: A | Receiver: B | Value: 10")
    blockchain.add("Second Transaction | Sender: A | Receiver: B | Value: 100")
    blockchain.add("Third Transaction | Sender: B | Receiver: S | Value: 40")
    blockchain.add("Fourth Transaction | Sender: S | Receiver: B | Value: 20")
    blockchain.add("Fifth Transaction | Sender: B | Receiver: A | Value: 45")

    print(blockchain) #prints five blocks and their relevant hashes

    print(blockchain.length()) #prints 5

    print(blockchain.get(2)) #prints third transaction details

    print(blockchain.is_valid()) #prints True

    modify_block = blockchain.get(2)
    modify_block.data = 'Third Changed Transaction | Sender: B | Receiver: S | Value: 400'

    print(blockchain) #prints five blocks and their relevant hashes. Hashes still match because they are unchanged. But is_valid will fail below.

    print(blockchain.is_valid()) #prints False