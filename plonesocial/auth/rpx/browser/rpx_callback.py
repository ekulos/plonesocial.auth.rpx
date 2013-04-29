from zope.interface import implements, Interface
from zope import event
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.PlonePAS.events import UserLoggedInEvent
from Products.PlonePAS.events import UserInitialLoginInEvent


class IRPXCallback(Interface):
    """RPXCallback browser view interface"""


class RPXCallback(BrowserView):
    """
    RPXCallback browser view
    """
    implements(IRPXCallback)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        if self.portal_membership.isAnonymousUser():
            session = self.context.session_data_manager.getSessionData()
            creds = session.get('rpx_credentials', {})
            if not creds:
                msg = (u'RPX authentication has failed. Try again later. '
                    u'You can still register login with your Plone username.')

                util = self.context.plone_utils
                util.addPortalMessage(msg, 'error')
            self.request.RESPONSE.redirect(
                            '%s/@@rpx_register' % self.portal.absolute_url())
        else:
            member = self.portal_membership.getAuthenticatedMember()
            self.portal_membership.createMemberArea()
            if self.portal_membership.setLoginTimes():
                event.notify(UserInitialLoginInEvent(member))
            else:
                event.notify(UserLoggedInEvent(member))


            self.request.RESPONSE.redirect(
                    '%s/login_next' % self.portal.absolute_url()
            )

            return

            # url = self.request.get('came_from')
            # if url is not None:
            #     if type(url) == list:
            #         url = url[0]
            #     self.request.RESPONSE.redirect(url)
            # else:
            #     self.request.RESPONSE.redirect(
            #         '%s/login_next' % self.portal.absolute_url()
            #     )

    @property
    def portal_membership(self):
        return getToolByName(self.context, 'portal_membership')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()
