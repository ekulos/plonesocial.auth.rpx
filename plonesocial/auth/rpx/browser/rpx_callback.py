from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


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

        session = self.context.session_data_manager.getSessionData()
        creds = session.get('rpx_credentials', {})
        if creds:
            member = self.portal_membership.getAuthenticatedMember()
            if not member.getProperty('company'):
                self.request.RESPONSE.redirect(
                            '%s/@@rpx_register' % self.portal.absolute_url())
                return
        url = self.request.get('came_from')
        if url is not None:
            self.request.RESPONSE.redirect(url[0])
        else:
            self.request.RESPONSE.redirect(self.portal.absolute_url())

    @property
    def portal_membership(self):
        return getToolByName(self.context, 'portal_membership')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()
