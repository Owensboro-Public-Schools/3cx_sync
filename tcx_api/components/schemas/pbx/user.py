from typing import List
from tcx_api.components.schemas.pbx.enums import (
    Authentication,
    OfficeHoursBits,
    UserTag,
)

from tcx_api.components.schemas.pbx.extension_rule import ExtensionRule
from tcx_api.components.schemas.pbx.forwarding_profile import ForwardingProfile
from tcx_api.components.schemas.pbx.schedule import Schedule
from tcx_api.components.schemas.pbx.schemas import (
    Greeting,
    Phone,
    UserGroup,
    VMEmailOptionsType,
    VMPlayMsgDateTimeType,
)


class User:
    def __init__(
        self,
        Id: int,
        AccessPassword: str = None,
        AllowLanOnly: bool = None,
        AllowOwnRecordings: bool = None,
        AuthID: str = None,
        AuthPassword: str = None,
        Blfs: str = None,
        BreakTime: Schedule | dict = None,
        CallScreening: bool = None,
        CallUsEnableChat: bool = None,
        CallUsEnablePhone: bool = None,
        CallUsEnableVideo: bool = None,
        CallUsRequirement: Authentication = None,
        ClickToCallId: str = None,
        ContactImage: str = None,
        CurrentProfileName: str = None,
        DeskphonePassword: str = None,
        DisplayName: str = None,
        EmailAddress: str = None,
        Enable2FA: bool = None,
        Enabled: bool = None,
        EnableHotdesking: bool = None,
        FirstName: str = None,
        ForwardingExceptions: List[ExtensionRule] = None,
        ForwardingProfiles: List[ForwardingProfile] = None,
        GoogleSignInEnabled: bool = None,
        Greetings: List[Greeting] = None,
        Groups: List[UserGroup] = None,
        HideInPhonebook: bool = None,
        HotdeskingAssignment: str = None,
        Hours: List[Schedule] = None,
        Internal: bool = None,
        IsRegistered: bool = None,
        Language: str = None,
        LastName: str = None,
        Mobile: str = None,
        MS365CalendarEnabled: bool = None,
        MS365ContactsEnabled: bool = None,
        MS365SignInEnabled: bool = None,
        MS365TeamsEnabled: bool = None,
        MyPhoneAllowDeleteRecordings: bool = None,
        MyPhoneHideForwardings: bool = None,
        MyPhonePush: bool = None,
        MyPhoneShowRecordings: bool = None,
        Number: str = None,
        OfficeHoursProps: List[OfficeHoursBits] = None,
        OutboundCallerID: str = None,
        Phones: List[Phone] = None,
        PinProtected: bool = None,
        PinProtectTimeout: int = None,
        PrimaryGroupId: int = None,
        PromptSet: str = None,
        ProvFile: str = None,
        ProvLink: str = None,
        RecordCalls: bool = None,
        RecordExternalCallsOnly: bool = None,
        Require2FA: bool = None,
        SendEmailMissedCalls: bool = None,
        SIPID: str = None,
        Tags: List[UserTag] = None,
        VMDisablePinAuth: bool = None,
        VMEmailOptions: VMEmailOptionsType = None,
        VMEnabled: bool = None,
        VMPIN: str = None,
        VMPlayCallerID: bool = None,
        VMPlayMsgDateTime: VMPlayMsgDateTimeType = None,
        WebMeetingApproveParticipants: bool = None,
        WebMeetingFriendlyName: str = None,
    ):
        self.Id = Id
        self.AccessPassword = AccessPassword
        self.AllowLanOnly = AllowLanOnly
        self.AllowOwnRecordings = AllowOwnRecordings
        self.AuthID = AuthID
        self.AuthPassword = AuthPassword
        self.Blfs = Blfs
        # self.BreakTime = BreakTime
        self.BreakTime = (
            BreakTime
            if isinstance(BreakTime, Schedule)
            else Schedule(**BreakTime) if isinstance(BreakTime, dict) else None
        )
        # self.BreakTime =  BreakTime if isinstance(Breaktime, Schedule) else Schedule(**BreakTime) if BreakTime is not None
        self.CallScreening = CallScreening
        self.CallUsEnableChat = CallUsEnableChat
        self.CallUsEnablePhone = CallUsEnablePhone
        self.CallUsEnableVideo = CallUsEnableVideo
        self.CallUsRequirement = CallUsRequirement
        self.ClickToCallId = ClickToCallId
        self.ContactImage = ContactImage
        self.CurrentProfileName = CurrentProfileName
        self.DeskphonePassword = DeskphonePassword
        self.DisplayName = DisplayName
        self.EmailAddress = EmailAddress
        self.Enable2FA = Enable2FA
        self.Enabled = Enabled
        self.EnableHotdesking = EnableHotdesking
        self.FirstName = FirstName
        self.ForwardingExceptions = ForwardingExceptions
        self.ForwardingProfiles = ForwardingProfiles
        self.GoogleSignInEnabled = GoogleSignInEnabled
        self.Greetings = Greetings
        self.Groups = Groups
        self.HideInPhonebook = HideInPhonebook
        self.HotdeskingAssignment = HotdeskingAssignment
        self.Hours = Hours
        self.Internal = Internal
        self.IsRegistered = IsRegistered
        self.Language = Language
        self.LastName = LastName
        self.Mobile = Mobile
        self.MS365CalendarEnabled = MS365CalendarEnabled
        self.MS365ContactsEnabled = MS365ContactsEnabled
        self.MS365SignInEnabled = MS365SignInEnabled
        self.MS365TeamsEnabled = MS365TeamsEnabled
        self.MyPhoneAllowDeleteRecordings = MyPhoneAllowDeleteRecordings
        self.MyPhoneHideForwardings = MyPhoneHideForwardings
        self.MyPhonePush = MyPhonePush
        self.MyPhoneShowRecordings = MyPhoneShowRecordings
        self.Number = Number
        Authentication["None"]
        self.OfficeHoursProps = (
            [OfficeHoursBits[e] for e in OfficeHoursProps] if OfficeHoursProps else None
        )

        self.OutboundCallerID = OutboundCallerID
        self.Phones = Phones
        self.PinProtected = PinProtected
        self.PinProtectTimeout = PinProtectTimeout
        self.PrimaryGroupId = PrimaryGroupId
        self.PromptSet = PromptSet
        self.ProvFile = ProvFile
        self.ProvLink = ProvLink
        self.RecordCalls = RecordCalls
        self.RecordExternalCallsOnly = RecordExternalCallsOnly
        self.Require2FA = Require2FA
        self.SendEmailMissedCalls = SendEmailMissedCalls
        self.SIPID = SIPID
        self.Tags = Tags
        self.VMDisablePinAuth = VMDisablePinAuth
        self.VMEmailOptions = VMEmailOptions
        self.VMEnabled = VMEnabled
        self.VMPIN = VMPIN
        self.VMPlayCallerID = VMPlayCallerID
        self.VMPlayMsgDateTime = VMPlayMsgDateTime
        self.WebMeetingApproveParticipants = WebMeetingApproveParticipants
        self.WebMeetingFriendlyName = WebMeetingFriendlyName