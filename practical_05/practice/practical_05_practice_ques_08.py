# Practical 5 - Practice Question 8: Stop at defective product

# Stop the inspection immediately when the first defective status is entered.
for product in range(1, 101):
    status = input(f"Product {product}/100 (ok/defective): ").strip().lower()
    if status == "defective":
        print("Inspection stopped at product", product)
        break
    print("Checked product", product)
else:
    print("All 100 products checked")
