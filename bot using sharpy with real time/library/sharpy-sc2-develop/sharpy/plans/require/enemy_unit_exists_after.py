import warnings

from sc2 import UnitTypeId

from sharpy.plans.require.require_base import RequireBase


class EnemyUnitExistsAfter(RequireBase):
    """
    Checks if enemy has units of the type based on the information we have seen.
    """

    def __init__(self, unit_type: UnitTypeId, count: int = 1):
        assert unit_type is not None and isinstance(unit_type, UnitTypeId)
        assert count is not None and isinstance(count, int)
        super().__init__()

        self.unit_type = unit_type
        self.count = count

    def check(self) -> bool:
        enemy_count = self.knowledge.enemy_units_manager.unit_count(self.unit_type)
        enemy_count += self.knowledge.lost_units_manager.enemy_lost_type(self.unit_type)

        if enemy_count is None:
            return False

        if enemy_count >= self.count:
            return True

        return False


class RequiredEnemyUnitExistsAfter(EnemyUnitExistsAfter):
    def __init__(self, unit_type: UnitTypeId, count: int = 1):
        warnings.warn(
            "'RequiredEnemyUnitExistsAfter' is deprecated, use 'EnemyUnitExistsAfter' instead", DeprecationWarning, 2
        )
        super().__init__(unit_type, count)
