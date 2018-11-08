from mock import mock

def mock_test(mock_method,request_data,url,method,response_data):

    mock_method = mock.Mock(return_value=response_data)

    res = mock_method(method,url,json=request_data)

    return res