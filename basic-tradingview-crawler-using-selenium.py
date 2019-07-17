from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC       
import sys
import time


config = {
    'script': {
        'name': 'Mossad Bands',
        'url': 'https://www.tradingview.com/script/swQodRpo-Mossad-Bands/'
    },
    'chartSymbol': 'BITFINEX:BTCUSD'
}

def addScriptToFavorites(driver):
    r = {'success': False}
    try:
        favButtonCheckedClass = 'i-checked'
        favButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-name="favorite"]')))
        if favButtonCheckedClass not in favButton.get_attribute('class'):
            favButton.click()
    except Exception, e:
        r['error'] = 'Could not favorite script: ' + str(e)
    else:
        r['success'] = True
    finally:
        return r

def addFavoritedIndicatorToChart(driver, indicatorName):
    r = {'success': False}
    indicatorsButton = '#header-toolbar-indicators'
    favoritesButton = 'div.tv-insert-indicator-dialog__tab[title="Favorites"]'
    desiredFavoriteIndicatorItem = 'div.tv-insert-study-item__title-text[title="' + indicatorName + '"]'
    closeIndicatorsDialogButton = 'div.tv-dialog__close.js-dialog__close'
    try:
        driver.execute_script('arguments[0].click();', driver.find_element_by_css_selector(indicatorsButton))
        time.sleep(3)
        driver.execute_script('arguments[0].click();', driver.find_element_by_css_selector(favoritesButton))
    except NoSuchElementException:
        r['error'] = 'Chart GUI does not seem to exist.'
    except Exception, e:
        r['error'] = 'Unexpected error, ' + str(e)
    else:
        try:
            driver.find_element_by_css_selector(desiredFavoriteIndicatorItem).click()
            driver.find_element_by_css_selector(closeIndicatorsDialogButton).click()
        except NoSuchElementException:
            r['error'] = 'Desired indicator was probably not favorited.'
        else:
            r['success'] = True
    finally:
        return r

def tryGrabAnything(driver):
    try:
        studies = driver.find_elements_by_css_selector('.study')
        firstIndicator = studies[1]
        indicatorValues = firstIndicator.find_elements_by_css_selector('.pane-legend-line')
        return [e.get_attribute('innerHTML') for e in indicatorValues]
    except:
        return False
            

def symbolURL(symbol):
    return 'https://www.tradingview.com/chart/?symbol=' + symbol    


# --------------------------------------------------


driver = webdriver.Firefox()

print('Favoriting script "' +config['script']['name'] + '"...')
driver.get(config['script']['url'])
time.sleep(20) # make it actually wait for clickable position

scriptAddedToFavorites = addScriptToFavorites(driver)
if (not scriptAddedToFavorites['success']):
    print('Something went wrong, ' + scriptAddedToFavorites['error'])
    driver.close()
    sys.exit()
print('Favorited successfully.')

print('Opening chart for symbol ' + config['chartSymbol'] + '"...')
driver.get(symbolURL(config['chartSymbol']))
time.sleep(10)

print('Adding indicator "' + config['script']['name'] + '" to chart...')
indicatorAddedToChart = addFavoritedIndicatorToChart(driver, config['script']['name'])
if (not indicatorAddedToChart['success']):
    print('Something went wrong, ' + indicatorAddedToChart['error'])
    #driver.close()
    sys.exit()
print('Added successfully.')

time.sleep(10)
print('Grabbing first pane legend line from second study field...')
grabbie = tryGrabAnything(driver)

if grabbie:
    print(grabbie)
