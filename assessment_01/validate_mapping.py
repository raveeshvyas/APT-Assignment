import pandas as pd


mapping = pd.read_json("mapping.json")
df = pd.read_csv("02_sample_data_with_fabricated_columns.csv")

for col in df.columns:
    df.rename(columns={col : mapping[col]["mapping"]}, inplace=True)
    

open = df["open"]
high = df["high"]
low = df["low"]
close = df["close"]
price = df["price"]
volumne = df["volume"]

def check_volume():
    is_integer = (df["volume"] % 1 == 0).all()
    other_cols = df.drop(columns=["volume"])
    is_larger = (df["volume"] > other_cols.max(axis=1)).all()
    assert(is_integer and is_larger)

    print("Volume check passed")

def check_high():
    for o, h, l, c in zip(open, high, low, close):
        assert(h > o and h > l and h > c)
    
    print("High check passed")

def check_low():
    for o, h, l, c in zip(open, high, low, close):
        assert(l < o and l < h and l < c)
    
    print("Low check passed")

def check_open_close():
    for o, h, l, c in zip(open, high, low, close):
        assert(o > l and o < h)
        assert(c > l and c < h)
    
    print("Open and close checks passed")

check_volume()
check_high()
check_low()
check_open_close()

print("All tests passed")

