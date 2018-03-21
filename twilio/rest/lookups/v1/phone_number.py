# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class PhoneNumberList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the PhoneNumberList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberList
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberList
        """
        super(PhoneNumberList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, phone_number):
        """
        Constructs a PhoneNumberContext

        :param phone_number: The phone_number

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number, )

    def __call__(self, phone_number):
        """
        Constructs a PhoneNumberContext

        :param phone_number: The phone_number

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Lookups.V1.PhoneNumberList>'


class PhoneNumberPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the PhoneNumberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberPage
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberPage
        """
        super(PhoneNumberPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PhoneNumberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        """
        return PhoneNumberInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Lookups.V1.PhoneNumberPage>'


class PhoneNumberContext(InstanceContext):
    """  """

    def __init__(self, version, phone_number):
        """
        Initialize the PhoneNumberContext

        :param Version version: Version that contains the resource
        :param phone_number: The phone_number

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        """
        super(PhoneNumberContext, self).__init__(version)

        # Path Solution
        self._solution = {'phone_number': phone_number, }
        self._uri = '/PhoneNumbers/{phone_number}'.format(**self._solution)

    def fetch(self, country_code=values.unset, type=values.unset,
              add_ons=values.unset, add_ons_data=values.unset):
        """
        Fetch a PhoneNumberInstance

        :param unicode country_code: The country_code
        :param unicode type: The type
        :param unicode add_ons: The add_ons
        :param dict add_ons_data: The add_ons_data

        :returns: Fetched PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        """
        params = values.of({
            'CountryCode': country_code,
            'Type': serialize.map(type, lambda e: e),
            'AddOns': serialize.map(add_ons, lambda e: e),
        })

        params.update(serialize.prefixed_collapsible_map(add_ons_data, 'AddOns'))
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return PhoneNumberInstance(self._version, payload, phone_number=self._solution['phone_number'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Lookups.V1.PhoneNumberContext {}>'.format(context)


class PhoneNumberInstance(InstanceResource):
    """  """

    class Type(object):
        LANDLINE = "landline"
        MOBILE = "mobile"
        VOIP = "voip"

    def __init__(self, version, payload, phone_number=None):
        """
        Initialize the PhoneNumberInstance

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        """
        super(PhoneNumberInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'caller_name': payload['caller_name'],
            'country_code': payload['country_code'],
            'phone_number': payload['phone_number'],
            'national_format': payload['national_format'],
            'carrier': payload['carrier'],
          """
          'fraud': payload['fraud'],
          """
            'add_ons': payload['add_ons'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'phone_number': phone_number or self._properties['phone_number'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        """
        if self._context is None:
            self._context = PhoneNumberContext(self._version, phone_number=self._solution['phone_number'], )
        return self._context

    @property
    def caller_name(self):
        """
        :returns: The caller_name
        :rtype: unicode
        """
        return self._properties['caller_name']

    @property
    def country_code(self):
        """
        :returns: The country_code
        :rtype: unicode
        """
        return self._properties['country_code']

    @property
    def phone_number(self):
        """
        :returns: The phone_number
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def national_format(self):
        """
        :returns: The national_format
        :rtype: unicode
        """
        return self._properties['national_format']

    @property
    def carrier(self):
        """
        :returns: The carrier
        :rtype: unicode
        """
        return self._properties['carrier']

    @property
    def fraud(self):
        """
        :returns: The fraud
        :rtype: unicode
        """
        return self._properties['fraud']

    @property
    def add_ons(self):
        """
        :returns: The add_ons
        :rtype: dict
        """
        return self._properties['add_ons']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, country_code=values.unset, type=values.unset,
              add_ons=values.unset, add_ons_data=values.unset):
        """
        Fetch a PhoneNumberInstance

        :param unicode country_code: The country_code
        :param unicode type: The type
        :param unicode add_ons: The add_ons
        :param dict add_ons_data: The add_ons_data

        :returns: Fetched PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        """
        return self._proxy.fetch(
            country_code=country_code,
            type=type,
            add_ons=add_ons,
            add_ons_data=add_ons_data,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Lookups.V1.PhoneNumberInstance {}>'.format(context)
