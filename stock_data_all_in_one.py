import adata
import pandas as pd
import argparse
import os
import json
from datetime import datetime

def download_stock_data(stock_code, start_date='2020-01-01', end_date=None, k_type=1, adjust_type=1):
    """
    下载指定股票的历史行情数据
    
    参数:
    stock_code: 股票代码，例如'00001'
    start_date: 开始日期，格式'YYYY-MM-DD'
    end_date: 结束日期，格式'YYYY-MM-DD'，默认为当前日期
    k_type: k线类型：1.日；2.周；3.月；4.季度；5.5分钟；15.15分钟；30.30分钟；60.60分钟
    adjust_type: k线复权类型：0.不复权；1.前复权；2.后复权
    
    返回:
    DataFrame: 包含股票历史行情数据的DataFrame
    """
    if end_date is None:
        end_date = datetime.now().strftime('%Y-%m-%d')
    
    print(f"正在下载 {stock_code} 从 {start_date} 到 {end_date} 的历史行情数据...")
    
    # 获取股票行情数据
    df = adata.stock.market.get_market(
        stock_code=stock_code,
        start_date=start_date,
        end_date=end_date,
        k_type=k_type,
        adjust_type=adjust_type
    )
    
    if df.empty:
        print(f"未找到 {stock_code} 的数据，请检查股票代码是否正确或调整日期范围。")
        return df
    
    print(f"成功下载 {len(df)} 条数据记录。")
    return df

def get_current_market_data(stock_code):
    """
    获取股票的当前行情数据
    
    参数:
    stock_code: 股票代码，例如'000001'
    
    返回:
    DataFrame: 包含股票当前行情数据的DataFrame
    """
    print(f"正在获取 {stock_code} 的当前行情数据...")
    
    # 获取当前行情数据
    df = adata.stock.market.list_market_current(code_list=[stock_code])
    
    if df.empty:
        print(f"未找到 {stock_code} 的当前行情数据。")
        return df
    
    print("成功获取当前行情数据。")
    return df

def get_minute_data(stock_code):
    """
    获取股票的分时行情数据
    
    参数:
    stock_code: 股票代码，例如'00001'
    
    返回:
    DataFrame: 包含股票分时行情数据的DataFrame
    """
    print(f"正在获取 {stock_code} 的今日分时行情数据...")
    
    # 获取分时行情数据
    df = adata.stock.market.get_market_min(stock_code=stock_code)
    
    if df.empty:
        print(f"未找到 {stock_code} 的分时行情数据。")
        return df
    
    print(f"成功获取 {len(df)} 条分时行情数据。")
    return df

def get_five_level_market(stock_code):
    """
    获取股票的五档行情数据
    
    参数:
    stock_code: 股票代码，例如'00001'
    
    返回:
    DataFrame: 包含股票五档行情数据的DataFrame
    """
    print(f"正在获取 {stock_code} 的五档行情数据...")
    
    # 获取五档行情数据
    df = adata.stock.market.get_market_five(stock_code=stock_code)
    
    if df.empty:
        print(f"未找到 {stock_code} 的五档行情数据。")
        return df
    
    print("成功获取五档行情数据。")
    return df

def get_capital_flow(stock_code):
    """
    获取股票的资金流向数据
    
    参数:
    stock_code: 股票代码，例如'00001'
    
    返回:
    DataFrame: 包含股票资金流向数据的DataFrame
    """
    print(f"正在获取 {stock_code} 的资金流向数据...")
    
    # 获取资金流向数据
    df = adata.stock.market.get_capital_flow(stock_code=stock_code)
    
    if df.empty:
        print(f"未找到 {stock_code} 的资金流向数据。")
        return df
    
    print(f"成功获取 {len(df)} 条资金流向数据。")
    return df

def get_dividend_data(stock_code):
    """
    获取股票的分红信息
    
    参数:
    stock_code: 股票代码，例如'00001'
    
    返回:
    DataFrame: 包含股票分红信息的DataFrame
    """
    print(f"正在获取 {stock_code} 的分红信息...")
    
    # 获取分红信息
    df = adata.stock.market.get_dividend(stock_code=stock_code)
    
    if df.empty:
        print(f"未找到 {stock_code} 的分红信息。")
        return df
    
    print(f"成功获取 {len(df)} 条分红信息。")
    return df

