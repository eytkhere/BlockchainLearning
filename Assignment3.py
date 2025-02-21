from __future__ import annotations


from Assignment2 import Block

class Blockchain:
    """
    ::
        The very beggining of a blockchain. The Blockchain class chains the blocks
        and continuosly adds new blocks the chain as requested.
    """
    def __init__(self):
        self.chain = [self._createGenesisBlock()]
        self.difficulty = 4
        self.blockReward = None

    @classmethod
    def _createGenesisBlock(cls) -> Block:
        """
        ::
            Create the very first block (genesis). classmethod.

            Return:
                genesisBlock (Block): Returns the first block of a chain after initialization.
        """
        genesisBlock = Block("Genesis Block")
        return genesisBlock

    def addBlock(self, data: str) -> None:
        """
        ::
            Function that adds a new block to the chain.

            Parameters:
                data (str): Data being saved on new block.
        """
        lastBlock = self.chain[-1]
        newBlock = Block(data)
        newBlock.index = int(lastBlock.index) + 1
        newBlock.previousHash = lastBlock.instHash
        self.chain.append(newBlock)

    def proofOfWork(self, block: Block) -> bool:
        """
        ::
            Function that ensures that blocks require effort to be added are met.

            Parameters:
                block (Block): The block that needs to be verified - usually the new block being added to the chain.
            Return:
                (bool):        Once the proof of work is verified the function returns true.

        """
        recalculateHash = block.blockHash
        while recalculateHash[0:4] != "0" * self.difficulty:
            block.nonce += 1
            recalculateHash = block.blockHash
        block.instHash = recalculateHash
        return True

    def __repr__(self) -> str:
        lastBlock = self.chain[-1]
        return f'index: {lastBlock.index}, last Hash: {lastBlock.instHash}'
