# Dockerfile with issues

FROM python:3.9

# Bad practice: Running as root
USER root

# Security issue: Exposing sensitive ports
EXPOSE 22
EXPOSE 3306

WORKDIR /app

# Inefficient: Not using layer caching properly
RUN pip install flask
RUN pip install requests
RUN pip install pandas

COPY . .

# Security: Hardcoded secret
ENV SECRET_KEY=super_secret_123

# Missing health check
# No resource linit

CMD ["python", "app.py"]
