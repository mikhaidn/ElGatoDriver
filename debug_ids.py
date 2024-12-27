import hid

print("USB Devices found:")
for device in hid.enumerate():
    print(f"VID: 0x{device['vendor_id']:04x}, PID: 0x{device['product_id']:04x}")
    print(f"    Product: {device['product_string']}")
    print(f"    Manufacturer: {device['manufacturer_string']}")
    print("---")
