import streamlit as st
from PIL import Image, ImageDraw

def make_circle_image(image_path):
    img = Image.open(image_path).convert("RGBA")
    size = min(img.size)
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    output = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    output.paste(img, ((size - img.width) // 2, (size - img.height) // 2))
    output.putalpha(mask)
    return output

circle_img = make_circle_image("images/MyPhoto.png")
st.image(circle_img,width=200)

st.markdown("""
# Jestin Jose

*Chicago, IL | 224-258-8087*  
[jestin.joseocto896@gmail.com](mailto:jestin.joseocto896@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/jestin-jose-b00ba2193) | [GitHub](https://github.com/jestinjose90)  

---
            


## Summary  
Highly motivated and detail-oriented data science enthusiast with a strong academic background in Data Science and hands-on experience in data analysis and machine learning. Proficient in Python, R, and data visualization tools. Eager to leverage my knowledge and skills to contribute to the success of a data-driven organization as a Junior Data Scientist. A quick learner with a passion for solving complex problems using data-driven insights.

---

## Education  
- **Master of Science (B.S.) in Data Science**, Eastern University, St Davids, PA 
  - GPA: 3.63  
- **IBM Data Science Professional Certificate** (Coursera.Inc)  
- **Bachelor of Science (B.S.) in Computer Science**, Northeastern Illinois University, Chicago, IL  
  - GPA: 3.83  
  - Graduated with Magna Cum Laude Honors  
 

---

## Relevant Experience  

### Capstone Project: SpaceX Landing Outcome Prediction  
_Mar 2023 – Aug 2023_  
Tools: Python, NumPy, pandas, Scikit-learn, Seaborn, Folium, SQLite  
- Gathered historical data on SpaceX Falcon 9 launches including mission parameters, environmental conditions, and landing outcomes.  
- Performed exploratory data analysis to identify patterns influencing landing success.  
- Conducted data preprocessing including missing value handling and feature engineering.  
- Built classification models using Linear Regression, SVM, Decision Tree Classifier to predict landing outcomes.  
- Used cross-validation and hyperparameter tuning for optimal performance.  
- Visualized model performance using confusion matrix and accuracy metrics.  
- Achieved 88% accuracy on test data.  
- Identified key factors impacting SpaceX landing success and failure.

### House Price Prediction Project  
_May 2023 – July 2023_  
Tools: Python, NumPy, pandas, Scikit-learn, Seaborn  
- Used real estate sales dataset to predict house prices with machine learning.  
- Cleaned data and handled missing values.  
- Explored dataset through visualization for insights on price distribution and feature correlations.  
- Developed and evaluated Simple Linear Regression model using R-squared metric.  
- Improved model performance with regularization techniques.

---

## Technical Skills  
- **Programming Languages:** Python, R, Java  
- **Data Analysis:** Pandas, NumPy, SciPy  
- **Data Cleaning & Preprocessing**  
- **Data Visualization:** Matplotlib, Seaborn, Dash, Tableau  
- **Machine Learning Libraries:** Scikit-learn  
- **Statistical Analysis & Predictive Modeling**  
- **Database Management:** SQL, SQLite  
- **Tools:** Jupyter Notebook, Visual Studio Code, Microsoft Excel, PowerPoint  
- **Big Data:** PySpark (Basic)  
- **Web Scraping:** BeautifulSoup4  
- **Cloud Computing:** AWS (Basic)  

---

## Key Attributes  
- Strong problem-solving and analytical skills  
- Excellent communication and teamwork abilities  
- Enthusiastic learner, actively engaged in online data science communities and courses  
""")