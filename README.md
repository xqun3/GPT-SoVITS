# Deploy GPT-SoVits on SageMaker Endpoint

## 部署
1. 启动并打开一台 SageMaker notebook（注意 notebook 的 IAM role 需要有访问 ECR 的权限，如果需要使用 [ssh-helper](https://github.com/aws-samples/sagemaker-ssh-helper) 调试部署代码，也需要添加对应权限）.
2. 打开一个 notebook Terminal 克隆项目到Tnotebook 环境
```
cd SageMaker && git clone https://github.com/xqun3/GPT-SoVITS.git

```
3. 进入到 GPT-SoVITS 目录下
4. 打开 [sagemaker_gpt_sovits_endpoint.ipynb](https://github.com/xqun3/GPT-SoVITS/blob/main/sagemaker_gpt_sovits_endpoint.ipynb) 文件
5. 启动一个 notebook 的 terminal，将示例代码中第一个代码单元格，"chmod +x ./*.sh && ./build_and_push.sh" 拷贝到终端中执行。
6. 打包好镜像后，就可以从第2个代码单元格顺序执行 notebook 中的代码进行部署（如果不需要 SSHhelper 调试代码，在执行过程中可跳过）


## 注意

1. 打镜像的时间大约需要6分钟，上传镜像到 Amazon ECR 大约需要10分钟左右，总共第一步大致需要20分钟左右
2. 由于打镜像过程中，Notebook 会不断刷新，所以最好将 [sagemaker_gpt_sovits_endpoint.ipynb](https://github.com/xqun3/GPT-SoVITS/blob/main/sagemaker_gpt_sovits_endpoint.ipynb) 中"./build_and_push.sh" 命令用 Terminal 执行
