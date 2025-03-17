import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_YJB = []
df_ICB = []
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
date = ['0224', '0225', '0226', '0227', '0228', '0301', '0302']
for i in date:
    df_YJB.append(pd.read_csv(f'YeongjongBr2025{i}Cum.csv', header=0, index_col=0))
    df_ICB.append(pd.read_csv(f'IncheonBr2025{i}Cum.csv', header=0, index_col=0))

# graph
plt.style.use('ggplot')  # style
fig, axs = plt.subplots(7, 2, figsize=(10, 20), sharex=True, sharey=True)
bar_width = 0.4  # 바 너비를 약간 좁게 설정하여 두 개의 그래프가 겹치지 않게 함
for i in range(7):
    bar_positions1 = np.arange(len(df_YJB[i]))  # df1의 bar 위치
    bar_positions2 = bar_positions1 + bar_width  # df2의 bar 위치는 df1의 bar 끝에 바로 이어서 배치
    # YeongjongBr IN
    axs[i, 0].bar(bar_positions1, df_YJB[i]['car_IN'], bar_width, label='Car_IN (Yeongjong)', color='gold')
    axs[i, 0].bar(bar_positions1, df_YJB[i]['truck_IN'], bar_width, label='Truck_IN (Yeongjong)', bottom=df_YJB[i]['car_IN'], color='orange')
    axs[i, 0].bar(bar_positions1, df_YJB[i]['bus_IN'], bar_width, label='Bus_IN (Yeongjong)', bottom=df_YJB[i]['car_IN'] + df_YJB[i]['truck_IN'], color='firebrick')
    # YeongjongBr OUT
    axs[i, 0].bar(bar_positions2, df_YJB[i]['car_OUT'], bar_width, label='Car_OUT (Yeongjong)', color='lightgreen')
    axs[i, 0].bar(bar_positions2, df_YJB[i]['truck_OUT'], bar_width, label='Truck_OUT (Yeongjong)', bottom=df_YJB[i]['car_OUT'], color='mediumaquamarine')
    axs[i, 0].bar(bar_positions2, df_YJB[i]['bus_OUT'], bar_width, label='Bus_OUT (Yeongjong)', bottom=df_YJB[i]['car_OUT'] + df_YJB[i]['truck_OUT'], color='royalblue')
    # IncheonBr IN
    axs[i, 1].bar(bar_positions1, df_ICB[i]['car_IN'], bar_width, label='Car_IN (Incheon)', color='gold')
    axs[i, 1].bar(bar_positions1, df_ICB[i]['truck_IN'], bar_width, label='Truck_IN (Incheon)', bottom=df_ICB[i]['car_IN'], color='orange')
    axs[i, 1].bar(bar_positions1, df_ICB[i]['bus_IN'], bar_width, label='Bus_IN (Incheon)', bottom=df_ICB[i]['car_IN'] + df_ICB[i]['truck_IN'], color='indianred')
    # IncheonBr OUT
    axs[i, 1].bar(bar_positions2, df_ICB[i]['car_OUT'], bar_width, label='Car_OUT (Incheon)', color='lightgreen')
    axs[i, 1].bar(bar_positions2, df_ICB[i]['truck_OUT'], bar_width, label='Truck_OUT (Incheon)', bottom=df_ICB[i]['car_OUT'], color='mediumaquamarine')
    axs[i, 1].bar(bar_positions2, df_ICB[i]['bus_OUT'], bar_width, label='Bus_OUT (Incheon)', bottom=df_ICB[i]['car_OUT'] + df_ICB[i]['truck_OUT'], color='royalblue') 
    # Title
    axs[i, 0].set_title(f"YeongjongBr {date[i]} ({week[i]})")
    axs[i, 1].set_title(f"IncheonBr {date[i]} ({week[i]})")
    axs[6, 0].set_xlabel('Time')
    axs[6, 1].set_xlabel('Time')
    axs[i, 0].set_ylabel('Count')
    # X-Axis
    df_YJB[i].index = pd.to_datetime(df_YJB[i].index, format='%H:%M:%S')  # 인덱스를 datetime 형식으로 변환
    df_ICB[i].index = pd.to_datetime(df_ICB[i].index, format='%H:%M:%S')  # 인덱스를 datetime 형식으로 변환
    step = 36
    axs[i, 0].set_xticks(bar_positions1[::step])
    axs[i, 0].set_xticklabels(df_YJB[i].index.strftime('%H')[::step])
    axs[i, 1].set_xticks(bar_positions2[::step])
    axs[i, 1].set_xticklabels(df_ICB[i].index.strftime('%H')[::step])

# 범례 표시
axs[0, 0].legend()

# 그래프 보여주기
plt.tight_layout()
plt.show()
