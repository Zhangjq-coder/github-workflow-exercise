# GitHub工作流练习项目

这是一个用于演示GitHub工作流的练习项目，包含以下功能：

## 功能

1. **去重列名功能** - 处理重复的列名，为重复项添加数字后缀
2. **数字加法功能** - 简单的数字加法运算

## 项目结构

```
.
├─ app/
│  └─ app.py              # 主应用代码
├─ tests/
│  └─ test_app.py         # 测试代码
├─ Dockerfile             # Docker容器定义
├─ requirements.txt       # Python依赖
└─ .github/
   └─ workflows/
      ├─ python-tests.yml # Python测试工作流
      └─ docker-build.yml # Docker构建工作流
```

## 分支策略

- `main`: 生产环境分支，仅接受来自staging的快进合并
- `staging`: 预生产验证分支，仅接受来自dev的压缩合并
- `dev`: 功能集成分支，仅接受来自feature/*的压缩合并
- `feature/*`: 短期功能分支，每个任务/issue一个分支

## CI/CD流程

1. 创建功能分支并开发功能
2. 提交代码并推送到远程仓库
3. 创建从功能分支到dev的Pull Request
4. CI检查（Python测试和Docker构建）通过后合并到dev
5. 创建从dev到staging的Pull Request
6. 验证通过后合并到staging
7. 创建从staging到main的Pull Request
8. 最终验证通过后合并到main，完成发布

## 本地运行

1. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

2. 运行应用：
   ```
   python app/app.py
   ```

3. 运行测试：
   ```
   pytest tests/ -v
   ```

## Docker运行

1. 构建镜像：
   ```
   docker build -t my-app .
   ```

2. 运行容器：
   ```
   docker run my-app
   ```