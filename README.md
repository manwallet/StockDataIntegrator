# StockDataIntegrator

一个强大的A股数据整合工具，基于[AData](https://adata.30006124.xyz)库开发，专注于为量化交易和AI分析提供全面、结构化的股票数据解决方案。

## 项目简介

StockDataIntegrator 是一个一站式股票数据处理工具，它能够：

- 自动获取并整合多维度股票数据（行情、财务、资金流向等）
- 支持灵活的数据格式（JSON/CSV）和时间周期配置
- 专为量化分析和机器学习应用场景优化
- 提供标准化的数据结构，便于后续分析处理

## 功能特点

- 支持下载多种类型的股票数据：历史行情、当前行情、分时行情、五档行情、资金流向、分红信息、基本信息等
- 提供两种整合格式：JSON和CSV
- 支持自定义时间范围、K线类型、复权类型等参数
- 一体化流程：一次性完成下载和整合

## 安装依赖

首先需要安装AData库：

```bash
pip install adata
```

如果安装速度较慢，可以使用国内镜像源：

```bash
pip install adata -i http://mirrors.aliyun.com/pypi/simple/
```

## 使用方法

### 一体化工具（推荐）

一次性完成下载和整合：

```bash
python stock_data_all_in_one.py --code 股票代码 --start 开始日期
```

例如，下载某股票从2024年1月1日到现在的数据：

```bash
python stock_data_all_in_one.py --code 000001 --start 2024-01-01
```

### 指定时间范围

```bash
# 指定开始日期
python stock_data_all_in_one.py --code 000001 --start 2023-01-01

# 指定开始和结束日期
python stock_data_all_in_one.py --code 000001 --start 2023-01-01 --end 2023-12-31
```

### 指定K线类型和复权类型

```bash
# 指定K线类型（1:日K，2:周K，3:月K，4:季度K，5:5分钟，15:15分钟，30:30分钟，60:60分钟）
python stock_data_all_in_one.py --code 000001 --ktype 2

# 指定复权类型（0:不复权，1:前复权，2:后复权）
python stock_data_all_in_one.py --code 000001 --adjust 0
```

### 指定输出目录和格式

```bash
# 指定输出目录
python stock_data_all_in_one.py --code 000001 --output data_folder

# 指定输出格式（json, csv, both）
python stock_data_all_in_one.py --code 000001 --format json
python stock_data_all_in_one.py --code 000001 --format csv
```

## 输出文件说明

该工具会生成以下文件：

1. **原始数据文件**：
   - `股票代码_history_k类型_a复权类型.csv`：历史行情数据
   - `股票代码_current.csv`：当前行情数据
   - `股票代码_minute.csv`：分时行情数据
   - `股票代码_five_level.csv`：五档行情数据
   - `股票代码_capital_flow.csv`：资金流向数据
   - `股票代码_dividend.csv`：分红信息
   - `股票代码_shares.csv`：股本信息
   - `股票代码_industry.csv`：行业信息
   - `股票代码_concept.csv`：概念信息

2. **整合数据文件**：
   - `股票代码_integrated_data.json`：JSON格式的整合数据
   - `股票代码_integrated_data.csv`：CSV格式的整合数据

### JSON格式

JSON格式的整合数据包含以下主要部分：

1. **基本信息**：
   - 行业信息
   - 概念信息
   - 股本信息

2. **市场数据**：
   - 历史行情数据
   - 当前行情数据
   - 分时行情数据
   - 五档行情数据
   - 资金流向数据

3. **财务数据**：
   - 分红信息

### CSV格式

CSV格式的整合数据以历史行情数据为基础，添加了以下信息：

1. **行业信息**：
   - industry_sw_code：申万行业代码
   - industry_industry_name：行业名称
   - industry_industry_type：行业类型
   - industry_source：数据来源

2. **分红信息**：
   - dividend_flag：是否为分红日（1表示是，0表示否）
   - dividend_plan：分红方案

## 完整参数说明

```
usage: stock_data_all_in_one.py [-h] --code CODE [--start START] [--end END]
                               [--ktype {1,2,3,4,5,15,30,60}]
                               [--adjust {0,1,2}] [--output OUTPUT]
                               [--format {json,csv,both}]

股票数据下载和整合工具

optional arguments:
  -h, --help            显示帮助信息并退出
  --code CODE           股票代码，例如：000001
  --start START         开始日期，格式：YYYY-MM-DD，默认为2020-01-01
  --end END             结束日期，格式：YYYY-MM-DD，默认为当前日期
  --ktype {1,2,3,4,5,15,30,60}
                        K线类型：1.日；2.周；3.月；4.季度；5.5分钟；15.15分钟；30.30分钟；60.60分钟，默认为1
  --adjust {0,1,2}      复权类型：0.不复权；1.前复权；2.后复权，默认为1
  --output OUTPUT       输出目录，默认为当前目录
  --format {json,csv,both}
                        整合数据的输出格式，可选json、csv或both，默认为both
```

## 为AI分析准备数据

对于AI分析，建议使用CSV格式的整合数据，因为它更容易被大多数机器学习库处理。CSV格式的整合数据包含了历史行情数据、行业信息和分红信息，这些通常是AI分析股票时最需要的数据。

如果需要更全面的数据，可以使用JSON格式的整合数据，它包含了所有下载的数据。

## 注意事项

1. 分时行情数据只能获取当天的数据。
2. 历史数据默认从2020年1月1日开始，可以通过`--start`参数指定更早的日期。
3. 数据来源于公开接口，可能存在限制，如遇到请求失败，可以尝试设置代理或稍后再试。
4. 整合后的CSV文件主要适合时间序列分析，而JSON文件包含更全面的信息。

## 数据来源

数据来源于AData库，该库整合了多个数据源：

- 同花顺
- 百度股市通
- 东方财富
- 腾讯理财
- 新浪财经

## 许可证

本项目采用MIT许可证。

## 致谢

感谢[AData](https://adata.30006124.xyz)项目提供的数据接口。

