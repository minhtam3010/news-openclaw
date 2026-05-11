# 1. Official AWS image (includes everything needed for Lambda)
FROM public.ecr.aws/lambda/python:3.12

# 2. Lambda uses this specific folder for code
WORKDIR ${LAMBDA_TASK_ROOT}

# 3. Standard install steps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Important: Install mangum if you haven't yet
RUN pip install mangum 

# 4. Copy your code
COPY . .

# 5. Point to the 'handler' variable we created in main.py
CMD [ "main.handler" ]
