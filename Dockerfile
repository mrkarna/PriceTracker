FROM python:3
COPY . /
RUN pip install selenium
EXPOSE 3333
CMD [ "python", "./main.py"]




# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Install any needed packages specified in package.json
# RUN npm install

# Expose port 3000 for accessing  the app
EXPOSE 3000

# EXPOSE $PORT

# Run app when the container launches
CMD ["python",  "main.py"]