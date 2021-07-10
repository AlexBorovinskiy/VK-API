def sent_report_to_vk():
    import pandas as pd
    import numpy as np
    import vk_api
    import random

    from datetime import datetime

    print('Libraries are imported')
    
    data = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vR-ti6Su94955DZ4Tky8EbwifpgZf_dTjpBdiVH0Ukhsq94jZdqoHuUytZsFZKfwpXEUCKRFteJRc9P/pub?gid=889004448&single=true&output=csv')

    views = data.query('event == "view"').groupby('date').event.count()

    clicks = data.query('event == "click"').groupby('date').event.count()

    ctr = clicks / views

    views_diff = ((views[-1] - views[-2]) / views[-2] * 100).round()

    clicks_diff = ((clicks[-1] - clicks[-2]) / clicks[-2] * 100).round()

    ctr_diff = ((ctr[-1] - ctr[-2]) / ctr[-2] * 100).round()

    money = data.ad_cost.unique()/1000*views

    money_diff = ((money[1] - money[0]) / money[0] * 100).round()

    print('Data is read and metrics are calculated')

    message = f"""Отчет по объявлению 121288 за 2 апреля
    Траты: {money[1]} рублей ({money_diff}%)
    Показы: {views_2} ({views_diff}%)
    Клики: {clicks_2} ({clicks_diff}%)
    CTR: {ctr_2} ({ctr_diff}%)
    """

    with open(f'report-2019-04-02.txt', 'w') as f:
        f.write(message)


    print('Report is made')

    app_token = '*********************************************************************************'
    chat_id = 1
    my_id = 'borovinskiy'
    vk_session = vk_api.VkApi(token=app_token)
    vk = vk_session.get_api()

    vk.messages.send(
        chat_id=chat_id,
        random_id=random.randint(1, 2 ** 31),
        message=message)

    print('Report is sent')