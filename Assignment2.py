from __future__ import annotations

from datetime import datetime
from Assignment1 import Hasher
from dataclasses import dataclass


@dataclass
class Block:
    """
    ::
        The most basic and fundamental class in a blockchain -> literally the block.
        Composed of a data, index of block (in chain), hashed block, previousBlock (hash), timestamp.
    """
    data: str
    index: int = 0
    previousHash: str = "0"
    instHash: str = "0"
    nonce: int = 0
    timestampInstBlock: float = datetime.timestamp(datetime.now())
    _hashInst: Hasher = Hasher()

    @property
    def blockHash(self) -> str:
        """
        ::
            A function that computes the block's hash dynamically when accessed.

            Return:
                (str): The hash of the block with a dynamic change whenever any data of the block is changed.
        """
        return self._hashInst.hash(self.data+str(self.index) +
                                            self.previousHash+ str(self.timestampInstBlock) + str(self.nonce))

    def __repr__(self) -> str:
        return (f'data: {self.data}, index: {self.index}, '
                f'previousHash: {self.previousHash}, timestamp: {self.timestampInstBlock}, blockHash: {self.blockHash}')
