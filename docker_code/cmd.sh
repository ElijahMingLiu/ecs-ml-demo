#!/bin/sh

# for saving model
mkdir model

# download code to ./
aws s3 cp $1 .

# download code to ./data
mkdir data
aws s3 cp $2 ./data/

#unzip code
tar xvf sourcedir.tar.gz

# saving model to ./model

# starting training
chmod +x run.sh
./run.sh

# upload model to specified s3
aws s3 cp model/ $3 --recursive

echo Model uploaded to $3