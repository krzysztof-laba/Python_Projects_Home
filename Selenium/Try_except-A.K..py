from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import time
from selenium.common.exceptions import NoSuchElementException
from pynput.keyboard import Key, Controller
import re
import os


#######################################################################################################################

#  Lokalization of chrome driver:
chrome_driver = "C:\Python-geckodriver\chromedriver.exe"

# Create object for selenium driver:
website = webdriver.Chrome(chrome_driver)

#######################################################################################################################

#######################################################################################################################

# WYBRAĆ USTAWIENIA PRZED I PO PIELGRZYMKACH
print('*******************************************************')

time_sleep = 0 # Czas po którym rozpocząć wyprawy (w min).
print("Zacznij wyprawy za minut:", time_sleep)

ilosc_wypraw = 1
print("Ustawiona ilość wypraw:	 ", ilosc_wypraw)

zestaw_eq = str(15)
print("Ubierzesz zestaw:		 ", zestaw_eq)

ubrac_wyprawkowy = True
print("Ubrać wyprawkowy:		 ", ubrac_wyprawkowy)

oddac_wyprawkowy = True
print("Oddać wyprawkowy:		 ", oddac_wyprawkowy)

wylogowac_web_browser = True
print("Wylogować:				 ", wylogowac_web_browser)

close_web_browser = True
print("Zamknąć przeglądarkę:	 ", close_web_browser)

shutdown_PC = False
print("Wyłączyć PC:			 ", shutdown_PC)

retries = 5

print('*******************************************************')

#######################################################################################################################


# Initialization of starting web browser and logging.
def initialization():
	# Open web browser and website:
	website.get("https://bloodwars.interia.pl")

	# Close RODO regulations.
	try:
		rodo = website.find_element_by_class_name('rodo-popup-agree')
		rodo.click()
		print("Zamknięto okno 'RODO'.")
	except:
		print("Brak okna 'RODO'.")

	# Logowanie i wybranie krainy:
	print("Logowanie i wybieranie krainy...")

	# Create object for login to the website:
	username = website.find_element_by_id('i_login')
	password = website.find_element_by_name('password')
	combobox = website.find_element_by_id('i_realm')
	login = website.find_element_by_name('submit')

	# Fill in the fields:
	username.click()
	username.send_keys("Alexander82")
	password.click()
	password.send_keys("dzieńsądu")

	# Choose the right land:
	combobox.click()
	i = 1
	while i <= 2:
		combobox.send_keys(Keys.ARROW_DOWN)
		i += 1
	combobox.click()
	time.sleep(randint(1, 2))

	# Login to a BW:
	login.click()
	if check_if_page_exists() == True:
		print("Zalogowano do BW.")

	# Wait time before expeditions start.
	if time_sleep >= 1:
		print("Program czeka około:", time_sleep, "minut by zacząć pielgrzymki.")
		print("Odświeżenie przeglądarki:")
		for i in range(int(time_sleep)):
			print("Minuta: ", i + 1)
			time.sleep(randint(58, 70))
			refresh_page()
	else:
		print("Brak opóźnienia z wystartowaniem wypraw.")


# Check if page exists or there is not a technical break by checking if Alexander82 exists.
def check_if_page_exists():
	print("* PIERWSZE sprawdzenie czy strona jest wyświetlona. *")
	# Checking after time elapsed:
	time.sleep(1)
	for i in retries:
		try:
			alexander = website.find_element_by_class_name('me')
			print("Strona działa. Alexander82 widoczny.")
			return alexander.is_enabled() # <----------------------------- Dać drugi return by po tym był refresh po expie.
		except NoSuchElementException:
			print("Brak strony BW. Alexander NIE widoczny.")
			time.sleep(randint(i^2, i^2 + 10))
			refresh_page();
			print("**" + i + "sprawdzenie czy strona jest wyświetlona. **")
			return False
		print("! ! ! S T R O N A	W Y G A S Ł A ! ! !")


# Checking amount of money in PLN needed to expeditions.
def check_amount_of_money():
	# Read amount of money from site.
	time.sleep(1)
	if check_if_page_exists() == True:
		wartosc_pln = website.find_element_by_xpath("//span[contains(@style, 'font-size: 10px;') and contains(text(),'PLN')]")
		wartosc_w_PLN = wartosc_pln.text.replace(" ", "").replace("PLN", "") # Removed spaces and value 'PLN'.
		print("Sprawdzenie ilości pieniędzy:", wartosc_w_PLN, "PLN")

		# Check money and buy if it is less then 6500 pln.
		if int(wartosc_w_PLN) < 6500:
			print("Ilość pln poniżej 6500 !!!")
			# Go to page 'sklep'.
			sklep = website.find_element_by_xpath("//a[@href='?a=townshop']") # Zakładka sklep.
			time.sleep(randint(3, 6))
			sklep.click()
			# Buy 20 000 pln.
			if check_if_page_exists() == True:
				sprzedaj = website.find_element_by_xpath("//a[contains(@class, 'sellItem')]") # Sprzedaż złomu.
				time.sleep(randint(3, 6))
				sprzedaj.click()
				if check_if_page_exists() == True:
					print("Sprzedano złom za 20.000 pln.")
		else:
			print("Ilość pln OK!")


