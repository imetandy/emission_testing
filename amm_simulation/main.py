import uuid
from emitter import Emitter
from trader import Trader
from pool import Pool
from climate_fund import ClimateFund

# Create EC <-> SOL, GC <-> SOL and EC <-> GC pools
ec_gc_pool = Pool(pool_name='pool1', tokenA='EC', tokenB='GC', pool_ratio=2/3, fee=0)
ec_sol_pool = Pool(pool_name='pool2', tokenA='EC', tokenB='SOL', pool_ratio=1, fee=0)
gc_sol_pool = Pool(pool_name='pool3', tokenA='GC', tokenB='SOL', pool_ratio=1, fee=0)

climate_fund = ClimateFund()
emitter = Emitter()

traders = [Trader(id=uuid.uuid4(),
                contributer='Y',
                ec_balance=1000,
                gc_balance=1000,
                sol_balance=1000)]

daily_ec, daily_gc = emitter.emit()
print('Daily EC emission:', daily_ec)
print('Daily GC emission:', daily_gc)

climate_fund.fund += emitter.climate_fund()
print('Amount added to the climate fund:', emitter.climate_fund())
print('Total climate fund:', climate_fund.fund)

# Distribute EC and GC to the traders
daily_ec_per_trader = daily_ec / len(traders)
daily_gc_per_trader = daily_gc / len(traders)

print(f'Distributing {daily_ec_per_trader} EC to each trader')
print(f'Distributing {daily_gc_per_trader} GC to each trader')

print('Trader 0 initial EC balance:', traders[0].ec_balance)
print('Trader 0 initial GC balance:', traders[0].gc_balance)

for trader in traders:
    trader.ec_balance += daily_ec_per_trader
    trader.gc_balance += daily_gc_per_trader

print('Trader 0 EC balance after emission:', traders[0].ec_balance)
print('Trader 0 GC balance after emission:', traders[0].gc_balance)
print('Trader 0 SOL balance after emission:', traders[0].sol_balance)

print('Swapping 100 EC for GC in ec_gc_pool')

traders[0].swap_tokens(pool=ec_gc_pool,
                       token_in='EC',
                       token_out='GC',
                       amount_in=100)

print('Trader 0 EC balance after swap:', traders[0].ec_balance)
print('Trader 0 GC balance after swap:', traders[0].gc_balance)
print('Trader 0 SOL balance after swap:', traders[0].sol_balance)