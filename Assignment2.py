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
    previousHash: str = None
    _hashInst = Hasher()
    timestamp: float = datetime.timestamp(datetime.now())

    @property
    def blockHash(self) -> str:
        """
        ::
            A function that implements @property that computes the block's hash dynamically when accessed.

            Return:
                (str): The hash of the block with a dynamic change whenever any data of the block is changed.
        """
        return self._hashInst.hash(self.data+str(self.index)+self.previousHash+str(self.timestamp))
