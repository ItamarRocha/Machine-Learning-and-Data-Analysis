import pandas as pd
import numpy as np
pd.set_option('max_columns',500)
pd.set_option('max_rows',500)

dataset = pd.read_excel("dataset.xlsx",index_col = 0)

dataset.columns = [x.replace("-"," ").replace(" ","_") for x in dataset.columns]

dataset['SARS_Cov_2_exam_result'] = dataset['SARS_Cov_2_exam_result'].replace(['negative','positive'], [0,1])

from sklearn.preprocessing import LabelEncoder


columns_to_be_encoded = []
for column in dataset.columns:
    if dataset[column].dtype == 'O':
        columns_to_be_encoded.append(column)
    else:
        print('not label')
        

labeled = dataset[columns_to_be_encoded]

labeled = labeled.astype("str").apply(LabelEncoder().fit_transform).where(~labeled.isna(), labeled)


dataset = dataset.drop(columns = columns_to_be_encoded)

df = dataset.join(labeled)

corr = dataset.corr()
corre = corr['SARS_Cov_2_exam_result']


age = dataset[['Patient_age_quantile','SARS_Cov_2_exam_result']]

ph = dataset.loc[dataset['pH_(arterial_blood_gas_analysis)'] > 0 ]
ph.columns
ph = ph[['pH_(arterial_blood_gas_analysis)','Patient_age_quantile','SARS_Cov_2_exam_result']]


import matplotlib.pyplot as plt
import numpy as np

plt.rc('axes',labelsize = 30)
plt.rc('xtick',labelsize = 20)
plt.rc('ytick',labelsize = 20)
plt.rc('legend', fontsize= 20)

labels = list(range(20))
posi = []
neg = []
for i in range(20):
    cases = age.loc[age['Patient_age_quantile'] == i]
    cases = cases.iloc[:,1].value_counts()
    neg.append(cases[0])
    posi.append(cases[1])


total = [x + y for x,y in zip(posi,neg)]
infect_percent = [(x/y)*100 for x,y in zip(posi,total)]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize = (20,10))
rects1 = ax.bar(x - width/2, neg, width, label='Negative', color = 'blue')
rects2 = ax.bar(x + width/2, posi, width, label='Positive', color = 'r')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('cases',fontsize = 30)
ax.set_title('Diagnosis by age',fontsize = 50)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax1 = ax.twinx()
ax1.set_ylabel('Infected percentage',fontsize = 30)
ax1.plot(x, infect_percent,marker = 'o', color = 'black',linewidth=7.0,label = f'Porcentagem de infectados por idade')

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',fontsize = 24)


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()


import plotly.graph_objects as go
from IPython.display import display
import numpy as np


total = [x + y for x,y in zip(posi,neg)]

infect_percent = [(x/y)*100 for x,y in zip(posi,total)]

title = 'Main Source for News'
analised = ['Television']
colors = ['rgb(67,67,67)']

mode_size = [12]
line_size = [4]

x_data = np.vstack((labels,)*4)

y_data = np.array([
    infect_percent
])

fig = go.Figure()

for i in range(0, 1):
    fig.add_trace(go.Scatter(x=x_data[i], y=y_data[i], mode='lines',
        name=analised[i],
        line=dict(color=colors[i], width=line_size[i]),
        connectgaps=True,
    ))

    # endpoints
    fig.add_trace(go.Scatter(
        x=[x_data[i][0], x_data[i][-1]],
        y=[y_data[i][0], y_data[i][-1]],
        mode='markers',
        marker=dict(color=colors[i], size=mode_size[i])
    ))

fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
    ),
    autosize=False,
    margin=dict(
        autoexpand=False,
        l=20,
        r=10,
        t=50,
    ),
    showlegend=False,
    plot_bgcolor='white'
)

annotations = []

# Adding labels
# labeling the left_side of the plot
annotations.append(dict(xref='paper', x=0.05, y=y_data[0][0],
                              xanchor='right', yanchor='middle',
                              text='{}%'.format(y_data[0][0]),
                              font=dict(family='Arial',
                                        size=16),
                              showarrow=False))
# labeling the right_side of the plot
annotations.append(dict(xref='paper', x=0.95, y=y_data[0][19],
                              xanchor='left', yanchor='middle',
                              text='{}%'.format(y_data[0][19]),
                              font=dict(family='Arial',
                                        size=16),
                              showarrow=False))
# Title
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Main Source for News',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
# Source
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: PewResearch Center & ' +
                                   'Storytelling with data',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))


fig.update_layout(annotations=annotations)

display(fig)