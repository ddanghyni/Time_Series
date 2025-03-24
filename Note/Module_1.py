#%% Random Variation Time Series
import numpy as np
import plotly.graph_objects as go

def plot_random_variation_time_series(alpha=0.0, length=100, noise_std=1.0, seed=None):

    if seed is not None:
        np.random.seed(seed)

    # 시계열 생성: e_t ~ N(0, noise_std^2)
    noise = np.random.normal(loc=0.0, scale=noise_std, size=length)
    y = alpha + noise  # Y_t = alpha + e_t

    # Plotly Figure 생성
    fig = go.Figure()

    # (1) 시계열 데이터
    fig.add_trace(
        go.Scatter(
            x=list(range(length)),
            y=y,
            mode='markers+lines',
            name='Time Series'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[0, length - 1],
            y=[alpha, alpha],
            mode='lines',
            line=dict(dash='dash', color='red'),
            name=f'Mean = {alpha}'
        )
    )

    fig.update_layout(
        title='Random Variation Time Series',
        xaxis_title='Time (t)',
        yaxis_title='Y_t',
        template='plotly_white'
    )

    fig.show()

#plot_random_variation_time_series(alpha=0, length=50, noise_std=0.8, seed=42)


#%%
def plot_seasonal_time_series(alpha=0.0, beta1=1.0, beta=1.0, f=12, length=50, noise_std=1.0, seed=None):

    if seed is not None:
        np.random.seed(seed)

    # 시계열의 시간 축 (예: 0, 1, 2, ..., length-1)
    t = np.arange(length)

    # 주기 성분(사인 + 코사인)
    seasonal_component = (
            beta1 * np.sin((2.0 * np.pi * t) / f)
            + beta * np.cos((2.0 * np.pi * t) / f)
    )

    # 정규분포 잡음 생성
    noise = np.random.normal(loc=0.0, scale=noise_std, size=length)

    # 최종 시계열: y_t = alpha + (seasonal part) + e_t
    y = alpha + seasonal_component + noise

    fig = go.Figure()

    # (1) 실제 시계열 (points + line)
    fig.add_trace(
        go.Scatter(
            x=t,
            y=y,
            mode='markers+lines',
            name='Seasonal Time Series',
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[0, length - 1],
            y=[alpha, alpha],
            mode='lines',
            line=dict(dash='dash', color='red'),
            name=f'Mean = {alpha}'
        )
    )

    # 레이아웃 설정
    fig.update_layout(
        title='Seasonal Variation Time Series',
        xaxis_title='Time (t)',
        yaxis_title='y_t',
        template='plotly_white'
    )

    fig.show()

#%%
def plot_trend_time_series(alpha=0.0, beta=1.0, length=100, noise_std=1.0, seed=None):
    # 난수 고정(옵션)
    if seed is not None:
        np.random.seed(seed)

    # 시간축 (t = 0, 1, 2, ..., length-1)
    t = np.arange(length)

    # 잡음 생성 e_t ~ N(0, noise_std^2)
    noise = np.random.normal(loc=0.0, scale=noise_std, size=length)

    # 추세 반영된 시계열: y_t = alpha + beta * t + e_t
    y = alpha + beta * t + noise

    # Plotly Figure 생성
    fig = go.Figure()

    # 시계열 데이터
    fig.add_trace(
        go.Scatter(
            x=t,
            y=y,
            mode='markers+lines',
            name='Trend Time Series'
        )
    )

    # 레이아웃 설정
    fig.update_layout(
        title='Trend Variation Time Series',
        xaxis_title='Time (t)',
        yaxis_title='y_t',
        template='plotly_white'
    )

    fig.show()

#plot_trend_time_series(alpha=5, beta=0.5, length=100, noise_std=2.0, seed=42)
