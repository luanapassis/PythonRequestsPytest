from enum import Enum


class AuthenticationEnum(Enum):
    BASIC = "BASIC"
    NTLM = "NTLM"
    DIGEST = "DIGEST"
    OAUTH1 = "OAUTH1"
    NONE = "NONE"
