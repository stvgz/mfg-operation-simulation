# Setup

## install git


## Pull remote code Find an empty folder

Run the following command in the terminal
> git clone https://github.com/stvgz/mfg-operation-simulation.git

## 10min guide for git

## install requirements
Run the following command in the terminal
> pip install -r requirements.txt


## install extensions: python, Excel Viewer, Draw.io Intergration
## Github copilot 


# Setup a temp database

docker run --name some-postgres -e POSTGRES_PASSWORD=cZ6eMqv&AZ4P^uB2 -d postgres


docker run -it --name postgres --restart always -e POSTGRES_PASSWORD='cZ6eMqv&AZ4P^uB2' -e ALLOW_IP_RANGE=0.0.0.0/0 -v /home/postgres/data:/var/lib/postgresql -p 5444:5444 -d postgres


psql -U postgres -W

aabbccdd