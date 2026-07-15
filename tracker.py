import requests
import time

BASE_RPC_URL = "https://mainnet.base.org"

def get_base_gas():
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_gasPrice",
        "params": [],
        "id": 1
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(BASE_RPC_URL, json=payload, headers=headers)
        result = response.json().get("result")
        if result:
            # تبدیل هگزادسیمال به gwei
            gas_price_wei = int(result, 16)
            gas_price_gwei = gas_price_wei / 1e9
            print(f"[Base Network] Gas Price: {gas_price_gwei:.4f} Gwei")
        else:
            print("Failed to fetch gas price from RPC.")
    except Exception as e:
        print(f"Error connecting to Base RPC: {e}")

if __name__ == "__main__":
    print("Starting Base Gas Tracker...")
    for _ in range(5):  # اسکن ۵ مرحله‌ای با فاصله ۵ ثانیه
        get_base_gas()
        time.sleep(5)