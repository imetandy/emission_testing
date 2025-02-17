class Pool:
    def __init__(self,
                 pool_name: str,
                 tokenA: str,
                 tokenB: str,
                 pool_ratio: float = 1.0,
                 fee: float = 0):
        """
        A Swap pool for token A -> token B, where a trader can swap token A for token B and vice versa
        at a given pool ratio and fee.

        Args:
            pool_name (str): the name of the pool to identify it
            tokenA (str): token A
            tokenB (str): token B
            pool_ratio (float): the pool ratio of token A to token B
            fee (float): the fee for swapping token A for token B. This is in SOL
        """
        self.pool_name = pool_name
        self.tokenA = tokenA
        self.tokenB = tokenB
        self.fee = fee
        self.a_to_b_ratio = pool_ratio
        self.b_to_a_ratio = 1 / pool_ratio