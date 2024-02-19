#TODO: need to pin down ubuntu version
FROM ubuntu:latest 
WORKDIR /bmi-calc
COPY requirements.txt /bmi-calc
COPY packages.txt /bmi-calc
#TODO: may need to remove update as this will have different updates over time
RUN apt-get update

RUN xargs apt-get -y install <packages.txt

RUN pip install -r requirements.txt
#Test additionkuui
#another test line

