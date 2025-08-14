import keyring

def setPass(uName, pasw, service="KEK"):
    keyring.set_password(service, uName, pasw)

def getPass(uName, service="KEK"):
    return keyring.get_password(service, uName)