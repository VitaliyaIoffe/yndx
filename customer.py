from enum import Enum

BASE = 10


class BudgetType(Enum):
    PASSIVE = 0
    EMPLOYED = 1
    OWN_BUSINESS = 2
    UNEMPLOYED = 3


class Goal(Enum):
    MORTGAGE = -2
    BUSINESS = -0.5
    AUTO = 0
    CUSTOMER = 1.5


class RetiredAge(Enum):
    """Current retired age"""
    FEMALE = 58
    MALE = 63


class Sex(Enum):
    FEMALE = 0
    MALE = 1


class Customer:
    def __init__(self, **kwargs) -> None:
        self.age: int = kwargs.pop('age')
        self.sex: Sex = kwargs.pop('sex')
        self.budget_type: BudgetType = kwargs.pop('budget_type')
        self.revenue: float = kwargs.pop('revenue')
        self.rank: int = kwargs.pop('rank')
        self.credit: float = kwargs.pop('credit')
        self.years: int = kwargs.pop('years')
        self.goal: Goal = kwargs.pop('goal')
        self.mode: float = self.get_mode_percent()

    def get_mode_percent(self) -> float:
        return self.goal.value

    def get_pay_sum(self) -> float:
        pay = (self.credit * (1 + self.years * (BASE + self.mode))) / self.years
        return pay

    def is_retire(self) -> bool:
        """is person retired or not at the end of credit years

        To be honest idk what means 'на момент возврата кредита'.
        Have to check with product owner.
        """
        if self.sex == Sex.FEMALE and self.age + self.years >= RetiredAge.FEMALE.value:
            return False
        elif self.sex == Sex.MALE and self.age + self.years >= RetiredAge.MALE.value:
            return False
        elif self.sex != Sex.FEMALE and self.sex != Sex.MALE:
            raise TypeError("something goes wrong")
        return True

    def is_enough_money(self) -> bool:
        return self.revenue * 3 > self.years * self.credit

    def is_good_rank(self) -> bool:
        if not isinstance(self.rank, int) or self.rank not in [-2, -1, 0, 1, 2]:
            raise TypeError("something goes wrong")
        return self.rank != -2

    def is_unemployed(self) -> bool:
        budget_types = [budget_type.value for budget_type in BudgetType]
        if self.budget_type not in budget_types:
            raise TypeError("something goes wrong")
        return self.budget_type == BudgetType.UNEMPLOYED

    def is_easy_to_pay(self) -> bool:
        return not 2 * self.get_pay_sum() > self.revenue

    def is_person_good_for_credit(self) -> bool:
        return (not self.is_retire()
                and not self.is_unemployed()
                and self.is_good_rank()
                and not self.is_unemployed()
                and self.is_easy_to_pay())






