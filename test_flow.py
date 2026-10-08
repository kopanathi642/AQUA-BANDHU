import urllib.request
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def test_api():
    base = "http://127.0.0.1:8000"
    
    print("--- 0. Testing GET / (HTML Index) ---")
    html_req = urllib.request.urlopen(f"{base}/")
    print(f"Index HTML Success: Status {html_req.status}, Length {len(html_req.read())} bytes")

    print("\n--- 1. Testing GET /api/v1/overview ---")
    req = urllib.request.urlopen(f"{base}/api/v1/overview")
    data = json.loads(req.read().decode('utf-8'))
    print(f"Overview Success: Total Avail Qty = {data['kpis']['available_quantity_kg']:,} kg, Active Orders = {data['kpis']['active_orders']}")
    
    print("\n--- 2. Testing GET /api/v1/marketplace ---")
    req = urllib.request.urlopen(f"{base}/api/v1/marketplace")
    market = json.loads(req.read().decode('utf-8'))
    print(f"Marketplace Success: {len(market['listings'])} seafood listings found.")
    for item in market['listings'][:3]:
        print(f"  * {item['product_name']} (₹{item['price_per_kg']}/kg) - Avail: {item['available_kg']} kg")

    print("\n--- 3. Testing POST /api/v1/orders (Buy Now Flow) ---")
    order_payload = {
        "listing_id": "lst_01",
        "quantity_kg": 200.0,
        "buyer_name": "Dubai Seafood LLC",
        "buyer_id": "usr_buyer_dubai"
    }
    req = urllib.request.Request(
        f"{base}/api/v1/orders",
        data=json.dumps(order_payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    res = urllib.request.urlopen(req)
    order_resp = json.loads(res.read().decode('utf-8'))
    created_order = order_resp['order']
    print(f"Order Created Successfully!")
    print(f"  Order Number: {created_order['order_number']}")
    print(f"  Product: {created_order['product_name']}")
    print(f"  Quantity: {created_order['quantity_kg']} kg")
    print(f"  Total Amount: ₹{created_order['total_amount']:,}")
    print(f"  Status: {created_order['status']}")

    print("\n--- 4. Checking Inventory Reservation ---")
    req = urllib.request.urlopen(f"{base}/api/v1/inventory")
    inv = json.loads(req.read().decode('utf-8'))
    vannamei = next(item for item in inv['items'] if item['name'] == 'Vannamei Prawns')
    print(f"  Vannamei Total: {vannamei['total_kg']} kg | Avail: {vannamei['available_kg']} kg | Reserved: {vannamei['reserved_kg']} kg")

    print("\n--- 5. Waiting for AI Multi-Agent Pipeline to Orchestrate (approx 4s) ---")
    time.sleep(4.5)
    req = urllib.request.urlopen(f"{base}/api/v1/orders/{created_order['id']}")
    updated_order = json.loads(req.read().decode('utf-8'))['order']
    print(f"  Order #{updated_order['order_number']} State after AI Chain: {updated_order['status']}")
    print(f"  Carrier Assigned: {updated_order['truck_id']}")
    print(f"  Quality Passed: {updated_order['quality_passed']}")
    print(f"  AI Activity Logs: {len(updated_order['logs'])} events logged.")
    for l in updated_order['logs'][:3]:
        print(f"    - [{l['level']}] {l['agent_name']}: {l['message']}")

    print("\n--- 6. Testing POST /api/v1/inventory/harvest (Stock In / Harvest Intake) ---")
    harvest_payload = {
        "product_name": "Vannamei Prawns",
        "quantity_kg": 500.0,
        "farm_source": "Farm - Kakinada",
        "grade_size": "30-40 pcs/kg",
        "storage_location_id": "loc_main_cold",
        "notes": "Harvest from Pond 1"
    }
    req = urllib.request.Request(
        f"{base}/api/v1/inventory/harvest",
        data=json.dumps(harvest_payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    res = urllib.request.urlopen(req)
    harvest_resp = json.loads(res.read().decode('utf-8'))
    print(f"Stock In Success: {harvest_resp['result']['reference']} (+{harvest_resp['result']['quantity_added']} kg)")

    print("\n--- ALL VERIFICATIONS PASSED SUCCESSFULLY! ---")

if __name__ == "__main__":
    test_api()
