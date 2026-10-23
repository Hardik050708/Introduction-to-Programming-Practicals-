# Practical 5 - Practice Question 4: Skip damaged barcodes

# continue skips damaged -1 codes while keeping later scans.
barcodes = input("Barcodes separated by spaces (-1 = damaged): ").split()
for barcode in barcodes:
    if barcode == "-1":
        continue
    print("Scanned:", barcode)
