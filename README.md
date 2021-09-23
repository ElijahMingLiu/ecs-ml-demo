# 介绍

这个repo以在Boston数据集训练LightGBM为例，展示了利用ECS进行无服务器的机器学习模型训练，并自动保存至S3。

```
├── dataset # 用于训练的数据，会被打包并上传至s3
│   ├── train.csv
├── docker_code # 存放docker镜像的代码
│   └── cmd.sh # cmd.sh接收3个参数，分别是代码s3文件,数据集s3文件,模型存储路径
├── Dockerfile # docker镜像的构建文件
├── ecs_maker.ipynb # 构建镜像并推送至ECR，构建ECS及Lambda函数
├── lambda_train # 存放Lambda函数的代码
│   ├── function.zip
│   └── lambda_function.py
├── train_code # 存放训练代码，会被上传至s3
│   ├── run.sh # 启动训练任务
│   ├── train.py # 训练脚本
└── utils.py # 辅助代码，用于构建镜像并推送至ECR及打包并推送代码至s3等
```