def get_stock_info(stock_code):
    """
    获取股票的基本信息
    
    参数:
    stock_code: 股票代码，例如'00001'
    
    返回:
    dict: 包含股票基本信息的字典
    """
    print(f"正在获取 {stock_code} 的基本信息...")
    
    # 获取股本信息
    shares_df = adata.stock.info.get_stock_shares(stock_code=stock_code)
    
    # 获取行业信息
    industry_df = adata.stock.info.get_industry_sw(stock_code=stock_code)
    
    # 获取概念信息
    concept_df = adata.stock.info.get_concept_ths(stock_code=stock_code)
    
    info = {
        'shares': shares_df,
        'industry': industry_df,
        'concept': concept_df
    }
    
    print("成功获取股票基本信息。")
    return info

def save_to_csv(df, file_path, encoding='utf-8-sig'):
    """
    将数据保存为CSV文件
    
    参数:
    df: 包含数据的DataFrame
    file_path: 保存路径
    encoding: 文件编码，默认为'utf-8-sig'
    """
    if df.empty:
        print("没有数据可保存。")
        return
    
    # 确保目录存在
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    df.to_csv(file_path, index=False, encoding=encoding)
    print(f"数据已保存至 {file_path}")

def download_all_data(stock_code, start_date='2020-01-01', end_date=None, k_type=1, adjust_type=1, output_dir=None):
    """
    下载指定股票的所有类型数据
    
    参数:
    stock_code: 股票代码，例如'00001'
    start_date: 开始日期，格式'YYYY-MM-DD'
    end_date: 结束日期，格式'YYYY-MM-DD'，默认为当前日期
    k_type: k线类型：1.日；2.周；3.月；4.季度；5.5分钟；15.15分钟；30.30分钟；60.60分钟
    adjust_type: k线复权类型：0.不复权；1.前复权；2.后复权
    output_dir: 输出目录，默认为当前目录
    
    返回:
    dict: 包含各种数据的字典
    """
    if output_dir is None:
        output_dir = '.'
    
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 初始化结果字典
    result = {}
    
    # 下载历史行情数据
    history_df = download_stock_data(
        stock_code=stock_code,
        start_date=start_date,
        end_date=end_date,
        k_type=k_type,
        adjust_type=adjust_type
    )
    if not history_df.empty:
        file_path = os.path.join(output_dir, f"{stock_code}_history_k{k_type}_a{adjust_type}.csv")
        save_to_csv(history_df, file_path)
        result['history'] = history_df
    
    # 获取当前行情数据
    current_df = get_current_market_data(stock_code)
    if not current_df.empty:
        file_path = os.path.join(output_dir, f"{stock_code}_current.csv")
        save_to_csv(current_df, file_path)
        result['current'] = current_df
    
    # 获取分时行情数据
    minute_df = get_minute_data(stock_code)
    if not minute_df.empty:
        file_path = os.path.join(output_dir, f"{stock_code}_minute.csv")
        save_to_csv(minute_df, file_path)
        result['minute'] = minute_df
    
    # 获取五档行情数据
    five_df = get_five_level_market(stock_code)
    if not five_df.empty:
        file_path = os.path.join(output_dir, f"{stock_code}_five_level.csv")
        save_to_csv(five_df, file_path)
        result['five_level'] = five_df
    
    # 获取资金流向数据
    flow_df = get_capital_flow(stock_code)
    if not flow_df.empty:
        file_path = os.path.join(output_dir, f"{stock_code}_capital_flow.csv")
        save_to_csv(flow_df, file_path)
        result['capital_flow'] = flow_df
    
    # 获取分红信息
    dividend_df = get_dividend_data(stock_code)
    if not dividend_df.empty:
        file_path = os.path.join(output_dir, f"{stock_code}_dividend.csv")
        save_to_csv(dividend_df, file_path)
        result['dividend'] = dividend_df
    
    # 获取股票基本信息
    info = get_stock_info(stock_code)
    for key, df in info.items():
        if not df.empty:
            file_path = os.path.join(output_dir, f"{stock_code}_{key}.csv")
            save_to_csv(df, file_path)
            result[key] = df
    
    return result

