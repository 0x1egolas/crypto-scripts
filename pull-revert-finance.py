import requests
import pandas as pd
import json

def run():
    params = {
        'sort': 'apr',
        'page': 0,
        'desc': True,
        'limit': 100,
        'offset': 0,
        'active': True 
    }
    url = 'https://staging-api.revert.finance/v1/positions/mainnet/uniswapv3'
    data = []
    while True:
        if params['page'] % 5 == 0:
            print(f"getting page {params['page']}")

        try:
            res = requests.get(url, params)
        except:
            print(trace.format_exc())
            break
        data.extend(res.json()['data'])
        params['page'] += 1
        params['offset'] += params['limit']
        if params['offset'] > res.json()['total_count']:
            break
    with open('data.json', 'w+') as f:
        f.write(json.dumps({'data': data}))

if __name__ == "__main__":
    run()
