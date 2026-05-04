import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Import data

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "fcc-forum-pageviews.csv")
output_dir = os.path.join(current_dir, "Docs")
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(file_path, index_col="date", parse_dates=True)

# Clean data (remove top 2.5% and bottom 2.5%)
low = df["value"].quantile(0.025)
high = df["value"].quantile(0.975)
df = df[(df["value"] >= low) & (df["value"] <= high)]


def draw_line_plot():
    # Copy data
    df_line = df.copy()

    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_line.index, df_line["value"], color="red", linewidth=1)

    ax.set_title("Daily Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image
    fig.savefig(os.path.join(output_dir, "line_plot.png"))
    return fig


def draw_bar_plot():
    # Copy data
    df_bar = df.copy()

    # Create year and month columns
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()

    # Pivot table for average views per month per year
    df_pivot = df_bar.pivot_table(values="value", index="year", columns="month", aggfunc="mean")

    # Reorder months properly
    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    df_pivot = df_pivot[month_order]

    # Draw bar plot
    fig = df_pivot.plot(kind="bar", figsize=(15, 8)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    # Save image
    fig.savefig(os.path.join(output_dir, "bar_plot.png"))
    return fig


def draw_box_plot():
    # Copy data
    df_box = df.copy()

    # Prepare data for box plots
    df_box.reset_index(inplace=True)
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")
    df_box["month_num"] = df_box["date"].dt.month

    # Sort by month number so Jan starts first
    df_box = df_box.sort_values("month_num")

    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise Box Plot
    sns.boxplot(data=df_box, x="year", y="value", ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise Box Plot
    sns.boxplot(data=df_box, x="month", y="value", ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image
    fig.savefig(os.path.join(output_dir, "box_plot.png"))
    return fig