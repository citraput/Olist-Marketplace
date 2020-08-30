# Final-Project

Dataset Source: https://drive.google.com/file/d/10aY2mJR9EZU65WJxcl0Ob7jGm3V0f05x/view?usp=sharing

Final Project Title: Customer Segmentation and Customer Behavior Purchase Prediction At Olist Marketplace

<h2>Problems:</h2>
1. Customer's data regarding gender, location, etc might not be correct 100%, therefore, segmenting customers based on persona is not really accurate<br>
2. Olist has abundant customers who don't do repurchase in 2018<br>
3. To maintain sustainable growth of company, it's better to retain the existing customer than to get a new customer<br>
4. It's harder to maintain customers than to get the new customers<br> 

<h2>Goals:</h2>
1. Retarget/segmenting customers based on the customer's behavior using RFM method (Recency, Monetary and Frequency)<br> 
2. Making Retain Model by analyzing the customer behavior in one year and make a prediction of customer next purchase in the next 1 year. Classify the customers is conducted by dividing customer into chustomers who will do the next purchase < 4 months, > 4 month and > 8 months<br>
3. Conducting Retention Rate and Churn Rate Analysis to be used as a metrics by Marketing Team<br> 

<h2>Conclusion:</h2>
1. Olist is presumed as a company with the low retention rate, Olist has to find selling point to make the customers loyal to the brand<br>
2. RFM Segmentation could be used to Increased customer retention as well as revenue by classifying customer and treat them accordingly<br>
3. This model is conducted to predict the customers next purchase under 4 months (Class 2) with predictor that consist of 'diff_day_1', 'RepurchaseDays', 'Recency', 'Frequency', 'Monetary', 'R_Score', 'F_Score', 'M_Score', 'RFM_Total_Score', 'Segment_High-Tier', 'Segment_Low-Tier', 'Segment_Mid-Tier'<br>
4. The company will not give the discount/promo to Class 2 Customers because we predicted that they will repurchase in before 4 months<br>
5. We determined the Precision Class 2 as a focus in this model because the company is better to reduce False Prediction Class 2 as an actual Class 0 or 1<br>
6. Failed prediction of Class 2 will result the actual Class 0 or 1 missing the promotion/discounts that leads to the potential of churn<br>


