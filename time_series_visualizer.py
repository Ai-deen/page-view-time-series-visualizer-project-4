import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975)) ]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(12, 4))
    plt.plot(df.index,df['value'])
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([(df.index.year),df.index.month]).mean()

  # Draw bar plot
    ax = df_bar.unstack().plot(kind='bar')
    fig = ax.get_figure()
    ax.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July',
                'August', 'September', 'October', 'November', 'December'])
    ax.set(xlabel='Years', ylabel='Average Page Views')

    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['mon_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('mon_num')

    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize = (14,6))
    ax1 = fig.add_subplot(1,2,1)
    sns.boxplot(x='year',y = 'value' , data = df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    ax2 = fig.add_subplot(1,2,2)
    sns.boxplot(x = 'month',y='value',data = df_box)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
