# 🎬 Hadoop-Powered Movies Analytics

This project demonstrates how to use **Hadoop MapReduce (Streaming with Python 3)** to analyze large-scale movie datasets (MovieLens) and generate valuable insights. It also integrates **Power BI** for rich, interactive visualizations.

---

## 📂 Dataset

The project uses the **MovieLens** dataset containing two files:

1. **movies.csv** – movieId, title, genres
2. **ratings.csv** – userId, movieId, rating, timestamp


## Technologies Used

* **Hadoop 2.7.2** (HDFS + MapReduce)
* **Python 3** (Hadoop Streaming)
* **Dockerized Hadoop Cluster**
* **Power BI** for data visualization

---

## MapReduce Applications

### 1️⃣ **Average Movie Ratings**

* **Objective:** Calculate the average rating for each movie.
* **Mapper:** Emits `(movieId, rating)`
* **Reducer:** Aggregates ratings and outputs average.

### 2️⃣ **Top 20 Movies by Rating**

* **Objective:** Get the top 20 movies with the highest average ratings.
* **Mapper:** Emits `(movieId, rating)`
* **Reducer:** Calculates average rating and sorts top 20.

### 3️⃣ **Top 10 Movies per Genre**

* **Objective:** Identify the top 10 rated movies within each genre.
* **Mapper:** Joins `movies.csv` and `ratings.csv` by movieId and emits `(genre, movieId, rating)`.
* **Reducer:** Groups by genre, computes average ratings, and selects top 10.

### 4️⃣ **Unique Ratings Distribution per Movie**

* **Objective:** List each movie and its unique ratings received.
* **Mapper:** Emits `(movieId, rating)`
* **Reducer:** Aggregates unique ratings and outputs distribution.

---

## 📊 Power BI Dashboard

The output data from Hadoop MapReduce is visualized in **Power BI** to create actionable dashboards:

* Genre-based performance
* Trends by year
* Highest and lowest rated movies

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
   -output /user/hadoop/output/project_name
   ```

3. **View Results:**

   ```bash
   hadoop fs -cat /user/hadoop/output/project_name/part-00000
   ```

4. **Load Results into Power BI** for visualization.


