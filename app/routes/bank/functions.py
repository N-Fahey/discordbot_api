from fastapi import HTTPException

from app.db import DBSessionDep
from app.model import User
from .schemas import SingleBalanceSchema, ManyBalanceSchema, TransferBalancesSchema, SingleDoleSchema

class GetBalanceByUID:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, uid:int):
        
        async with self.session.begin() as session:
            user = await User.get_user_by_uid(session, uid)

            if user is None:
                raise HTTPException(status_code=404, detail="User not found.")
            return SingleBalanceSchema.model_validate(user)

class GetDoleByUID:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, uid:int):

        async with self.session.begin() as session:
            user = await User.get_user_by_uid(session, uid)
            if user is None:
                raise HTTPException(status_code=404, detail="User not found.")
            
            return SingleDoleSchema.model_validate(user)

class GetTopNBalances:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, user_count:int):
        if user_count == 0:
            user_count = None

        async with self.session.begin() as session:
            users = [user async for user in User.get_users_with_balance(session, user_count)]

            return_dict = {
                'balances': users
                }
            
            return ManyBalanceSchema.model_validate(return_dict)

class DepositAmountByUID:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, uid:int, amount:int):

        async with self.session.begin() as session:
            user = await User.get_user_by_uid(session, uid)
            if user is None:
                raise HTTPException(status_code=404, detail="User not found.")

            await user.deposit(session, amount)
            return SingleBalanceSchema.model_validate(user)

class WithdrawAmountByUID:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, uid:int, amount:int):

        async with self.session.begin() as session:
            user = await User.get_user_by_uid(session, uid)
            if user is None:
                raise HTTPException(status_code=404, detail="User not found.")

            await user.withdraw(session, amount)
            return SingleBalanceSchema.model_validate(user)

class TransferAmountByUIDs:
    def __init__(self, session: DBSessionDep):
        self.session = session
    
    async def execute(self, from_uid:int, to_uid:int, amount:int):

        async with self.session.begin() as session:
            from_user = await User.get_user_by_uid(session, from_uid)
            to_user = await User.get_user_by_uid(session, to_uid)

            if from_user is None or to_user is None:
                raise HTTPException(status_code=404, detail=f"User {from_uid if from_user is None else to_uid} not found.")

            await User.transfer(session, from_user, to_user, amount)
            
            return_dict = {
                'from_uid': from_user.uid,
                'from_balance': from_user.balance,
                'to_uid': to_user.uid,
                'to_balance': to_user.balance,
            }
            return TransferBalancesSchema.model_validate(return_dict)


