
# data = {
#     'time': ['2025-02-20 00:00', '2025-02-20 01:00', '2025-02-20 02:00', '2025-02-20 03:00'],
#     'car': [50, 60, 55, 45],
#     'truck': [10, 12, 15, 8],
#     'bus': [5, 6, 4, 7]
# }

# df = pd.DataFrame(data)
# df['time'] = pd.to_datetime(df['time'])  # 시간을 datetime 형식으로 변환

####################################################################################################################################################
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# df1 = pd.read_csv('YeongjongBr.csv')
# df1['total'] = df1['car_IN'] + df1['truck_IN'] + df1['bus_IN']

# plt.style.use('ggplot')

# # 막대 그래프 그리기
# fig, ax = plt.subplots(figsize=(10, 6))

# bar_width = 1
# bar_positions = np.arange(len(df1))

# ax.bar(bar_positions, df1['car_IN'], bar_width, label='Car_IN', color='royalblue')    # cornflowerblue
# ax.bar(bar_positions, df1['truck_IN'], bar_width, label='Truck_IN', bottom=df1['car_IN'], color='orange')    # yellowgreen mediumseagreen mediumpurple
# ax.bar(bar_positions, df1['bus_IN'], bar_width, label='Bus_IN', bottom=df1['car_IN'] + df1['truck_IN'], color='firebrick')    # lightcoral indianred

# ax.set_xlabel('Time')
# ax.set_ylabel('Count')
# ax.set_title('Vehicle Counts over Time')

# # x축의 시간 값 표시
# ax.set_xticks(bar_positions)
# #ax.set_xticklabels(df['time'].dt.strftime('%H:%M'))

# # 범례 표시
# ax.legend()

# # 그래프 보여주기
# plt.tight_layout()
# plt.show()

####################################################################################################################################################
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# class CctvGraph():
    
#     def plot(df):
#         plt.style.use('ggplot')

#         fig, ax = plt.subplots(figsize=(10, 6))    # 그래프의 전체 크기 설정, 내용을 그릴 수 있는 영역인 Axes 객체 -> 그래프의 다양한 속성 설정, 데이터 시각화 가능

#         bar_width = 1
#         bar_positions = np.arange(len(df))

#         ax.bar(bar_positions, df['car_IN'], bar_width, label='Car_IN', color='royalblue')
#         ax.bar(bar_positions, df['truck_IN'], bar_width, label='Truck_IN', bottom=df['car_IN'], color='orange')
#         ax.bar(bar_positions, df['bus_IN'], bar_width, label='Bus_IN', bottom=df['car_IN'] + df['truck_IN'], color='firebrick')

#         ax.set_xlabel('Time')
#         ax.set_ylabel('Count')
#         ax.set_title('Vehicle Counts over Time')

#         # x축의 시간 값 표시
#         ax.set_xticks(bar_positions)
#         #ax.set_xticklabels(df['time'].dt.strftime('%H:%M'))

#         # 범례 표시
#         ax.legend()

#         # 그래프 보여주기
#         plt.tight_layout()
#         plt.show()

#     # df1 = pd.read_csv('YeongjongBr.csv')
#     # df2 = pd.read_csv('IncheonBr.csv')

#     # plot(df1)
#     # plot(df2)

####################################################################################################################################################
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# df1 = pd.read_csv('YeongjongBr20250224Cum.csv')
# df2 = pd.read_csv('IncheonBr20250224Cum.csv')

# plt.style.use('ggplot')

# # 막대 그래프 그리기
# fig, ax = plt.subplots(figsize=(10, 6))

# bar_width = 0.4  # 바 너비를 약간 좁게 설정하여 두 개의 그래프가 겹치지 않게 함
# bar_positions1 = np.arange(len(df1))  # df1의 bar 위치
# bar_positions2 = bar_positions1 + bar_width  # df2의 bar 위치는 df1의 bar 끝에 바로 이어서 배치

# # df1에 대한 막대 그래프
# ax.bar(bar_positions1, df1['car_IN'], bar_width, label='Car_IN (Yeongjong)', color='gold')    # royalblue
# ax.bar(bar_positions1, df1['truck_IN'], bar_width, label='Truck_IN (Yeongjong)', bottom=df1['car_IN'], color='orange')    # orange
# ax.bar(bar_positions1, df1['bus_IN'], bar_width, label='Bus_IN (Yeongjong)', bottom=df1['car_IN'] + df1['truck_IN'], color='darkorange')    # firebrick

# # df2에 대한 막대 그래프
# ax.bar(bar_positions2, df2['car_IN'], bar_width, label='Car_IN (Incheon)', color='lightgreen')    # plum
# ax.bar(bar_positions2, df2['truck_IN'], bar_width, label='Truck_IN (Incheon)', bottom=df2['car_IN'], color='mediumaquamarine')    # yellowgreen
# ax.bar(bar_positions2, df2['bus_IN'], bar_width, label='Bus_IN (Incheon)', bottom=df2['car_IN'] + df2['truck_IN'], color='lightseagreen')    # salmon

# ax.set_xlabel('Time')
# ax.set_ylabel('Count')
# ax.set_title('Vehicle Counts over Time (Yeongjong vs Incheon)')

# # x축의 시간 값 표시
# #ax.set_xticks(bar_positions1 + bar_width / 2)  # 두 그래프가 겹치지 않도록 가운데로 맞춤
# #ax.set_xticklabels(df['time'].dt.strftime('%H:%M'))

# # 범례 표시
# ax.legend()

# # 그래프 보여주기
# plt.tight_layout()
# plt.show()

####################################################################################################################################################
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


# axs[0, 0].set_xlabel('Time')
# axs[0, 0].set_ylabel('Count')
# axs[0, 0].set_title('Vehicle Counts over Time (Yeongjong vs Incheon)')


# 범례 표시
axs[0, 0].legend()

# 그래프 보여주기
plt.tight_layout()
plt.show()