from second_kill.spider_requests import SpiderSession, QrLogin, JdSecondKill

if __name__ == '__main__':
    second_kill = JdSecondKill()
    second_kill.login_by_qr_code()