def integrate_to_json(stock_code, data_dict=None, output_file=None):
    """
    整合指定股票的各种数据到一个JSON文件中
    
    参数:
    stock_code: 股票代码，例如'000001'
    data_dict: 包含各种数据的字典，如果为None则使用已下载的文件
    output_file: 输出文件路径，默认为'股票代码_integrated_data.json'
    
    返回:
    dict: 包含整合后数据的字典
    """
    if output_file is None:
        output_file = f"{stock_code}_integrated_data.json"
    
    print(f"正在整合 {stock_code} 的数据到JSON文件...")
    
    # 初始化整合数据字典
    integrated_data = {
        "stock_code": stock_code,
        "integration_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "basic_info": {},
        "market_data": {},
        "financial_data": {}
    }
    
    # 如果提供了数据字典，直接使用
    if data_dict:
        # 基本信息
        if 'industry' in data_dict and not data_dict['industry'].empty:
            integrated_data["basic_info"]["industry"] = data_dict['industry'].to_dict(orient='records')
            print(f"已整合行业信息数据")
        
        if 'concept' in data_dict and not data_dict['concept'].empty:
            integrated_data["basic_info"]["concept"] = data_dict['concept'].to_dict(orient='records')
            print(f"已整合概念信息数据")
        
        if 'shares' in data_dict and not data_dict['shares'].empty:
            integrated_data["basic_info"]["shares"] = data_dict['shares'].to_dict(orient='records')
            print(f"已整合股本信息数据")
        
        # 市场数据
        if 'history' in data_dict and not data_dict['history'].empty:
            integrated_data["market_data"]["history"] = data_dict['history'].to_dict(orient='records')
            print(f"已整合历史行情数据，共 {len(data_dict['history'])} 条记录")
        
        if 'current' in data_dict and not data_dict['current'].empty:
            integrated_data["market_data"]["current"] = data_dict['current'].to_dict(orient='records')
            print(f"已整合当前行情数据")
        
        if 'minute' in data_dict and not data_dict['minute'].empty:
            integrated_data["market_data"]["minute"] = data_dict['minute'].to_dict(orient='records')
            print(f"已整合分时行情数据，共 {len(data_dict['minute'])} 条记录")
        
        if 'five_level' in data_dict and not data_dict['five_level'].empty:
            integrated_data["market_data"]["five_level"] = data_dict['five_level'].to_dict(orient='records')
            print(f"已整合五档行情数据")
        
        if 'capital_flow' in data_dict and not data_dict['capital_flow'].empty:
            integrated_data["market_data"]["capital_flow"] = data_dict['capital_flow'].to_dict(orient='records')
            print(f"已整合资金流向数据，共 {len(data_dict['capital_flow'])} 条记录")
        
        # 财务数据
        if 'dividend' in data_dict and not data_dict['dividend'].empty:
            integrated_data["financial_data"]["dividend"] = data_dict['dividend'].to_dict(orient='records')
            print(f"已整合分红信息数据，共 {len(data_dict['dividend'])} 条记录")
    
    # 保存整合后的数据
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(integrated_data, f, ensure_ascii=False, indent=2)
        print(f"整合数据已保存至 {output_file}")
    except Exception as e:
        print(f"保存整合数据失败: {e}")
    
    return integrated_data

