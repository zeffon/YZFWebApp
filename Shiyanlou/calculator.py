#!/Users/yuzefeng/PycharmProjects/Shiyanlou/venv/bin/python

import sys
import csv  # 用于写入 csv 文件
import os
from collections import namedtuple
from multiprocessing import Process, Queue, Pool

IncomeTaxQuickLookupItem = namedtuple(
    'IncomeTaxQuickLookupItem',
    ['start_point', 'tax_rate', 'quick_subtractor']
)

INCOME_TAX_START_POINT = 3500

INCOME_TAX_QUICK_LOOKUP_TABLE = [
    IncomeTaxQuickLookupItem(80000, 0.45, 13505),
    IncomeTaxQuickLookupItem(55000, 0.35, 5505),
    IncomeTaxQuickLookupItem(35000, 0.30, 2755),
    IncomeTaxQuickLookupItem(9000, 0.25, 1005),
    IncomeTaxQuickLookupItem(4500, 0.2, 555),
    IncomeTaxQuickLookupItem(1500, 0.1, 105),
    IncomeTaxQuickLookupItem(0, 0.03, 0)
]

queue1, queue2 = Queue()
pool = Pool(processes=3)


# 处理命令行参数类
class Args(object):

    def __init__(self):
        self.args = sys.argv[1:]

    def get_config_path(self):
        index = self.args.index('-c')
        return self.check_file(self.args[index + 1], '.cfg')

    def get_userdata_path(self):
        index = self.args.index('-d')
        return self.check_file(self.args[index + 1], '.csv')

    def get_output_path(self):
        index = self.args.index('-o')
        path = self.args[index+1]
        if not os.path.isfile(path):
          with open(path, 'w') as f:
              csv.writer(f)
        return path

    @staticmethod
    def check_file(path_string, extend):
        if not os.path.isfile(path_string):
            raise FileExistsError
        dir_path, file_path = os.path.split(path_string)
        file_name, file_extend = os.path.splitext(file_path)
        if not file_extend == extend:
            raise ValueError
        return path_string
    """
    补充代码：
    1. 补充参数读取函数，并返回相应的路径.
    2. 当参数格式出错时，抛出异常.
    """


# 配置文件类
class Config(object):

    def __init__(self, path_string):
        self.path_string = path_string
        self.config = self._read_config()
        self.config['rate'] = self._get_rate()
        self.JiShuL = self._get_JiShuL()
        self.JiShuH = self._get_JiShuH()

    # 配置文件读取内部函数
    def _read_config(self):
        config = {}
        with open(self.path_string) as f:
            for line in f.readlines():
                line = line.strip().replace(' ', '')
                key, value = line.split('=')
                config[key] = float(value)
            return config

        """
        补充代码：
        1. 根据参数指定的配置文件路径，读取配置文件信息，并写入到 config 字典中.
        2. 使用 strip() 和 split() 对读取到的配置文件去掉空格以及切分.
        3. 当格式出错时，抛出异常.
        """

    def _get_JiShuL(self):
        return self.config['JiShuL']

    def _get_JiShuH(self):
        return self.config['JiShuH']

    def _get_rate(self):
        rate = self.config['YangLao'] + self.config['YiLiao'] + self.config['ShiYe'] + \
        self.config['GongShang'] + self.config['ShengYu'] + self.config['GongJiJin']
        return rate


# 用户数据类
class UserData(object):

    def __init__(self, path_string):
        self.path_string = path_string
        self.userdata = self._read_users_data()


    # 用户数据读取内部函数
    def _read_users_data(self):
        userdata = []
        with open(self.path_string) as f:
            csv_data = csv.reader(f)
            for row in csv_data:
                employee_id, income = row[:2]
                userdata.append((employee_id, income))
            return userdata
        """
        补充代码：
        1. 根据参数指定的工资文件路径，读取员工 ID 和工资数据.
        2. 可将员工工号和工资数据设置为元组，并存入 userdata 列表中.
        3. 当格式出错时，抛出异常.
        """


# 税后工资计算类
class IncomeTaxCalculator(object):

    def __init__(self, path_string, config, users):
        self.path_string = path_string
        self.JiShuL = config['JiShuL']
        self.JiShuH = config['JiShuH']
        self.rate = config['rate']
        self.users = users
    # 计算每位员工的税后工资函数
    def calc_for_all_userdata(self):

        """
        补充代码：
        1. 计算每位员工的税后工资（扣减个税和社保）.
        2. 注意社保基数的判断.
        3. 将每位员工的税后工资按指定格式返回.
        工号,税前工资,社保金额,个税金额,税后工资
        """


        result = []
        for employee_id, income in self.users.userdata:
            income = float(income)
            social_insurance_money = income
            if income < self.JiShuL:
                social_insurance_money = self.JiShuL
            if income > self.JiShuH:
                social_insurance_money = self.JiShuH

            social_insurance_money = social_insurance_money * self.rate
            real_income = income - social_insurance_money
            taxable_part = real_income - INCOME_TAX_START_POINT
            if taxable_part <= 0:
                result.append((employee_id, '{:.2f}'.format(income), '{:.2f}'.format(social_insurance_money), '0.00',
                              '{:.2f}'.format(real_income)))

            for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
                if taxable_part > float(item.start_point):
                    tax = taxable_part * item.tax_rate - item.quick_subtractor
                    result.append((employee_id, '{:.2f}'.format(income), '{:.2f}'.format(social_insurance_money),
                                  '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)))
        return result

    # 输出 CSV 文件函数
    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open(self.path_string, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)


# 执行
if __name__ == '__main__':
    """
    按实际情况补充代码
    """
    argvs = Args()

    try:
        config_path = argvs.get_config_path()
        user_data_path = argvs.get_userdata_path()
        output_path = argvs.get_output_path()

        cfg = Config(config_path)
        user_data = UserData(user_data_path)
        calculator = IncomeTaxCalculator(output_path, cfg.config, user_data)
        calculator.calc_for_all_userdata()
        calculator.export()

    except Exception as e:
        print(e)
        exit()


