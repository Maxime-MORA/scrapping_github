def githubConnect(driver, email, password, display) :
    driver.get('https://github.com/login') #Get url with the driver

    driver.find_element_by_id('login_field').send_keys(email) #Recuperation et remplissage du login
    driver.find_element_by_id('password').send_keys(password) #Recuperation et remplissage du password
    driver.find_element_by_name("commit").click() #Soumission du formulaire

    if (display):
        if (driver.title == "GitHub"): #Verification de connexion
            print("Connecte sur le compte : " + email)
            return True
        else:
            print("Connexion non etablie")
            return False