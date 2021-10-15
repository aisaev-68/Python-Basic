import requests
import re

if __name__ == '__main__':
    print('Результат:')
    all_data_columb = requests.get('http://www.columbia.edu/~fdc/sample.html')
    if all_data_columb.status_code:
        data = all_data_columb.text
        result = re.findall(r'<h3.*?>(.*)</h3>', data)
        print(result)