# Check attribute of the page expedition and NAVIGATE if it is not active/open.
def navigate_to_page_expeditions():
	if check_if_page_exists() == True:
		# Check if a page expeditions.
		time.sleep(randint(1, 2))
		wyprawy = website.find_element_by_xpath("//a[@href='?a=quest']")
		print("Sprawdzenie czy jesteś na zakładce wypraw:")
		print("Atrybutu klasy wyprawy: menulink/activemenulink):", wyprawy.get_attribute('class'))
		if wyprawy.get_attribute('class') == 'activemenulink':
			print("Jesteś na zakładce wyprawy.")
		else:
			# Navigate to a page with expeditons.
			time.sleep(randint(3, 7))
			wyprawy.click()
			if check_if_page_exists() == True:
				print("Przekierowano na stronę wypraw.")


# Check amount of expeditions.
def check_amount_of_expeditions():
	# Check if page of expeditions and navigate if not.
	navigate_to_page_expeditions()
	# Check amount of expeditions.
	amount_of_exp = website.find_element_by_xpath("//div[contains(@style, 'margin-top: 10px; margin-bottom: 20px;')]")
	amount_of_exp = amount_of_exp.text.replace(" ", "")
	amount_of_exp = amount_of_exp.replace("Pozostałowypraw:", "")
	if re.search('/', amount_of_exp[0:2]):
		if amount_of_exp[0:1] != '0':
			print("--> POZOSTAŁO EKSPEDYCJI DO WYKONANIA:", amount_of_exp[0:1])
			return amount_of_exp[0:1]
		else:
			print("BRAK EKSPEDYCJI DO WYKONANIA!")
			return amount_of_exp[0:1]
	else:
		print("--> POZOSTAŁO EKSPEDYCJI DO WYKONANIA:", amount_of_exp[0:2])
		return amount_of_exp[0:2]


# Check if button 'Start Expedition' exists.
def check_button_exp_exists():
	# Check if page with expeditions and navigate if not open.
	navigate_to_page_expeditions()

	# Check if button 'Rozpocznij Wyprawę' exists.
	time.sleep(2)
	try:
		rozpocznij_wyprawe = website.find_element_by_xpath("//input[contains(@value, 'ROZPOCZNIJ WYPRAWĘ')]")
		print("Przycisk 'Rozpocznij wyprawę' istnieje. Wartość:", rozpocznij_wyprawe.is_enabled())
		return rozpocznij_wyprawe.is_enabled()
	except NoSuchElementException:
		print("Brak przycisku 'Rozpocznij wyprawę. Wartość:", "False")
		return False


# Press and release F5 (refresh page).
def refresh_page():
	keyboard = Controller()
	keyboard.press(Key.f5)
	keyboard.release(Key.f5)


# Press and release button 'ENTER'.
def press_enter():
	keyboard = Controller()
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	if check_if_page_exists() == True:
		print("Enter zadziałał - strona odświerzona.")


# Set right expedition, max blood, start expedition and refresh after exp.
def expeditions(exp):
	# Check if page with expeditions and navigate if not open.
	navigate_to_page_expeditions()

	# First time check and set the longest expedition and max amount of blood.
	if exp == int(0):
		# Set the longest expedition.
		time.sleep(randint(2, 5))
		zaznacz_pielgrzymke = website.find_element_by_xpath("//div[contains(@id, 'questDiff_2')]")
		zaznacz_pielgrzymke.click()
		# Set maximum amount of blood.
		time.sleep(randint(2, 4))
		max_moc_krwi = website.find_element_by_xpath("//input[contains(@onclick, 'clickMax(12)')]")
		max_moc_krwi.click()
		print("Ustawiono max moc krwi.")
	else:
		print("Max krew ustawiona.")

	# Start an expedition.
	time.sleep(randint(3, 6))
	rozpocznij_wyprawe = website.find_element_by_xpath("//input[contains(@value, 'ROZPOCZNIJ WYPRAWĘ')]")
	expedition_no = exp + 1
	print("Pielgrzymka nr:", expedition_no, "z", ilosc_wypraw)
	print("Zostało wypraw:", ilosc_wypraw - expedition_no)
	rozpocznij_wyprawe.click()
	time.sleep(randint(185, 200))
	if check_if_page_exists() == True:
		time.sleep(randint(1, 2)) # <------------------------------------------------- tu ten refresh ma się inicjować.
		refresh_page()