def integrate_to_csv(stock_code, data_dict=None, output_file=None):
    """
    整合指定股票的历史行情数据和其他关键信息到一个CSV文件中
    
    参数:
    stock_code: 股票代码，例如'000001'
    data_dict: 包含各种数据的字典，如果为None则使用已下载的文件
    output_file: 输出文件路径，默认为'股票代码_integrated_data.csv'
    
    返回:
    DataFrame: 包含整合后数据的DataFrame
    """
    if output_file is None:
        output_file = f"{stock_code}_integrated_data.csv"
    
    print(f"正在整合 {stock_code} 的数据到CSV文件...")
    
    # 如果没有提供数据字典，返回空DataFrame
    if not data_dict or 'history' not in data_dict or data_dict['history'].empty:
        print(f"未找到 {stock_code} 的历史行情数据")
        return pd.DataFrame()
    
    # 使用历史行情数据作为基础
    history_df = data_dict['history'].copy()
    print(f"已读取历史行情数据，共 {len(history_df)} 条记录")
    
    # 添加行业信息
    if 'industry' in data_dict and not data_dict['industry'].empty:
        industry_info = data_dict['industry'].iloc[0].to_dict()
        for key, value in industry_info.items():
            if key not in ['stock_code']:  # 避免重复的列
                history_df[f'industry_{key}'] = value
        print(f"已添加行业信息")
    
    # 添加分红信息
    if 'dividend' in data_dict and not data_dict['dividend'].empty:
        try:
            dividend_df = data_dict['dividend']
            
            # 将日期列转换为日期类型
            history_df['trade_date'] = pd.to_datetime(history_df['trade_date'])
            dividend_df['ex_dividend_date'] = pd.to_datetime(dividend_df['ex_dividend_date'])
            
            # 创建分红标记列
            history_df['dividend_flag'] = 0
            history_df['dividend_plan'] = ''
            
            # 标记分红日
            for _, row in dividend_df.iterrows():
                ex_date = row['ex_dividend_date']
                plan = row['dividend_plan']
                
                # 找到对应的交易日记录
                mask = history_df['trade_date'] == ex_date
                if mask.any():
                    history_df.loc[mask, 'dividend_flag'] = 1
                    history_df.loc[mask, 'dividend_plan'] = plan
            
            print(f"已添加分红信息")
        except Exception as e:
            print(f"处理分红信息时出错: {e}")
    
    # 保存整合后的数据
    try:
        history_df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"整合数据已保存至 {output_file}")
    except Exception as e:
        print(f"保存整合数据失败: {e}")
    
    return history_df

def parse_arguments():
    """
    解析命令行参数
    
    返回:
    argparse.Namespace: 包含命令行参数的对象
    """
    parser = argparse.ArgumentParser(description='股票数据下载和整合工具')
    
    parser.add_argument('--code', type=str, required=True, help='股票代码，例如：00001')
    parser.add_argument('--start', type=str, default='2020-01-01', help='开始日期，格式：YYYY-MM-DD，默认为2020-01-01')
    parser.add_argument('--end', type=str, default=None, help='结束日期，格式：YYYY-MM-DD，默认为当前日期')
    parser.add_argument('--ktype', type=int, default=1, choices=[1, 2, 3, 4, 5, 15, 30, 60], 
                        help='K线类型：1.日；2.周；3.月；4.季度；5.5分钟；15.15分钟；30.30分钟；60.60分钟，默认为1')
    parser.add_argument('--adjust', type=int, default=1, choices=[0, 1, 2], 
                        help='复权类型：0.不复权；1.前复权；2.后复权，默认为1')
    parser.add_argument('--output', type=str, default=None, 
                        help='输出目录，默认为当前目录')
    parser.add_argument('--format', type=str, choices=['json', 'csv', 'both'], default='both', 
                        help='整合数据的输出格式，可选json、csv或both，默认为both')
    
    return parser.parse_args()

def main():
    """
    主函数
    """
    args = parse_arguments()
    
    # 设置输出目录
    output_dir = args.output or '.'
    
    # 下载所有数据
    data_dict = download_all_data(
        stock_code=args.code,
        start_date=args.start,
        end_date=args.end,
        k_type=args.ktype,
        adjust_type=args.adjust,
        output_dir=output_dir
    )
    
    # 整合数据
    if args.format in ['json', 'both']:
        json_file = os.path.join(output_dir, f"{args.code}_integrated_data.json")
        integrate_to_json(args.code, data_dict, json_file)
    
    if args.format in ['csv', 'both']:
        csv_file = os.path.join(output_dir, f"{args.code}_integrated_data.csv")
        integrate_to_csv(args.code, data_dict, csv_file)
    
    print(f"\n所有操作已完成！数据已保存到 {output_dir} 目录。")

if __name__ == "__main__":
    main() 
