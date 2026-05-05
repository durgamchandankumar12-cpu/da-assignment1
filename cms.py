import pandas as pd
import numpy as np

class CMS:
    def __init__(self, w, d):
        self.w = w
        self.d = d
        self.table = np.zeros((d, w))

    def hash(self, x, i):
        return hash(str(x)+str(i)) % self.w

    def add(self, x):
        for i in range(self.d):
            self.table[i][self.hash(x,i)] += 1

    def estimate(self, x):
        return min(self.table[i][self.hash(x,i)] for i in range(self.d))

# Read dataset
df = pd.read_csv("datasets/access_log.csv", nrows=10000)

# 🔥 IMPORTANT: Get first column automatically
first_col = df.columns[0]

# Extract IP (first word of each row)
ips = df[first_col].astype(str).apply(lambda x: x.split()[0])

cms = CMS(200,5)

for ip in ips:
    cms.add(ip)

print("Top IP Estimates:")
for ip in ips.unique()[:10]:
    print(ip, cms.estimate(ip))