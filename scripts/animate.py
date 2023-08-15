import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

file = 'data/expandeds.csv'

df = pd.read_csv(file)
df.drop(columns=df.columns[0], axis=1,  inplace=True)
plt.style.use('dark_background')
colors = {
    'Toyota': 'white',
    'Ford': 'blue',
    'Chevrolet': 'yellow',
    'Honda': 'turquoise',
    'Nissan': 'orange',
    'Volkswagen': 'green',
    'Hyundai': 'lime',
    'Dodge': 'gray',
    'Renault': 'brown',
    'Suzuki': 'violet',
    'Peugeot': 'pink',
    'Mazda': 'red',
    'Mercedes-Benz': 'silver',
    'Citroen': 'thistle',
    'Kia': 'cyan',
    'BMW': 'gold'
}

car_logos = {
    'Toyota': 'logos/Toyota.png',
    'Ford': 'logos/Ford.png',
    'Chevrolet': 'logos/Chevrolet.png',
    'Honda': 'logos/Honda.png',
    'Nissan': 'logos/Nissan.png',
    'Volkswagen': 'logos/Volkswagen.png',
    'Hyundai': 'logos/Hyundai.png',
    'Dodge': 'logos/Dodge.png',
    'Renault': 'logos/Renault.png',
    'Suzuki': 'logos/Suzuki.png',
    'Peugeot': 'logos/Peugeot.png',
    'Mazda': 'logos/Mazda.png',
    'Mercedes-Benz': 'logos/Mercedes-Benz.png',
    'Citroen': 'logos/Citroen.png',
    'Kia': 'logos/Kia.png',
    'BMW': 'logos/BMW.png'
}

fig, ax = plt.subplots(figsize=(10, 13))
plt.style.use('dark_background')



def animate(i):
    ax.clear()
    df_new = df.iloc[i]

    car_sales = pd.Series(df_new)

    # Sorting in descending order
    sorted_car_sales = car_sales.sort_values(ascending=False)

    sorted_car_sales = sorted_car_sales[0:10]
    sorted_car_sales = sorted_car_sales.iloc[::-1]
    val = sorted_car_sales.index
    sales = sorted_car_sales.values
    print(val)

    ax.barh(sorted_car_sales.index, sorted_car_sales.values, color=[colors[car] for car in sorted_car_sales.index], height=0.8)
    for index, value in enumerate(sorted_car_sales.values):
        ax.text(value, index, f'{value:,.0f}'.replace(',', ' '), va='center', fontsize=23)
    ax.set_xlim(0, 130000000)
    ax.tick_params(axis='y', labelsize=23)
    ax.set_xlabel("Sales")
    plt.suptitle('Top 10 Best Selling Car Companies by Year:', size=26)
    ax.set_title(f"{df['year'][i]}", size=25, color = '#E6825D')
    for edge in ['top', 'right', 'bottom', 'left']:
        ax.spines[edge].set_visible(False)
    #ax.tick_params(left = False)
    ax.get_xaxis().set_visible(False)

plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.subplots_adjust(left=0.27, right=0.81)

animation = FuncAnimation(fig,animate, frames=range(0, len(df)), interval = 55)
animation.save('car.gif', dpi=100, writer=PillowWriter(fps=100)) # Script for saving

plt.show()