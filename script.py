for currency in currencies:
        while True:
            try:
                # Opening the connection and grabbing the page
                my_url = f'https://49239ea5-c38e-4dcf-ba90-1d21c9dc2d68-00-1tjjbrmlld1k8.janeway.replit.dev/-{currency.lower()}-historical-data'
                option = Options()
                option.headless = False
                driver = webdriver.Chrome(options=option)
                driver.get(my_url)
                driver.maximize_window()
                   
                # Clicking on the date button
                date_button = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH,
                            "/html/body/div[5]/section/div[8]/div[3]/div/div[2]/span")))
                
                date_button.click()
                
                # Sending the start date
                start_bar = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH,
                            "/html/body/div[7]/div[1]/input[1]")))
                            
                start_bar.clear()
                start_bar.send_keys(start)

                # Sending the end date
                end_bar = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH,
                            "/html/body/div[7]/div[1]/input[2]")))
                            
                end_bar.clear()
                end_bar.send_keys(end)
               
                # Clicking on the apply button
                apply_button = WebDriverWait(driver,20).until(
                		EC.element_to_be_clickable((By.XPATH,
                		"/html/body/div[7]/div[5]/a")))
                
                apply_button.click()
                sleep(5)
                
                # Getting the tables on the page and quiting
                dataframes = pd.read_html(driver.page_source)
                driver.quit()
                print(f'{currency} scraped.')
                break
            
            except:
                driver.quit()
                print(f'Failed to scrape {currency}. Trying again in 30 seconds.')
                sleep(30)
                continue