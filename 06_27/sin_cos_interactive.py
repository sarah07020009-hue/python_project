import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 設定中文字型（依作業系統自動選用）
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Heiti TC', 'Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

# 建立圖表與軸
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.28)  # 預留空間給滑桿

# X 軸範圍：0 到 4π
x = np.linspace(0, 4 * np.pi, 1000)

# 初始參數
A_init, omega_init, phi_init = 1.0, 1.0, 0.0

# 繪製初始曲線
sin_line, = ax.plot(x, A_init * np.sin(omega_init * x + phi_init),
                    label='sin 波形', color='#1f77b4', linewidth=2)
cos_line, = ax.plot(x, A_init * np.cos(omega_init * x + phi_init),
                    label='cos 波形', color='#ff7f0e', linewidth=2, linestyle='--')

# 圖表設定
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-5.5, 5.5)
ax.set_title('正弦（sin）與餘弦（cos）波形互動繪圖', fontsize=14)
ax.set_xlabel('x (弧度)', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')
ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi])
ax.set_xticklabels(['0', 'π', '2π', '3π', '4π'])

# ========== 建立三個滑桿 ==========

# 滑桿顏色設定
slider_color = 'lightgoldenrodyellow'

# 振幅滑桿
ax_amp = plt.axes([0.15, 0.17, 0.70, 0.03], facecolor=slider_color)
slider_amp = Slider(ax_amp, '振幅 (A)', 0.1, 5.0, valinit=A_init, valstep=0.05)

# 頻率滑桿
ax_freq = plt.axes([0.15, 0.11, 0.70, 0.03], facecolor=slider_color)
slider_freq = Slider(ax_freq, '頻率 (ω)', 0.1, 10.0, valinit=omega_init, valstep=0.05)

# 相位偏移滑桿
ax_phase = plt.axes([0.15, 0.05, 0.70, 0.03], facecolor=slider_color)
slider_phase = Slider(ax_phase, '相位偏移 (φ)', 0, 2 * np.pi, valinit=phi_init, valstep=0.01)


# 更新波形的函數
def update(val):
    """當滑桿值變動時重新計算並更新波形"""
    A = slider_amp.val
    omega = slider_freq.val
    phi = slider_phase.val

    sin_line.set_ydata(A * np.sin(omega * x + phi))
    cos_line.set_ydata(A * np.cos(omega * x + phi))

    # 根據振幅動態調整 Y 軸範圍
    ax.set_ylim(-A * 1.15, A * 1.15)
    fig.canvas.draw_idle()


# 將更新函數綁定到三個滑桿
slider_amp.on_changed(update)
slider_freq.on_changed(update)
slider_phase.on_changed(update)

# 顯示圖表
plt.show()
