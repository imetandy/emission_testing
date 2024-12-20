import numpy as np
import matplotlib.pyplot as plt


class AMM:
    def __init__(self, ec_reserve, gc_reserve):
        self.ec_reserve = ec_reserve  # Amount of Endcoin in the pool
        self.gc_reserve = gc_reserve  # Amount of Gaiacoin in the pool
        self.k = ec_reserve * gc_reserve  # Constant product of reserves * base SST

    def get_endcoin_price(self):
        """Returns the price of Endcoin in terms of Gaiacoin."""
        return self.gc_reserve / self.ec_reserve

    def get_gaiacoin_price(self):
        """Returns the price of Gaiacoin in terms of Endcoin."""
        return self.ec_reserve / self.gc_reserve

    def get_endcoin_reserve(self):
        """Returns the amount of Endcoin in the pool."""
        return self.ec_reserve

    def get_gaiacoin_reserve(self):
        """Returns the amount of Gaiacoin in the pool."""
        return self.gc_reserve

    def trade(self, input_token, token_type='ec'):
        """
        Simulate a trade. If token_type is 'ec', it means the user is providing Endcoin to buy Gaiacoin.
        If token_type is 'gc', it means the user is providing Gaiacoin to buy Endcoin.
        """
        if token_type == 'ec':
            new_ec_reserve = self.ec_reserve + input_token
            new_gc_reserve = self.k / new_ec_reserve
            self.ec_reserve = new_ec_reserve
            self.gc_reserve = new_gc_reserve
        elif token_type == 'gc':
            new_gc_reserve = self.gc_reserve + input_token
            new_ec_reserve = self.k / new_gc_reserve
            self.gc_reserve = new_gc_reserve
            self.ec_reserve = new_ec_reserve


def simulate_trades(amm, trades, token_type='ec'):
    prices = []
    for trade in trades:
        amm.trade(trade, token_type)
        prices.append(amm.get_price())

    return prices


coin_map = {'ec': 'Endcoin', 'gc': 'Gaiacoin'}

n_trades = 100  # play about with this number to simulate a number of trades

amm = AMM(1000, 1000)  # initialise the AMM with 1000 Endcoin and 1000 Gaiacoin

# Simulate 1000 random trades
trades = np.random.randint(1, 100, n_trades)  # Random trade sizes
coin_types = np.random.choice(['ec', 'gc'], n_trades)  # Random coin types

ec_prices = []
ec_reserve = []
gc_prices = []
gc_reserve = []

for trade, coin_type in zip(trades, coin_types):
    ec_prices.append(amm.get_endcoin_price())
    ec_reserve.append(amm.get_endcoin_reserve())
    gc_prices.append(amm.get_gaiacoin_price())
    gc_reserve.append(amm.get_gaiacoin_reserve())

    other_coin = 'gc' if coin_type == 'ec' else 'ec'

    print(f'User is trading {trade} {coin_map[coin_type]} for {coin_map[other_coin]}')
    amm.trade(trade, coin_type)  # make the trade

fig, ax = plt.subplots(2, 1, figsize=(10, 10))
ax[0].plot(ec_prices, label='Endcoin Price')
ax[0].plot(gc_prices, label='Gaiacoin Price')
ax[0].set_xlabel('Trade Number')
ax[0].set_ylabel('Price')
ax[0].legend()

ax[1].plot(ec_reserve, label='Endcoin Reserve')
ax[1].plot(gc_reserve, label='Gaiacoin Reserve')
ax[1].set_xlabel('Trade Number')
ax[1].set_ylabel('Reserve')
ax[1].legend()

plt.tight_layout()
plt.show()

# As the Endcoin Reserve decreases, the value of Endcoin increases.
# As the Gaiacoin Reserve increases, the value of Gaiacoin decreases.
# At the start there is more Endcoin and Less Gaiacoin, so the price of Endcoin is lower and the price of Gaiacoin is higher.
