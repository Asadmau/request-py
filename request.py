import requests

ac_id = 'https://learn.stikombanyuwangi.ac.id'
try:
    r = requests.get(ac_id)
    if r.status_code == 200:
        print(f'Success ! status code {r}')
        print('Content ',r.text)
    else:
        print(f'terjadi kesalahan di !{r.status_code}')
except Exception as e:
    print('error 404')
print('end code')
