# Practical 9 - Practice Question 4: Bill function

# Apply discount first, then add GST to the discounted price.
def bill_amount(price, discount, gst):
    after_discount = price * (1 - discount / 100)
    return after_discount * (1 + gst / 100)

print(f"Final bill: INR {bill_amount(2500, 10, 18):.2f}")
