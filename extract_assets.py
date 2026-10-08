import os
from PIL import Image

brain_uploaded = r"C:\Users\kopan\.gemini\antigravity-ide\brain\02ee0aa9-2293-48b5-bee0-ee9f3b1c60fd\.user_uploaded"
assets_dir = r"C:\Users\kopan\.gemini\antigravity-ide\scratch\aqua-bandhu\static\assets"
os.makedirs(assets_dir, exist_ok=True)

# List images
for fname in os.listdir(brain_uploaded):
    path = os.path.join(brain_uploaded, fname)
    if fname.lower().endswith(('.jpg', '.png', '.jpeg')):
        im = Image.open(path)
        print(f"{fname}: size={im.size}, format={im.format}")

# Load reference 2 (approved visual assets)
# media_1791365399892.jpg is the approved assets board
ref2_path = os.path.join(brain_uploaded, "media_1791365399892.jpg")
if os.path.exists(ref2_path):
    im2 = Image.open(ref2_path)
    W, H = im2.size
    print(f"Ref2 asset sheet size: {W}x{H}")
    
    # We can crop individual approved assets based on proportions of the grid:
    # Asset Sheet Layout:
    # Top Left (0-48% W, 0-16% H): Prawns / Shrimp
    #   Vannamei (0-8% W), Tiger Prawns (8-16%), Fresh Prawns (16-24%), Cooked (24-32%), Black Tiger (32-40%), Head-on (40-48%)
    # Top Right (49-100% W, 0-16% H): Fish
    #   Tilapia (50-58%), Seabass (58-66%), Pomfret (66-74%), Rohu (74-82%), Catla (82-90%), King Fish (90-99%)
    # Row 2 Left (0-42% W, 17-32% H): Crab & Others
    #   Blue Crab, Mud Crab, Snow Crab, Lobster, Squid, Octopus
    # Row 2 Middle (43-71% W, 17-32% H): Shellfish
    #   Mussels, Oysters, Clams, Scallops
    # Row 2 Right (72-100% W, 17-32% H): Other Seafood
    #   Pangasius, Tuna, Mahi Mahi, Snapper
    # Row 3 Left (0-40% W, 33-50% H): Aqua Farm Imagery (Ponds, Aerators, Nets, Farmer with Harvest)
    # Row 3 Middle (40-100% W, 33-50% H): Workers (Farmer, Worker, Quality Inspector, Warehouse Worker, Buyer, Logistics, Supplier)
    # Row 4 (0-40% W, 51-69% H): Warehouse & Processing
    # Row 4 (40-79% W, 51-69% H): Trucks & Transport
    # Row 4 (79-100% W, 51-69% H): Ships & Logistics
    # Row 5 (0-100% W, 70-83% H): Logistics & Status Icons
    # Row 6 (0-100% W, 84-100% H): Charts, AI Robot, Tech, Environment
    
    crops = {
        "vannamei_prawns.jpg": (0.01, 0.04, 0.09, 0.15),
        "tiger_prawns.jpg": (0.09, 0.04, 0.17, 0.15),
        "fresh_prawns.jpg": (0.17, 0.04, 0.25, 0.15),
        "cooked_prawns.jpg": (0.25, 0.04, 0.33, 0.15),
        "black_tiger_prawns.jpg": (0.33, 0.04, 0.41, 0.15),
        "tilapia.jpg": (0.51, 0.04, 0.60, 0.15),
        "seabass.jpg": (0.60, 0.04, 0.68, 0.15),
        "pomfret.jpg": (0.68, 0.04, 0.76, 0.15),
        "rohu.jpg": (0.76, 0.04, 0.83, 0.15),
        "catla.jpg": (0.83, 0.04, 0.91, 0.15),
        "kingfish.jpg": (0.91, 0.04, 0.99, 0.15),
        "blue_crab.jpg": (0.01, 0.20, 0.08, 0.31),
        "mud_crab.jpg": (0.08, 0.20, 0.15, 0.31),
        "snow_crab.jpg": (0.15, 0.20, 0.22, 0.31),
        "lobster.jpg": (0.22, 0.20, 0.28, 0.31),
        "squid.jpg": (0.28, 0.20, 0.35, 0.31),
        "octopus.jpg": (0.35, 0.20, 0.42, 0.31),
        "oysters.jpg": (0.50, 0.20, 0.58, 0.31),
        "scallops.jpg": (0.64, 0.20, 0.71, 0.31),
        "tuna.jpg": (0.78, 0.20, 0.86, 0.31),
        
        # Farm imagery
        "shrimp_farm_ponds.jpg": (0.01, 0.36, 0.11, 0.50),
        "aerators_in_pond.jpg": (0.11, 0.36, 0.21, 0.50),
        "fish_farming_nets.jpg": (0.21, 0.36, 0.31, 0.50),
        "farmer_with_harvest.jpg": (0.31, 0.36, 0.40, 0.50),
        
        # People
        "farmer_portrait.jpg": (0.41, 0.36, 0.48, 0.50),
        "farm_worker.jpg": (0.48, 0.36, 0.56, 0.50),
        "quality_inspector.jpg": (0.56, 0.36, 0.65, 0.50),
        "warehouse_worker.jpg": (0.65, 0.36, 0.74, 0.50),
        "buyer_portrait.jpg": (0.74, 0.36, 0.82, 0.50),
        "logistics_staff.jpg": (0.82, 0.36, 0.91, 0.50),
        "supplier_portrait.jpg": (0.91, 0.36, 0.99, 0.50),
        
        # Warehouse & Transport
        "cold_storage_warehouse.jpg": (0.01, 0.55, 0.10, 0.68),
        "processing_plant.jpg": (0.10, 0.55, 0.20, 0.68),
        "packaging_sorting.jpg": (0.20, 0.55, 0.30, 0.68),
        "ice_storage.jpg": (0.30, 0.55, 0.40, 0.68),
        "refrigerated_truck.jpg": (0.41, 0.55, 0.52, 0.68),
        "cold_chain_truck.jpg": (0.52, 0.55, 0.62, 0.68),
        "delivery_van.jpg": (0.62, 0.55, 0.70, 0.68),
        "container_truck.jpg": (0.70, 0.55, 0.79, 0.68),
        "cargo_ship.jpg": (0.80, 0.55, 0.90, 0.68),
        "port_shipping.jpg": (0.90, 0.55, 0.99, 0.68),
        
        # Tech
        "ai_robot.jpg": (0.50, 0.85, 0.58, 0.98),
        "ai_dashboard.jpg": (0.58, 0.85, 0.72, 0.98),
        "ocean_background.jpg": (0.87, 0.85, 0.99, 0.98)
    }
    
    for name, (x1, y1, x2, y2) in crops.items():
        box = (int(x1 * W), int(y1 * H), int(x2 * W), int(y2 * H))
        cropped = im2.crop(box)
        out_p = os.path.join(assets_dir, name)
        cropped.save(out_p, quality=92)
        print(f"Saved asset: {name} ({cropped.size})")

# Also copy reference images for reference modal or direct inspection
import shutil
shutil.copy(os.path.join(brain_uploaded, "media_1791365303094.jpg"), os.path.join(assets_dir, "reference_dashboards.jpg"))
shutil.copy(os.path.join(brain_uploaded, "media_1791365399892.jpg"), os.path.join(assets_dir, "reference_assets.jpg"))
shutil.copy(os.path.join(brain_uploaded, "media_1791365469369.jpg"), os.path.join(assets_dir, "reference_warehouse.jpg"))
print("Done extracting and organizing assets!")
