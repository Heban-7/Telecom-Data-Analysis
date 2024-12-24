# 📊 **Telecom User Engagement and Experience Analysis**

### **Project Overview**
This project analyzes telecom user data to understand customer engagement, experience, and satisfaction. Using machine learning and statistical techniques, we identified key performance metrics, clustered users based on their behavior, and provided actionable insights for business strategy.

---

## 🚀 **Objectives**
- Analyze user engagement to identify top-performing customers.
- Evaluate user experience based on network performance metrics.
- Assess customer satisfaction through engagement and experience scores.
- Build predictive models to forecast satisfaction.
- Provide data-driven recommendations for business growth.

---

## 🗂️ **Dataset**
- **Source:** TellCo Telecom Aggregated User Data
- **Rows:** 150001
- **Columns:** 55
- **Key Metrics:**
   - Session Frequency
   - Session Duration
   - Total Traffic
   - TCP Retransmissions
   - Round Trip Time (RTT)
   - Throughput (UL/DL)

---

## ⚙️ **Technologies Used**
- **Python**: Data analysis and machine learning
- **Pandas & NumPy**: Data manipulation
- **Scikit-learn**: Machine learning models
- **Matplotlib & Seaborn**: Data visualization
- **PostgreSQL**: Data storage and querying
- **SQLAlchemy**: Database integration

---

## 📊 **Key Tasks and Insights**

### **Task 1: Data Preprocessing & EDA**
- Cleaned and standardized the dataset.
- Identified trends in user behavior and network performance.
**Insight:** Top 10% of users contribute 60% of total data consumption.

### **Task 2: User Engagement Analysis**
- Clustered users into 3 groups (High, Medium, Low engagement).
**Insight:** Highly engaged users are responsible for significant data usage.

### **Task 3: User Experience Analysis**
- Analyzed network metrics (RTT, TCP Retransmissions, Throughput).
**Insight:** High RTT and retransmissions degrade user experience significantly.

### **Task 4: Satisfaction Analysis**
- Calculated engagement and experience scores using Euclidean distance.
- Built a regression model to predict satisfaction.
**Insight:** Balanced engagement and optimized network performance drive higher satisfaction.

---

## 📈 **Machine Learning Models**
- **K-Means Clustering**: Segmentation of users based on engagement and experience.
- **Linear Regression**: Prediction of user satisfaction scores.

---

## 🛠️ **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telecom-analysis.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up PostgreSQL database and update connection details in the script.

---

## 📊 **Database Integration**
- Results exported to a MySQL database.
- Table: `customer_satisfaction`
- Fields: `MSISDN`, `engagement_score`, `experience_score`, `satisfaction_score`

---

## 📢 **Recommendations**
- Improve user engagement via loyalty programs.
- Optimize network performance in high-traffic areas.
- Implement device upgrade campaigns for better user experience.

---

## 🤝 **Contributing**
Pull requests are welcome!

---

**Developed ❤️ by Liul Jima Teshome**

