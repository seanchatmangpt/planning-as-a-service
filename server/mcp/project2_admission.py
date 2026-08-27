from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
import re

_SHA1 = re.compile(r"^[0-9a-f]{40}$")
_ALLOWED_AUTHORITY = "SELECT|CONSTRUCT|VERIFY"


@dataclass(frozen=True, slots=True)
class Admission:
    repo: str
    base: str
    head: str
    authority: str
    direct_actuation: bool = False


class AdmissionRefused(ValueError):
    pass


def admit_project2_subject(subject: Admission) -> str:
    """Admit an exact Project #2 subject and return a deterministic receipt digest.

    This is an observation/construct boundary only. It never grants DO authority.
    """
    if not subject.repo or "/" not in subject.repo:
        raise AdmissionRefused("REFUSED_REPOSITORY_IDENTITY")
    if not _SHA1.fullmatch(subject.base) or not _SHA1.fullmatch(subject.head):
        raise AdmissionRefused("REFUSED_NON_EXACT_SUBJECT")
    if subject.authority != _ALLOWED_AUTHORITY:
        raise AdmissionRefused("REFUSED_AUTHORITY_SCOPE")
    if subject.direct_actuation:
        raise AdmissionRefused("REFUSED_AMBIENT_DO_AUTHORITY")

    payload = {
        "authority": subject.authority,
        "base": subject.base,
        "direct_actuation": False,
        "head": subject.head,
        "repo": subject.repo,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return sha256(encoded).hexdigest()
