import schedule

import time

from etl.pipeline import run_pipeline


schedule.every().day.at("09:00").do(

    run_pipeline

)


while True:

    schedule.run_pending()

    time.sleep(60)
