from fastapi import APIRouter, Depends

from .schemas import HTTPError, SingleBalanceSchema, ManyBalanceSchema, TransferBalancesSchema, SingleDoleSchema, SingleBalanceRequestSchema, TransferAmountRequestSchema
from .functions import GetBalanceByUID, GetDoleByUID, GetTopNBalances, DepositAmountByUID, WithdrawAmountByUID, TransferAmountByUIDs

router = APIRouter(prefix='/bank')

@router.get('/get_balance', response_model=SingleBalanceSchema, responses={404: {'model':HTTPError}})
async def get_balance_by_uid(user_id:int, function: GetBalanceByUID = Depends(GetBalanceByUID)) -> SingleBalanceSchema:
    '''Get a single user's bank balance by Discord unique ID'''
    user_bank = await function.execute(user_id)
    return user_bank

@router.get('/get_dole', response_model=SingleDoleSchema, responses={404: {'model':HTTPError}})
async def get_dole_by_uid(user_id:int, function:GetDoleByUID = Depends(GetDoleByUID)):
    '''Get a single user's last dole timestamp'''
    user_dole = await function.execute(user_id)

    return user_dole

@router.get('/get_balances', response_model=ManyBalanceSchema)
async def get_top_n_balances(num_balances:int = 0, function:GetTopNBalances = Depends(GetTopNBalances)):
    '''Get a list of N user bank balances, in descending order. Ignores users with no balance. Set to 0 to get all'''
    user_banks = await function.execute(num_balances)

    return user_banks

@router.post('/deposit', response_model=SingleBalanceSchema, responses={404: {'model':HTTPError}})
async def deposit_by_uid(data: SingleBalanceRequestSchema, function: DepositAmountByUID = Depends(DepositAmountByUID)) -> SingleBalanceSchema:
    '''Deposit an amount to a single user's bank balance by Discord unique ID'''
    user_bank = await function.execute(data.uid, data.amount)
    return user_bank

@router.post('/withdraw', response_model=SingleBalanceSchema, responses={404: {'model':HTTPError}})
async def withdraw_by_uid(data: SingleBalanceRequestSchema, function: WithdrawAmountByUID = Depends(WithdrawAmountByUID)) -> SingleBalanceSchema:
    '''Withdraw an amount from a single user's bank balance by Discord unique ID'''
    user_bank = await function.execute(data.uid, data.amount)
    return user_bank

@router.post('/transfer', response_model=TransferBalancesSchema, responses={404: {'model':HTTPError}})
async def transfer_by_uids(data: TransferAmountRequestSchema, function: TransferAmountByUIDs = Depends(TransferAmountByUIDs)) -> TransferBalancesSchema:
    '''Transfer an amount from one user's balance to anothers by Discord unique IDs'''
    transfer_result = await function.execute(data.from_uid, data.to_uid, data.amount)
    return transfer_result
