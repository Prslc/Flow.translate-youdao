<div align="center">

# 有道翻译插件 (FlowLauncher)

<img src="../Images/app.png" alt="应用图标" width="150" height="150"><br>

中文 | [English](../README.md)

</div>

## 概览

该插件允许你在 Flow Launcher 内快速进行文本翻译。支持自动语言检测、可配置的源语言和目标语言，并可快速将翻译结果复制到剪贴板。

## 注意事项

- 当前插件 **仅支持有道开放 API**。  
- 非 API 翻译模式（网页或离线）**尚未实现**，未来可能添加。  
- 如果你是首次使用有道开放 API，请注意其 **非免费**，注册和使用可能需要付费计划，请在使用前查看有道官方定价。  
- 申请 API: **[有道开放平台](https://ai.youdao.com)**

## 功能

- 实时翻译（使用有道 API）  
- 自动语言检测  
- 一键复制翻译结果到剪贴板  

## 安装

1. **下载插件 ZIP**  
   访问 GitHub 仓库 [Releases](https://github.com/Prslc/Flow.translate-youdao/releases) 下载最新 ZIP 文件。

2. **安装到 Flow Launcher**  
   - 打开 Flow Launcher **设置**  
   - 点击 **插件商店**  
   - 选择 **从本地安装插件**  
   - 选择下载的 ZIP 文件  
   - **重启 Flow Launcher**

3. **配置有道 API 凭证**  
   在插件设置中填写 `app_token` 和 `app_secret`。

4. **选择源语言和目标语言**  
   使用下拉菜单选择你需要的源语言和目标语言。

## 使用方法

- 打开 Flow Launcher 输入框，输入插件关键词 **`tr`**，然后输入需要翻译的文本。  
- 按 **Enter** 将翻译结果复制到剪贴板。

## 发展计划

- [ ] 非 API 翻译模式（网页或离线）  
- [ ] 多语言本地化支持  
- [ ] 节省模式（降低 API 消耗）  

## 致谢

- **[FlowLauncher](https://github.com/Flow-Launcher/Flow.Launcher)** – 插件运行的平台，提供核心功能与集成。  
- **[pyFlowLauncher](https://github.com/Garulf/pyFlowLauncher)** – Flow Launcher Python 插件框架，本插件使用其作为主要接口。  
- **[DirectTranslate](https://github.com/Drimix20/Flow.Launcher.Plugin.DirectTranslate)** – 提供插件架构、交互设计和翻译工作流程的灵感。
