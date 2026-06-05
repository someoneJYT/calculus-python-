import math
import random

# ==========================================
# 1. Box-Muller 演算法核心（純內建功能實作）
# ==========================================
def generate_box_muller_data(num_samples):
    gaussian_samples = []
    
    # 因為一次轉換可以產生兩個相互獨立的高斯分布數值 (X 和 Y)
    # 我們跑一半的循環次數即可得到所需總量
    for _ in range(num_samples // 2):
        # random.random() 會產生 [0.0, 1.0) 的隨機浮點數
        # 為了避免 math.log(0) 出錯，如果抽到 0 就重新抽一次
        u1 = random.random()
        while u1 == 0:
            u1 = random.random()
        u2 = random.random()
        
        # 核心數學公式
        r = math.sqrt(-2 * math.log(u1))
        theta = 2 * math.pi * u2
        
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        
        gaussian_samples.extend([x, y])
        
    return gaussian_samples

# 設定產生 5000 個高斯分布隨機數
samples = generate_box_muller_data(5000)


# ==========================================
# 2. 用純文字在終端機繪製「統計直方圖」
# ==========================================
print("\n" + "="*60)
print("  Box-Muller 產生的數列分布概況 (文字統計直方圖)  ")
print("="*60)

# 設定直方圖的區間 (Bins) 數量與範圍（高斯分布大多落在 -3 到 +3 之間）
num_bins = 20
min_val, max_val = -3.0, 3.0
bin_width = (max_val - min_val) / num_bins

# 初始化每個區間的計數器
bins = [0] * num_bins

# 將數值歸類到對應的區間中
for val in samples:
    if min_val <= val < max_val:
        index = int((val - min_val) / bin_width)
        bins[index] += 1

# 找出最高的區間數量，用來等比例縮放圖表寬度（最多顯示 40 個字元寬）
max_count = max(bins)
scale = 40 / max_count if max_count > 0 else 1

# 逐行印出直方圖
for i in range(num_bins):
    bin_start = min_val + i * bin_width
    bin_end = bin_start + bin_width
    
    # 將計數轉換為星號 (*) 的數量
    stars = "*" * int(bins[i] * scale)
    
    # 格式化輸出：顯示區間範圍與分佈長條
    print(f"[{bin_start:5.2f} : {bin_end:5.2f}] | {stars}")

print("="*60)
print(f" 統計說明：總共取樣 {len(samples)} 個點。")
print(" 圖表可見中間 (0.00 附近) 數據最多，向兩側對稱遞減，符合高斯分布。")
print("="*60)