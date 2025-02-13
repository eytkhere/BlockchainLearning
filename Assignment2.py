from __future__ import annotations

import hashlib

from dataclasses import dataclass


@dataclass
class Block:
    """
    ::
        The most basic and fundamental class in a blockchain -> literally the block.
        Composed of a timestamp, data, index of block (in chain), previousBlock, hashed block.
    """
    timestamp: float
    data: str
    index: int = 0
    previousHash: str = None
    hashBlock: str = None
