from zope.component import getUtility
from zope.formlib import form
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.browser.account import AccountPanelSchemaAdapter
from plone.app.users.browser.personalpreferences import UserDataPanel
from Products.CMFDefault.formlib.widgets import FileUploadWidget
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plonesocial.auth.rpx.browser.userdataschema import IRPXUserDataSchemaProvider


class RPXUserDataPanelAdapter(AccountPanelSchemaAdapter):

    # def _getProperty(self, name):
    #     """ PlonePAS encodes all unicode coming from PropertySheets.
    #         Decode before sending to formlib. """
    #     value = self.context.getProperty(name, '')
    #     if value:
    #         return safe_unicode(value)
    #     return value

    # def get_company(self):
    #     return self._getProperty('company')

    # def set_company(self, value):
    #     if value is None:
    #         value = ''
    #     return self.context.setMemberProperties({'company': value})

    # def get_companyrole(self):
    #     return self._getProperty('companyrole')

    # def set_companyrole(self, value):
    #     if value is None:
    #         value = ''
    #     return self.context.setMemberProperties({'companyrole': value})

    # def get_research_area(self):
    #     return self._getProperty('research_area')

    # def set_research_area(self, value):
    #     if value is None:
    #         value = ''
    #     return self.context.setMemberProperties({'research_area': value})

    # def get_keywords(self):
    #     return self._getProperty('keywords')

    # def set_keywords(self, value):
    #     if value is None:
    #         value = ''
    #     return self.context.setMemberProperties({'keywords': value})

    # def get_multimedialinks(self):
    #     return self._getProperty('multimedialinks')

    # def set_multimedialinks(self, value):
    #     if value is None:
    #         value = ''
    #     return self.context.setMemberProperties({'multimedialinks': value})

    # company = property(get_company, set_company)
    # companyrole = property(get_companyrole, set_companyrole)
    # research_area = property(get_research_area, set_research_area)
    # keywords = property(get_keywords, set_keywords)
    # multimedialinks = property(get_multimedialinks, set_multimedialinks)


class RPXUserDataPanel(UserDataPanel):

    def __init__(self, context, request):
        """ Load the UserDataSchema at view time.

        (Because doing getUtility for IUserDataSchemaProvider fails at startup
        time.)
        """
        super(UserDataPanel, self).__init__(context, request)
        util = getUtility(IUserDataSchemaProvider)
        base_schema = util.getSchema()
        base_field = form.FormFields(base_schema)
        rpx_util = getUtility(IRPXUserDataSchemaProvider)
        rpx_schema = rpx_util.getSchema()
        rpx_field = form.FormFields(rpx_schema)
        #make field in right order
        self.form_fields = base_field.select('fullname') + \
                           base_field.select('email') + \
                           rpx_field + \
                           base_field.omit('email').omit('fullname')
        #import pdb; pdb.set_trace()
        self.form_fields['portrait'].custom_widget = FileUploadWidget


class RPXUserDataConfiglet(RPXUserDataPanel):
    """ """
    template = ViewPageTemplateFile('account-configlet.pt')
