# STEP 1: Install base iamge. Optimized for Python.
FROM python:3.7-slim-buster

# Step 2: Add requirements.txt file 
COPY requirements.txt /requirements.txt

# Step 3:  Install required pyhton dependencies from requirements file
RUN pip install -r requirements.txt

# Step 4: Copy source code in the current directory to the container
COPY . /app

# Step 5: Set working directory to previously added app directory
WORKDIR /app

# Step 6: Expose the port Flask is running on
ENTRYPOINT [ "python"]

# Step 9: Run Flask


CMD ["./app.py" ]