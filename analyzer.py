import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Student': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Usman',
                'Zara', 'Hassan', 'Ayesha', 'Bilal', 'Maryam'],
    'Math':    [85, 92, 78, 95, 60, 88, 73, 91, 65, 80],
    'Science': [79, 88, 82, 91, 70, 85, 68, 93, 72, 77],
    'English': [90, 85, 70, 88, 75, 92, 80, 87, 69, 83],
    'Computer':[95, 90, 85, 97, 65, 88, 78, 94, 70, 86]
}

df = pd.DataFrame(data)
df['Total'] = df[['Math','Science','English','Computer']].sum(axis=1)
df['Average'] = df['Total'] / 4

print("=" * 50)
print("      STUDENT MARKS ANALYSIS REPORT")
print("=" * 50)
print(df[['Student','Total','Average']].to_string(index=False))

best = df.loc[df['Average'].idxmax()]
worst = df.loc[df['Average'].idxmin()]
print(f"\n🏆 Top Student: {best['Student']} ({best['Average']:.1f} avg)")
print(f"📉 Needs Help:  {worst['Student']} ({worst['Average']:.1f} avg)")

# Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(df['Student'], df['Average'], color='steelblue')
plt.title('Average Marks per Student')
plt.xlabel('Student')
plt.ylabel('Average Marks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()

# Heatmap
plt.figure(figsize=(10, 6))
heat_data = df.set_index('Student')[['Math','Science','English','Computer']]
sns.heatmap(heat_data, annot=True, fmt='d', cmap='YlOrRd')
plt.title('Student Marks Heatmap')
plt.tight_layout()
plt.savefig('heatmap.png')
plt.show()

# Pie Chart
subject_avg = df[['Math','Science','English','Computer']].mean()
plt.figure(figsize=(7, 7))
plt.pie(subject_avg, labels=subject_avg.index,
        autopct='%1.1f%%', startangle=140,
        colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Subject-wise Average Marks')
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.show()

print("\n✅ All charts saved!")
