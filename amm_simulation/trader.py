import uuid
import json
from typing_extensions import Literal
from datetime import datetime
from pool import Pool


class Trader:
    def __init__(self,
                 id: uuid,
                 contributer: Literal["Y", "N"],
                 ec_balance: float = 0,
                 gc_balance: float = 0,
                 sol_balance: float = 0):
        """
        A trader class to keep track of the balances of the trader.

        Args:
            id (uuid): Unique identifier for the trader
            contributer (Literal['Y', 'N']): Climate contributer identifier
            ec_balance (float): Amount of Endcoin the trader has
            gc_balance (float): Amount of Gaiacoin the trader has
            sol_balance (float): Amount of Solana the trader has
        """
        self.id = id
        self.contributer = contributer
        self.ec_balance = ec_balance
        self.gc_balance = gc_balance
        self.sol_balance = sol_balance

    def swap_tokens(self,
                    pool: Pool,
                    token_in: Literal['EC', 'GC'],
                    token_out: Literal['EC', 'GC'],
                    amount_in: float):
        """
        Swaps tokens in a pool.

        Args:
            pool (Pool): Pool to swap tokens in.
            token_in (Literal['EC', 'GC', 'SOL']): Token to swap in.
            token_out (Literal['EC', 'GC', 'SOL']): Token to swap out.
            amount_in (float): Amount of token_in to swap.
        """
        if token_in not in [pool.tokenA, pool.tokenB] or token_out not in [pool.tokenA, pool.tokenB]:
            raise ValueError(f"Invalid token pair {token_in} -> {token_out} for pool {pool.pool_name}")

        ratio = pool.a_to_b_ratio if token_in == pool.tokenA else pool.b_to_a_ratio

        self.sol_balance -= pool.fee # Deduct fee from sol balance

        amount_in_with_fee = amount_in * (1 - pool.fee)
        amount_out = amount_in_with_fee * ratio

        if token_in == 'EC':
            self.ec_balance -= amount_in
            self.gc_balance += amount_out
        elif token_in == 'GC':
            self.gc_balance -= amount_in
            self.ec_balance += amount_out

        self.log_swap(token_in, token_out, amount_in)

    def log_swap(self, token_in: Literal['EC', 'GC'],
                 token_out: Literal['EC', 'GC'],
                 amount_in: float):
        """
        Logs the swap details.
        Args:
            token_in (Literal['EC', 'GC']): Token swapped in.
            token_out (Literal['EC', 'GC']): Token swapped out.
            amount_in (float): Amount of token_in swapped.
        """
        swap_log = {
            'trader_id': str(self.id),
            'trade_time': datetime.now().isoformat(),
            'token_in': token_in,
            'token_out': token_out,
            'amount_in': amount_in,
            'gc_balance': self.gc_balance,
            'ec_balance': self.ec_balance,
            'sol_balance': self.sol_balance,
        }

        with open('logs/swap_log.json', 'r') as f:
            logs = json.load(f)

        logs.append(swap_log)

        with open('logs/swap_log.json', 'w') as f:
            json.dump(logs, f, indent=4)


# if __name__ == '__main__':
#     trader = Trader(id=uuid.uuid4(),
#                     contributer='Y',
#                     ec_balance=1000,
#                     gc_balance=1000,
#                     sol_balance=1)
#
#     # create a pool
#     ec_gc_pool = Pool(pool_name='pool1', tokenA='EC', tokenB='GC', pool_ratio=2/3, fee=0.00005)
#
#
#     print(trader.ec_balance)
#     print(trader.gc_balance)
#     print(trader.sol_balance)
#
#     trader.swap_tokens(pool=ec_gc_pool, token_in='EC', token_out='GC', amount_in=100)
#     print('After swap')
#     print(trader.ec_balance)
#     print(trader.gc_balance)
#     print(trader.sol_balance)
