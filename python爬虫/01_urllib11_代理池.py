proxies_pool = [
    {'http':'202.101.213.67:20419'},
    {'http':'202.101.215.69:20111'}
]

import random
proxies = random.choice(proxies_pool)

print(proxies)