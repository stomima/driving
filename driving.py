#建立Github專案
#寫台灣部分
#上傳
#寫美國部分
#upload
#最後else部分
#upload

country = input ('請問你是哪國人 （台灣/美國)')
age = input ('請問你的年齡')
# 型別轉換 casting
age = int (age)
if country == '台灣':
	if age >= 18 :
		print ('你可以考駕照')
	else :
		print ('毛長齊再來')
elif country == '美國': # 使用elif 不是if
	if age >= 16 :
		print ('Driving License is avaiale')
	else :
		print ('you are too young')
     