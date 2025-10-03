# Airflow Task

This DAG has **3 tasks** that run in order:

1. **Print current date** – using BashOperator.  
2. **Print welcome message** – using PythonOperator.  
3. **Generate a random number** – saves it to `/tmp/random.txt` using PythonOperator.

---

## DAG Flow

task_prnt --> welcome_print --> task_numss


## Screenshots

**DAG Graph**  
<img src="screenshots/graph.png" alt="DAG Graph" width="600"/>

**Task Logs – Print Date**  
<img src="screenshots/date.png" alt="Task Date Logs" width="600"/>

**Task Logs – Welcome Message**  
<img src="screenshots/welcome.png" alt="Welcome Logs" width="600"/>

**Task Logs – Random Number**  
<img src="screenshots/random.png" alt="Random Number Logs" width="600"/>


