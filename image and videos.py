
import os
import shutil

# Your exact path from the screenshot
my_folder = r"D:\backup Asus rgu\Darling\202504__"

def start_cleaning():
    # Check if Python can actually see the folder
    if not os.path.exists(my_folder):
        print("I can't find that folder. Is the D: drive plugged in?")
        return

    all_items = os.listdir(my_folder)
    print(f"I found {len(all_items)} items. Starting work...")

    for item in all_items:
        item_path = os.path.join(my_folder, item)

        if os.path.isfile(item_path):
            # .lower() makes sure we catch .JPG and .jpg
            name_lower = item.lower()
            
            # 1. DELETE COPIES
            if "copy" in name_lower:
                os.remove(item_path)
                print(f"DELETED: {item}")
            
            # 2. MOVE IMAGES & IPHONE DATA (.AAE)
            elif name_lower.endswith((".jpg", ".jpeg", ".png", ".aae")):
                folder = os.path.join(my_folder, "My_Images")
                os.makedirs(folder, exist_ok=True)
                shutil.move(item_path, os.path.join(folder, item))
                print(f"MOVED IMAGE: {item}")
            
            # 3. MOVE VIDEOS (I saw these in your screenshot!)
            elif name_lower.endswith((".mp4", ".mov", ".m4v")):
                folder = os.path.join(my_folder, "My_Videos")
                os.makedirs(folder, exist_ok=True)
                shutil.move(item_path, os.path.join(folder, item))
                print(f"MOVED VIDEO: {item}")

start_cleaning()
