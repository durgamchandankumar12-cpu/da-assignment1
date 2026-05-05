import pandas as pd

# Load dataset (limit rows for speed)
df = pd.read_csv("datasets/Reviews.csv", nrows=5000)

print("Columns:", df.columns)
print(df[['Text']].head())

# 🔹 Step 1: Shingling
def shingles(text, k=5):
    text = str(text)
    return set([text[i:i+k] for i in range(len(text)-k+1)])

# 🔹 Step 2: MinHash
def minhash(shingle_set, num_hash=50):
    signatures = []
    for i in range(num_hash):
        min_val = min(hash(str(s)+str(i)) for s in shingle_set)
        signatures.append(min_val)
    return signatures

# 🔹 Step 3: Similarity
def similarity(sig1, sig2):
    count = sum(1 for i in range(len(sig1)) if sig1[i] == sig2[i])
    return count / len(sig1)

# 🔹 Compare two reviews
text1 = df['Text'][0]
text2 = df['Text'][1]

print("\nReview 1:", text1[:100])
print("\nReview 2:", text2[:100])

# Create shingles
s1 = shingles(text1)
s2 = shingles(text2)

# Create signatures
sig1 = minhash(s1)
sig2 = minhash(s2)

# Calculate similarity
sim = similarity(sig1, sig2)

print("\nSimilarity Score:", sim)