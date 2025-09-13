# =============================================================================
#  Copycord
#  Copyright (C) 2021 github.com/Copycord
#
#  This source code is released under the GNU Affero General Public License
#  version 3.0. A copy of the license is available at:
#  https://www.gnu.org/licenses/agpl-3.0.en.html
# =============================================================================

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RoleData:
    """Serializable representation of a guild role.

    Attributes mirror the role properties we care about when cloning
    roles between guilds.  Color is represented as a hex string prefixed
    with ``#`` and permissions are encoded as a decimal string to avoid
    JSON integer size issues.
    """

    id: int
    name: str
    color: str
    hoist: bool
    permissions: str
    mentionable: bool
    position: int
    isEveryone: bool
    managed: bool = False

