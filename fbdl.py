import requests as req
import json
import os

os.system('clear')
x = '\x1b'
y = '['
z = ';'
abu = x + y + '90m'
merah = x + y + '91m'
hijau = x + y + '92m'
kuning = x + y + '93m'
biru = x + y + '94m'
ungu = x + y + '95m'
birumud = x + y + '96m'
putih = x + y + '37m'
kotak = x + y + '47' + z + '30m'
bersih = x + y + 'm'

try:
	print(f"{kotak} FbVideoDownloader | sanzking {bersih}")
	url = input(f"\n{putih}enter url : ")
	file = input(f"{birumud}masukan nama output : {bersih}")
	print(f"{biru}Sedang mendownload...{bersih}")
	raw = req.get(f"https://fzn-gaz.herokuapp.com/api/fbdl?url={url}", timeout=5).text
	js = json.loads(raw)
	ah = js['kualitasHD']
	r = req.get(ah, allow_redirects=True)
	open(f'/sdcard/{file}.mp4', 'wb').write(r.content)
	print(f"{hijau}file berhasil {putih}disimpan {hijau}di penyimpanan {putih}internal\n{putih}dengan nama {hijau}{file}.mp4{bersih}")
except KeyError:
	print(f"{merah}Url yang anda masukan salah!!!{bersih}")
except KeyboardInterrupt:
	print(f"{merah}Diberhentikan!!!{bersih}")