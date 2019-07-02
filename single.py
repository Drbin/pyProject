import requests
import json
def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    return data_model
if __name__ == '__main__':
    main()


