from read_case_auto.interfa_auto import read_case, api_fun, write_result


def execute_fun(file_name, sheet_name):
    cases = read_case(file_name, sheet_name)  # 调用函数，设置变量接收返回值
    for case in cases:
        case_id = case['case_id']  # 获取第几条用例
        url = case['url']  # 字符串格式
        # data = case['data']         # 字符串格式，非字典
        # expect = case['expect']         # 字符串格式，非字典
        data = eval(case['data'])  # 字符串格式，转字典
        expect = eval(case['expect'])  # 字符串格式，转字典
        real_res = api_fun(url_login=url, data_login=data)
        if (expect['code'] == real_res['code']) and (expect['msg'] == real_res['msg']):
            # print("用例通过")
            write_result(file_name, sheet_name, case_id + 1, 8, 'passed')
        else:
            # print("用例不通过")
            write_result(file_name, sheet_name, case_id + 1, 8, 'failed')


# 调用函数
execute_fun('C:\\ztt\\PycharmProjects\\sc18_20201228\\test_data\\test_case_api.xlsx', 'register')
execute_fun('C:\\ztt\\PycharmProjects\\sc18_20201228\\test_data\\test_case_api.xlsx', 'login')
