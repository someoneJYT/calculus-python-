import random
import math

# --- [設定參數] ---
num_series = 150  # 150組
length = 200      # 每組長度 200
low, high = 1, 100

# --- [1] 產生 150 組 AA 系列 (1*200) ---
# 使用隨機亂數產生 1~100 的均勻分布數列
AA_series = []
for _ in range(num_series):
    # 產生一組 200 個元素的隨機數列
    row = [random.uniform(low, high) for _ in range(length)]
    AA_series.append(row)

# 計算每一組 AA 的平均值和變異數 (儲存起來供最後檢查用)
aa_means = []
aa_vars = []
for row in AA_series:
    m = sum(row) / length
    v = sum((x - m) ** 2 for x in row) / length
    aa_means.append(m)
    aa_vars.append(v)

# --- [2] 加總成一組 BB (1*200) ---
# 初始化一個長度 200 的全 0 數列
BB = [0.0] * length
for j in range(length):
    for i in range(num_series):
        BB[j] += AA_series[i][j]

# --- [3] 計算 BB 的統計量與標準化 (CC) ---
# 計算 BB 的平均值
mean_BB = sum(BB) / length

# 計算 BB 的變異數 (修正這裡的錯誤：對 BB 數列進行迭代)
var_BB = sum((x - mean_BB) ** 2 for x in BB) / length
std_BB = math.sqrt(var_BB)

# 產生 CC 系列 (Normalization: 調整成 zero-mean, unit-variance)
CC = [(x - mean_BB) / std_BB for x in BB]

# --- [4] 繪製文字直方圖 (驗證分佈) ---
def draw_hist(data, title, bins=12):
    print(f"\n{'='*20} {title} {'='*20}")
    min_val, max_val = min(data), max(data)
    rng = max_val - min_val
    hist = [0] * bins
    
    for x in data:
        # 計算該數值落在哪個箱子(bin)
        idx = int((x - min_val) / rng * (bins - 1)) if rng > 0 else 0
        hist[idx] += 1
    
    # 找出最大數量用來做比例縮放
    max_h = max(hist)
    for i in range(bins):
        # 根據比例畫出星號
        bar_length = (hist[i] * 40) // max_h if max_h > 0 else 0
        bar = '*' * bar_length
        print(f"區間 {i+1:2d}: {bar} ({hist[i]})")

# 顯示分佈差異
draw_hist(AA_series[0], "Original Sequence (AA[0]) - Uniform Distribution")
draw_hist(CC, "Final Normalized Result (CC) - Normal Distribution")

# --- [5] 檢查一致性 (對應投影片 [3]) ---
print("\n" + "="*50)
print("統計一致性檢查報告 (Verification Report)")
print("-" * 50)
print(f"1. BB 系列直接計算的平均值:    {mean_BB:.4f}")
print(f"2. 各組 AA 平均值累加的總和:   {sum(aa_means):.4f}")
print("-" * 50)
print(f"3. BB 系列直接計算的變異數:    {var_BB:.4f}")
print(f"4. 各組 AA 變異數累加的總和:   {sum(aa_vars):.4f}")
print("-" * 50)
print(f"5. CC 標準化後的平均值 (應為0): {sum(CC)/length:.4f}")
print(f"6. CC 標準化後的變異數 (應為1): {sum((x - (sum(CC)/length))**2 for x in CC)/length:.4f}")
print("=" * 50)