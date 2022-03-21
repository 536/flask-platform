import os
import random
import string

import requests
from flask import Blueprint, session, redirect, request, abort, url_for

bp = Blueprint('auth', __name__, url_prefix='/auth')

REDIRECT_URI = 'http://127.0.0.1:5000/auth/login'
FEISHU_APP_URL = 'https://open.feishu.cn/open-apis/authen/v1/index?redirect_uri={REDIRECT_URI}&app_id={APPID}&state={STATE}'


def get_access_token():
    response = requests.post(
        url='https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal',
        headers={
            "Content-Type": "application/json; charset=utf-8",
        },
        json={
            "app_id": os.environ.get('FEISHU_APP_ID'),
            "app_secret": os.environ.get('FEISHU_APP_SECRET'),
        },
        verify=False,
    )
    return response.json()['tenant_access_token']


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user'):
        return redirect(url_for('platform.index'))
    else:
        code = request.args.get('code')
        if code:
            if session['STATE'] == request.args.get('state'):
                access_token = get_access_token()
                response = requests.post(
                    url='https://open.feishu.cn/open-apis/authen/v1/access_token',
                    headers={
                        "Authorization": "Bearer {access_token}".format(access_token=access_token),
                        "Content-Type": "application/json; charset=utf-8",
                    },
                    json={
                        "grant_type": "authorization_code",
                        "code": code,
                    },
                    verify=False
                )
                session['user'] = response.json()['data']
                return redirect(url_for('platform.index'))
            else:
                return abort(400, 'Error state in response.')
        else:
            session['STATE'] = ''.join(random.choice(string.ascii_letters) for _ in range(10))
            return redirect(FEISHU_APP_URL.format(
                REDIRECT_URI=REDIRECT_URI,
                APPID=os.environ.get('FEISHU_APP_ID'),
                STATE=session['STATE'],
            ))


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session['user'] = None
    return redirect(url_for('platform.index'))
