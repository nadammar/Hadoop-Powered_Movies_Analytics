# 🎬 Hadoop-Powered Movies Analytics

This project demonstrates how to use **Hadoop MapReduce (Streaming with Python 3)** to analyze large-scale movie datasets (MovieLens) and generate valuable insights. It also integrates **Power BI** for rich, interactive visualizations.

---

## 📂 Dataset

The dataset used in this project is the **[MovieLens 25M Dataset](https://grouplens.org/datasets/movielens/25m)** provided by GroupLens. 


## Technologies Used

* **Hadoop 2.7.2** (HDFS + MapReduce)
* **Python 3** (Hadoop Streaming)
* **Dockerized Hadoop Cluster**
* **Power BI** for data visualization

---


## 🗂 MapReduce Applications

* 1️⃣ **Average Movie Ratings**
* 2️⃣ **Top 20 Movies by Rating (with Titles)**
* 3️⃣ **Highest Rated Movies for Each Genre**
* 4️⃣ **The Average Rating for Each Film per Genre**

👉 More details about these applications, including methodology, code, and results, are explained in the PDF file **“Hadoop\_Movie\_Analytics\_Report.pdf”** (included in the project).

---

## 📊 Power BI Visualizations

The output data from Hadoop MapReduce is visualized in **Power BI** through a set of meaningful charts and reports, helping to better understand trends and insights from the movie dataset.



---

## How to Run

1. **Upload Data to HDFS:**

   ```bash
   hadoop fs -mkdir /user/root/input
   hadoop fs -put movies.csv ratings.csv /user/root/input/
   ```

2. **Run MapReduce Jobs:**

   ```bash
   hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
   -files mapper.py,reducer.py \
   -mapper "python3 mapper.py" \
   -reducer "python3 reducer.py" \
   -input /user/root/input/ratings.csv \
   -output /user/hadoop/output/Hadoop-Powered_Movies_Analytics
   ```

3. **View Results:**

   ```bash
   hadoop fs -cat /user/hadoop/output/Hadoop-Powered_Movies_Analytics/part-00000
   ```

4. **Load Results into Power BI** for visualization.


