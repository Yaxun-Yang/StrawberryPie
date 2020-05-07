from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


def send_sms(send_template):
    # client = AcsClient('<accessKeyId>', '<accessSecret>', 'default')
    client = AcsClient('LTAI4FvcnaLHkQVsV8mYWbSu', 'oGUsJq5ourYg4E0jrY4mx0pI4R5tlv', 'default')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    # 以上部分是公用的不变
    request.set_action_name('SendSms')
    # set_action_name 这个是选择你调用的接口的名称，如：SendSms，SendBatchSms等
    request.add_query_param('RegionId', "default")
    # 这个参数也是固定的

    request.add_query_param('PhoneNumbers', "13835649105")  # 发给谁
    request.add_query_param('SignName', "petstore")  # 签名
    request.add_query_param('TemplateCode', "SMS_189623058")  # 模板编号
    request.add_query_param('TemplateParam', send_template)  # 发送验证码内容
    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))


if __name__ == '__main__':
    template = {
        'code': '新二舍101'
    }
    send_sms(template)
