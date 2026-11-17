import matplotlib.pyplot as plt

# ---------------- DATA ----------------
# Monthly Sales Data - 2026
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

sales = [52000, 68000, 75000, 60000, 95000, 110000,
         98000, 82000, 78000, 105000, 118000, 125000]

profit = [11000, 15000, 19000, 13000, 24000, 32000,
          26000, 21000, 20000, 29000, 34000, 38000]

# Category Sales Data
categories = ['Electronics', 'Clothing', 'Grocery', 'Furniture']
category_sales = [450000, 320000, 280000, 180000]

# Customer Age Data - 40 Customers
customers_age = [22, 25, 28, 30, 31, 32, 33, 34, 35, 38,
                 40, 27, 29, 31, 32, 36, 24, 26, 30, 33,
                 28, 31, 35, 37, 29, 30, 32, 34, 25, 28,
                 31, 33, 36, 29, 30, 31, 32, 34, 28, 29]

# Top 5 Months Data
top_months = ['May', 'Oct', 'Jun', 'Nov', 'Dec']
top_sales = [95000, 105000, 110000, 118000, 125000]

# ---------------- DASHBOARD ----------------
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('E-Commerce Sales Analysis Dashboard - 2026',
             fontsize=20, fontweight='bold')

# 1. Line Plot - Monthly Sales Trend
axes[0, 0].plot(months, sales, marker='o', color='blue', linewidth=2)
axes[0, 0].set_title('Monthly Sales Trend')
axes[0, 0].set_ylabel('Sales (Rs)')
axes[0, 0].grid(alpha=0.3)

# 2. Bar Plot - Sales by Category
axes[0, 1].bar(categories, category_sales,
               color=['red', 'green', 'skyblue', 'orange'])
axes[0, 1].set_title('Sales by Category')
axes[0, 1].tick_params(axis='x', rotation=20)

# 3. Pie Chart - Category Share
axes[0, 2].pie(category_sales, labels=categories,
               autopct='%1.1f%%', startangle=90)
axes[0, 2].set_title('Category Share %')

# 4. Scatter Plot - Sales vs Profit
axes[1, 0].scatter(sales, profit, color='green', alpha=0.7, s=100)
axes[1, 0].set_title('Sales vs Profit Relation')
axes[1, 0].set_xlabel('Sales')
axes[1, 0].set_ylabel('Profit')

# 5. Histogram - Customer Age Distribution
axes[1, 1].hist(customers_age, bins=10, color='purple',
                alpha=0.7, edgecolor='white')
axes[1, 1].set_title('Customer Age Distribution')
axes[1, 1].set_xlabel('Age')

# 6. Horizontal Bar - Top 5 Months
axes[1, 2].barh(top_months, top_sales, color='orange')
axes[1, 2].set_title('Top 5 Sales Months')

plt.tight_layout()
plt.savefig('dashboard.png', dpi=300)
plt.show()
print("Dashboard created successfully!")