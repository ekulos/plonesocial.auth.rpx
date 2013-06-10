from zope.interface import Interface, implements
from zope import schema
from plonesocial.auth.rpx import rpxMessageFactory


class IRPXUserDataSchemaProvider(Interface):
    """
    """

    def getSchema():
        """
        """


class RPXUserDataSchemaProvider(object):
    implements(IRPXUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IRPXUserDataSchema


class IRPXUserDataSchema(Interface):
    """
    """

    company = schema.TextLine(
        title=rpxMessageFactory(u'label_rpx_company', default=u'Company'),
        description=rpxMessageFactory(u'help_rpx_company',
                      default=u"Enter company name"),
        required=True,
    )

    companyrole = schema.TextLine(
        title=rpxMessageFactory(u'label_rpx_companyrole', default=u'Role'),
        description=rpxMessageFactory(u'help_rpx_companyrole',
                      default=u"Enter your role"),
        required=True,
    )

    research_area = schema.TextLine(
        title=rpxMessageFactory(u'label_rpx_research_area',
                                                    default=u'Research Area'),
        description=rpxMessageFactory(u'help_rpx_research_area',
                      default=u"Enter research area"),
        required=True,
    )

    keywords = schema.TextLine(
        title=rpxMessageFactory(u'label_rpx_keywords', default=u'Keywords'),
        description=rpxMessageFactory(u'help_rpx_keywords',
                      default=u"Enter keywords"),
        required=False,
    )

    multimedialinks = schema.TextLine(
        title=rpxMessageFactory(u'label_rpx_multimedialinks',
                                            default=u'Multimedia links'),
        description=rpxMessageFactory(u'help_rpx_multimedialinks',
                      default=u"Enter Multimedia links"),
        required=False,
    )
