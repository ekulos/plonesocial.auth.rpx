def clear_extra_cookies_on_logout(event):
    """
    Logout event handler.
    When user explicitly logs out from the Logout menu,
    clear our privileges smartcard cookie.
    """

    # Which cookie we want to clear
    cookie_name = 'rpx_credentials'

    request = event.object.REQUEST
    response = request.RESPONSE
    response.expireCookie(cookie_name)
