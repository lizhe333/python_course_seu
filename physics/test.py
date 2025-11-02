import pandas as pd
import matplotlib.pyplot as plt
import os

# --- 1. 设置参数 ---
# 换算系数 B(mT) = V_H(mV) / (K_H * I_s) = V_H(mV) / (10 * 5)
conversion_factor = 50.0

# --- 2. 定义所有要绘制的数据集 ---

# !! 关键修改点 !!
# 我们现在定义一个列表，其中包含每个数据集的详细信息
# 'filename': CSV 文件名
# 'position_col': 此数据集的位置列名
# 'voltage_col': 此数据集的电压列名
# 'label': 此数据集在图例中的标签

datasets_to_plot = [
    {
        'filename': '单线圈.csv',
        'position_col': 'Position (m) Run 1',
        'voltage_col': '霍尔电压 (mV) Run 1',
        'label': '单线圈'
    },
    {
        'filename': '双线圈.csv',
        'position_col': '位置 (米 m) 运行 1', # '双线圈.csv' 中的 '运行 1'
        'voltage_col': '霍尔电压 (mV) 运行 1',
        'label': '双线圈 (距离 d1)' # !!! 请根据实验情况修改 'd1'
    },
    {
        'filename': '双线圈.csv',
        'position_col': '位置 (米 m) 运行 2', # '双线圈.csv' 中的 '运行 2'
        'voltage_col': '霍尔电压 (mV) 运行 2',
        'label': '双线圈 (距离 d2)' # !!! 请根据实验情况修改 'd2'
    }
    # 如果你的 '双线圈.csv' 中还有 '运行 3' 等，请仿照上面的格式添加
]

# --- 3. 设置绘图 ---
# 设置 matplotlib 支持中文显示
try:
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 尝试使用 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
except Exception as e:
    print(f"设置中文字体失败: {e}. 可能会显示乱码。")
    plt.rcParams['font.sans-serif'] = ['sans-serif'] # 降级到通用字体
    plt.rcParams['axes.unicode_minus'] = False

# 创建一个图形和一个坐标轴
fig, ax = plt.subplots(figsize=(12, 8)) # 设置图像大小

# --- 4. 循环读取、处理和绘图 ---

files_processed = 0
# 用于缓存已读取的文件，避免重复读取
loaded_data = {}

for dataset in datasets_to_plot:
    
    filename = dataset['filename']
    position_col = dataset['position_col']
    voltage_col = dataset['voltage_col']
    label = dataset['label']
    
    try:
        # 检查文件是否存在
        if not os.path.exists(filename):
            print(f"警告：未找到文件 '{filename}'。将跳过数据集 '{label}'。")
            continue
        
        # 检查是否已加载此文件
        if filename not in loaded_data:
            print(f"正在读取文件: {filename}")
            loaded_data[filename] = pd.read_csv(filename)
        
        # 使用已加载的数据
        data = loaded_data[filename].copy() # 使用副本以防后续操作相互影响
        
        # 检查列是否存在
        if position_col not in data.columns or voltage_col not in data.columns:
            print(f"错误：文件 '{filename}' 中未找到所需的列 '{position_col}' 或 '{voltage_col}'。")
            print(f"    文件中找到的列为: {list(data.columns)}")
            print(f"    将跳过数据集 '{label}'。")
            continue
        
        # --- 数据处理 ---
        # 1. 解决数据类型问题：确保数据是数值型
        data[position_col] = pd.to_numeric(data[position_col], errors='coerce')
        data[voltage_col] = pd.to_numeric(data[voltage_col], errors='coerce')

        # 2. 删除转换失败的行
        data.dropna(subset=[position_col, voltage_col], inplace=True)
            
        # 3. 将位置从 (m) 转换为 (cm)
        # 两个文件的位置列单位都是 'm' 或 '米 m'，所以都乘以 100
        data['position_cm'] = data[position_col] * 100
        
        # 4. 转换电压为磁场强度 B (mT)
        data['magnetic_field_mT'] = data[voltage_col] / conversion_factor
        
        # 5. 确保数据按位置排序
        data = data.sort_values(by='position_cm')
        
        # --- 绘图 ---
        ax.plot(
            data['position_cm'],          # X轴：使用转换后的 cm 位置
            data['magnetic_field_mT'],    # Y轴：使用计算出的磁场强度
            marker='o',          # 'o' 表示用圆点标记每个数据点
            markersize=4,        # 标记点的大小
            linestyle='-',       # '-' 表示用实线连接数据点
            label=label          # 设置图例标签
        )
        print(f"已成功处理并绘制数据集: '{label}' (来自 {filename})")
        files_processed += 1

    except Exception as e:
        print(f"处理数据集 '{label}' 时发生严重错误: {e}")

# --- 5. 美化图表 ---

if files_processed == 0:
    print("错误：没有数据集被成功处理，无法生成图表。")
    print("请检查上述关于文件未找到或列名错误的警告/错误信息。")
else:
    # 设置图表标题和坐标轴标签 (并使用 LaTeX 格式化)
    # 我已根据你的偏好，为公式和单位添加了 LaTeX 标记
    ax.set_title(f'单线圈与双线圈轴线磁场分布 (线圈电流 $I_M = 0.5$ A)', fontsize=16)
    ax.set_xlabel('位置 $x$ (cm)', fontsize=12)
    ax.set_ylabel('磁场强度 $B$ (mT)', fontsize=12)
    
    # 添加图例
    ax.legend(fontsize=10)
    
    # 添加网格
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # 添加中心线（x=0）
    ax.axvline(x=0, color='gray', linestyle='--', linewidth=1)
    
    # --- 6. 保存图表 ---
    
    output_filename = 'magnetic_field_distribution_combined.png'
    plt.savefig(output_filename, dpi=300) # 保存为高分辨率PNG
    
    print(f"\n图表已成功保存为: {output_filename}")
    print("你可以将此 'magnetic_field_distribution_combined.png' 图像文件粘贴到你的电子版报告中。")