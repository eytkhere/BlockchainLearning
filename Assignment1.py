from __future__ import annotations

import hashlib


class Hasher:
    """
    Class that allows initiation of different types of hash methods.
    """
    def __init__(self, hashType: str = "sha256") -> None:
        if not hasattr(hashlib, hashType.casefold()):
            raise ValueError(f'Unsupported hash function: {hashType}')
        self.hashType = hashType
        self.lastHash = None

    def hash(self, data: str) -> str:
        """
        ::
            Function that hashes the input data using the selected algorithm.

            Input:
                data (str): The data wanted to be hashed.

            Return:
                (str):      The data after being hashed by the algorithm.
        """
        hashFunction = getattr(hashlib, self.hashType)
        self.lastHash = hashFunction(data.encode()).hexdigest()
        return self.lastHash

    def __call__(self, data: str) -> str:
        """
        ::
            Function that allows the instance to be called like a function.

            Return:
                (str): The hashed data.
        """
        return self.hash(data)

    def __str__(self) -> str:
        """
        ::
            Function that returns the last computed hash as a string.

            Return:
                (str): The last hashed data.
        """
        return self.lastHash if self.lastHash else "No hash computed yet"
