FROM python:3.9

RUN apt update && apt install sudo
# Add file to image
ADD requirements_unpinned.txt /tmp/requirements.txt
# Install anything
RUN pip install -r /tmp/requirements.txt
# Set environmental variables
ENV KERAS_BACKEND=torch

# Set user
# Define a build-time variable
ARG USER_ID
ARG GROUP_ID


RUN groupadd -g ${GROUP_ID} my_group
RUN useradd -u ${USER_ID} -g ${GROUP_ID} -o -m my_user
RUN usermod -aG sudo my_user
RUN echo 'my_user ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

USER my_user
