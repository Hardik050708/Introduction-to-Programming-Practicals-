# Practical 2 - Practice Question 3: Discount and GST

price = 2500
discount = price * 0.10
gst = (price - discount) * 0.18  # GST applies after discount.
print(f"Discount: INR {discount:.2f}\nGST: INR {gst:.2f}\nNet bill: INR {price - discount + gst:.2f}")
