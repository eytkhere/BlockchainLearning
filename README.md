Assignment 1: Implementing a Hashing Utility Class

    Blockchain Concept: Cryptographic hash functions (SHA-256, Keccak, etc.).
    OOP Requirement:
        Create a Hasher class with methods for different hash algorithms (sha256, keccak256).
        Implement __call__ to make an instance callable like a function.
        Overload __str__ to return the last computed hash.

Assignment 2: Designing a Block Class with OOP Principles

    Blockchain Concept: Structure of a block (index, timestamp, data, previous hash).
    OOP Requirement:
        Define a Block class using @dataclass.
        Use a staticmethod to generate timestamps.
        Implement __repr__ for clean debugging output.
        Add a hash property that automatically updates when block data changes.

Assignment 3: Creating a Blockchain Class with Chain Validation

    Blockchain Concept: Chain integrity and linked blocks.
    OOP Requirement:
        Create a Blockchain class with an attribute chain (a list of Block objects).
        Implement a validate_chain method that checks for hash consistency.
        Use @classmethod to create a blockchain with a predefined genesis block.

Assignment 4: Implementing Proof of Work with an OOP Miner

    Blockchain Concept: Mining, nonce, and difficulty.
    OOP Requirement:
        Define a Miner class that takes a Blockchain instance and mines new blocks.
        Use @staticmethod to define a proof-of-work function.
        Implement an __iter__ method so the miner can yield new blocks continuously.