# Check if a page equipment and if not Navigation to a page with equipment.
def navigate_to_page_equipment():
	if check_if_page_exists() == True:
		# Check if a page equipment and if not then Navigate to a page equipment.
		time.sleep(randint(2, 3))
		zbrojownia = website.find_element_by_xpath("//a[@href='?a=equip']")
		print("Sprawdzenie atrybutu klasy:", zbrojownia.get_attribute('class'))
		if zbrojownia.get_attribute('class') == 'activemenulink':
			print("Jesteś na zakładce zbrojownia.")
		else:
			time.sleep(randint(3, 7))
			zbrojownia.click()
			if check_if_page_exists() == True:
				print("Przekierowano na stronę zbrojowni.")


# Choose right combat equipment from save sets.
def choose_combat_eq():
	# Navigate to the page with equipment.
	navigate_to_page_equipment()

	# Choose combat equipment.
	time.sleep((randint(3, 7)))
	print("Wybieranie zestawu nr:", zestaw_eq)
	set_combat_no = website.find_element_by_xpath("//div[contains(@class, 'itemSetNrContainer') and contains(text(), '" + zestaw_eq + "')]")
	set_combat_no.click()
	time.sleep((randint(2, 4)))
	press_enter()
	if check_if_page_exists() == True:
		print("Wybrano zestaw numer:", zestaw_eq)


# Using Flying frame.
def flying_frame(button_name, activity):
	time.sleep(randint(2, 4))
	# Find and select flying frame.
	frame = website.find_element_by_id('selectedItemsBar_combined')
	# On the flying frame find and click right element.
	frame_button_name = frame.find_element_by_name(button_name)
	frame_button_name.click()
	if check_if_page_exists() == True:
		print(activity)


# Choose and dress an expedition's equipments.
def grab_exp_eq():
	# Navigate to the page with equipment.
	navigate_to_page_equipment()

	# Choose en empty equipment for expeditions.
	time.sleep((randint(3, 6)))
	print("Wybieranie pustego wyprawkowego - zestaw nr 12")
	set_empty_equip_expedition = website.find_element_by_xpath("//div[contains(@class, 'itemSetNrContainer') and contains(text(), '12')]")
	set_empty_equip_expedition.click()
	time.sleep((randint(2, 4)))
	press_enter()
	if check_if_page_exists() == True:
		print("Wybrano zestaw numer 12 - pusty wyprawkowy.")

		# Select  equipments of a clan.
		time.sleep((randint(3, 6)))
		odwroć_zaznaczenie_przedmioty_klanowe = website.find_element_by_xpath("//input[contains(@onclick, 'invertSelectTab(20);')]")
		odwroć_zaznaczenie_przedmioty_klanowe.click()
		print("Zaznaczono przedmioty klanowe.")

		# Dress an equipment on expeditions.
		flying_frame('eqsel', 'Ubrano wyprawkowy (tzn. przedmioty klanowe).')


# Navigate to a page with equipment, select clan equipment and return/give back.
def return_exp_eq():
	# Navigate to a page with equipment.
	navigate_to_page_equipment()

	if oddac_wyprawkowy == True:
		# Select clan equipment.
		time.sleep((randint(3, 6)))
		odwroć_zaznaczenie_przedmioty_klanowe = website.find_element_by_xpath("//input[contains(@onclick, 'invertSelectTab(20);')]")
		odwroć_zaznaczenie_przedmioty_klanowe.click()
		print("Zaznaczono przedmioty klanowe.")

		# Return borrowed items (clan equipments).
		flying_frame('armoryPutIn', 'Oddano przedmioty klanowe (wyprawkowy).')
	else:
		print("Nie oddano przedmiotów klanowych.")


# Logout and close a web browser and shutdown computer.
def logout_and_close_web_browser():
	if check_if_page_exists() == True:
		# Logout from BW.
		if wylogowac_web_browser is True:
			time.sleep(randint(5, 10))
			wylogowanie = website.find_element_by_xpath("//a[@href='?a=logout']")
			wylogowanie.click()
			print("Wylogowano z BW.")
		else:
			print("Nie wylogowano z BW.")

	# Close web browser.
	if close_web_browser == True:
		time.sleep(randint(1, 2))
		website.close()
		print("Zamknięto przeglądarkę.")
	else:
		print("Nie zamknięto przeglądarki.")

	# Shutdown PC.
	if shutdown_PC == True:
		print("Sutting down system...")
		time.sleep(10)
		os.system("shutdown -s")
	else:
		print("Nie wyłączono komputera.")



#######################################################################################################################
# 			**************************            P R O G R A M            **************************
#######################################################################################################################

# Start web browser.
initialization()
check_if_page_exists()