FROM python
COPY . /home
RUN pip install --no-cache-dir pandas Faker && \
    mkdir /home/report /home/data && \
    chmod +x /home/hello.py
VOLUME /home/report /home/data
WORKDIR /home
CMD python /home/hello.py