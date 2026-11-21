# Reflection

Name: Nipat Liampisan

Answer each question in 2–3 sentences.

**1. Which antipatterns from the lecture did `train_all.py` show? Point to the lines.**

> Main antipattern in train_all.py is Big-a** script architecture. The entire python file is one long script. Line 15 contained a constant data input, so the antipattern here is set and forget meaning never retrain. Line 19 contains the format of year month and day. This means that if this format changes for different data sources it can cause an error which is the pipeline jungle antipattern.  Lines 28-31 contained dead experimental code paths antipattern, because USE_LOG_PRICE is not used in the train_all.py script at all. 

**2. Suppose there were no test and no evaluation gate. What would have happened when the 2026 batch arrived? Think about both the crash and the missing `sqft` values.**

> Without the test, we would not have known that the format of date time had changed in the 2026 batch. We also would not have known about the missing sqft values, which is a silent error because there would be no crash in the code. Without an evaluation gate, a scheduled run could cause a very inaccurate model to be deployed to production. So it is a good last integration test. 

**3. In the real marketplace, which non-ML parts of the system should trigger this pipeline or feed it data?**

> A scheduled orchestrator like Airflow or github actions could trigger the pipeline. For feeding the data, a data warehouse should be a good fit. This is because the ML algorithm used here is expecting fixed rows and columns. In a real marketplace, a non-ML part that could trigger this pipeline could be the customer satisfaction tracking service. If the customer is too unhappy with the predicted prices, it could also trigger the pipeline. 
