import pandas as pd
import sys

def dedup (input_file, output_file, method):
    last_occ = {}

    df = pd.read_csv(input_file)
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="ISO8601")
    threshold = pd.Timedelta(milliseconds=4)
    dedup_rows = []
    dups = 0
    for i, (sym, time, price) in enumerate(zip(df["symbol"], df["timestamp"], df["price"])):
        if (sym not in last_occ):
            dedup_rows.append([sym, time, price, 1])
        else:
            if (abs(time - dedup_rows[last_occ[sym] - dups][1]) <= threshold):
                if (method == "last"):
                    dedup_rows[last_occ[sym] - dups][2] = price
                elif (method == "highest"):
                    if price > dedup_rows[last_occ[sym] - dups][2]:
                        dedup_rows[last_occ[sym] - dups][2] = price
                elif method == "average":
                    dedup_rows[last_occ[sym] - dups][2] += price
                    dedup_rows[last_occ[sym] - dups][3] += 1
                else:
                    raise ValueError ("Method must be 'last', 'highest', or 'average'")
                dups += 1
                continue
            else:
                dedup_rows.append([sym, time, price, 1])

        last_occ[sym] = i

    if method == "average":
        for i in range (len(dedup_rows)):
            dedup_rows[i][2] /= dedup_rows[i][3]
    
    deduped_df = pd.DataFrame(dedup_rows, columns=["symbol", "timestamp", "price", "count"])
    deduped_df.drop(columns=["count"], inplace=True)
    deduped_df.to_csv(output_file, index=False)




if __name__ == "__main__":
    if (len(sys.argv) != 4):
        raise ValueError ("Enter input file, output file and method")
    
    dedup(sys.argv[1], sys.argv[2], sys.argv[3])
