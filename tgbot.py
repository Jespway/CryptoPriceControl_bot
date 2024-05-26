import asyncio
import logging
import time
from datetime import datetime

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
import requests

import config

import http.client
import json

dp = Dispatcher()

# Функция для получения данных о криптовалюте из Coinmarketcap API
def get_crypto_data(symbol):
    url = f'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol={symbol}&convert=USD'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.CMC_TOKEN,
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Проверить курс"),
            #types.KeyboardButton(text="Отследить транзакцию"),
            #types.KeyboardButton(text="Аирдроп")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите"
    )
    await message.answer("Выберите вариант", reply_markup=keyboard)

@dp.message(F.text.lower() == "проверить курс")
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="BTC/USD",
        callback_data="BTCcourse_check")
    )
    builder.add(types.InlineKeyboardButton(
        text="ETH/USD",
        callback_data="ETHcourse_check")
    )
    builder.add(types.InlineKeyboardButton(
        text="TRX/USD",
        callback_data="TRXcourse_check")
    )
    builder.add(types.InlineKeyboardButton(
        text="TON/USD",
        callback_data="TONcourse_check")
    )
    await message.answer(
        "Выберите интересующую криптовалюту, чтобы узнать актуальный курс",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "BTCcourse_check")
async def send_crypto_data(callback: types.CallbackQuery):
    crypto_data = get_crypto_data("BTC")
    btc_data = crypto_data['data']['BTC'][0]
    price_usd = btc_data['quote']['USD']['price']
    market_cap = btc_data['quote']['USD']['market_cap']
    volume_24h = btc_data['quote']['USD']['volume_24h']
    percent_change_1h = btc_data['quote']['USD']['percent_change_1h']
    percent_change_24h = btc_data['quote']['USD']['percent_change_24h']
    percent_change_7d = btc_data['quote']['USD']['percent_change_7d']

    response_message = f"BTC/USD: {price_usd}\n" \
                       f"Market Cap: {market_cap}\n" \
                       f"Volume (24h): {volume_24h}\n" \
                       f"Change (1h): {percent_change_1h}%\n" \
                       f"Change (24h): {percent_change_24h}%\n" \
                       f"Change (7d): {percent_change_7d}%"

    await callback.message.answer(response_message)
    await callback.answer(
        text="Спасибо, что воспользовались ботом!"
    )


@dp.callback_query(F.data == "ETHcourse_check")
async def send_eth_data(callback: types.CallbackQuery):
    crypto_data = get_crypto_data("ETH")
    eth_data = crypto_data['data']['ETH'][0]
    price_usd = eth_data['quote']['USD']['price']
    market_cap = eth_data['quote']['USD']['market_cap']
    volume_24h = eth_data['quote']['USD']['volume_24h']
    percent_change_1h = eth_data['quote']['USD']['percent_change_1h']
    percent_change_24h = eth_data['quote']['USD']['percent_change_24h']
    percent_change_7d = eth_data['quote']['USD']['percent_change_7d']

    response_message = f"ETH/USD: {price_usd}\n" \
                       f"Market Cap: {market_cap}\n" \
                       f"Volume (24h): {volume_24h}\n" \
                       f"Change (1h): {percent_change_1h}%\n" \
                       f"Change (24h): {percent_change_24h}%\n" \
                       f"Change (7d): {percent_change_7d}%"

    await callback.message.answer(response_message)
    await callback.answer(
        text="Спасибо, что воспользовались ботом!"
    )

@dp.callback_query(F.data == "TRXcourse_check")
async def send_eth_data(callback: types.CallbackQuery):
    crypto_data = get_crypto_data("TRX")
    trx_data = crypto_data['data']['TRX'][0]
    price_usd = trx_data['quote']['USD']['price']
    market_cap = trx_data['quote']['USD']['market_cap']
    volume_24h = trx_data['quote']['USD']['volume_24h']
    percent_change_1h = trx_data['quote']['USD']['percent_change_1h']
    percent_change_24h = trx_data['quote']['USD']['percent_change_24h']
    percent_change_7d = trx_data['quote']['USD']['percent_change_7d']

    response_message = f"TRX/USD: {price_usd}\n" \
                       f"Market Cap: {market_cap}\n" \
                       f"Volume (24h): {volume_24h}\n" \
                       f"Change (1h): {percent_change_1h}%\n" \
                       f"Change (24h): {percent_change_24h}%\n" \
                       f"Change (7d): {percent_change_7d}%"

    await callback.message.answer(response_message)
    await callback.answer(
        text="Спасибо, что воспользовались ботом!"
    )

@dp.callback_query(F.data == "TONcourse_check")
async def send_eth_data(callback: types.CallbackQuery):
    crypto_data = get_crypto_data("TON")
    ton_data = crypto_data['data']['TON'][0]
    price_usd = ton_data['quote']['USD']['price']
    market_cap = ton_data['quote']['USD']['market_cap']
    volume_24h = ton_data['quote']['USD']['volume_24h']
    percent_change_1h = ton_data['quote']['USD']['percent_change_1h']
    percent_change_24h = ton_data['quote']['USD']['percent_change_24h']
    percent_change_7d = ton_data['quote']['USD']['percent_change_7d']

    response_message = f"TON/USD: {price_usd}\n" \
                       f"Market Cap: {market_cap}\n" \
                       f"Volume (24h): {volume_24h}\n" \
                       f"Change (1h): {percent_change_1h}%\n" \
                       f"Change (24h): {percent_change_24h}%\n" \
                       f"Change (7d): {percent_change_7d}%"

    await callback.message.answer(response_message)
    await callback.answer(
        text="Спасибо, что воспользовались ботом!"
    )
"""
async def get_wallet_transactions(wallet_address):
    conn = http.client.HTTPSConnection("rest.cryptoapis.io")
    querystring = f"context=yourExampleString&limit=10&offset=0&fromTimestamp=0&toTimestamp={int(time.time())}"
    headers = {
        'Content-Type': "application/json",
        'X-API-Key': config.CryptoAPI_TOKEN  # Замените на ваш API ключ
    }

    conn.request("GET", f"/blockchain-data/ethereum/sepolia/addresses/{wallet_address}/tokens-transfers-by-time-range?{querystring}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

@dp.message(F.text.lower() == "отследить транзакцию")
async def track_transaction(message: types.Message):
    await message.answer("Пожалуйста, введите адрес кошелька в блокчейн сети:")


@dp.message()
async def handle_wallet_address(message: types.Message):
    wallet_address = message.text.strip()
    try:
        # Получаем информацию о транзакциях по адресу кошелька
        transactions_data = await get_wallet_transactions(wallet_address)

        # Обработка полученных данных
        if 'data' in transactions_data and 'items' in transactions_data['data']:
            transactions = transactions_data['data']['items']
            if transactions:
                response_message = "Последние 10 транзакций по адресу кошелька:\n"
                for transaction in transactions:
                    response_message += f"Транзакция: {transaction['transactionHash']}\n" \
                                        f"Количество: {transaction['tokensAmount']} {transaction['tokenSymbol']}\n" \
                                        f"Дата: {datetime.fromtimestamp(transaction['transactionTimestamp'])}\n\n"
                await message.answer(response_message)
            else:
                await message.answer("По указанному адресу кошелька не найдено транзакций.")
        else:
            await message.answer("Ошибка при получении информации о транзакциях.")
    except Exception as e:
        await message.answer("Произошла ошибка при обработке запроса.")
        logging.exception(f"Error while handling wallet address: {e}")

def get_top_exchanges():
    url = 'https://pro-api.coinmarketcap.com/v1/exchange/map'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.CMC_TOKEN,  # Замените 'your-api-key' на ваш реальный ключ API
    }
    parameters = {
        'start': '1',
        'limit': '10',  # Получаем топ 10 бирж
    }

    try:
        response = requests.get(url, headers=headers)#, params=parameters)
        response.raise_for_status()  # Проверяем наличие ошибок в ответе
        data = response.json()
        return data['data']
    except requests.exceptions.RequestException as e:
        print('Failed to fetch top exchanges data:', e)
        return None

@dp.message(F.text.lower() == "аирдроп")
async def top_exchanges(message: types.Message):
    exchanges_data = get_top_exchanges()
    if exchanges_data:
        # Отправляем информацию о топ 10 бирж пользователю
        await message.answer(format_exchanges_data(exchanges_data))
    else:
        await message.answer("Failed to fetch top exchanges data. Please try again later.")

def format_exchanges_data(exchanges_data):
    formatted_data = ''
    for exchange in exchanges_data:
        formatted_data += f"Name: {exchange['name']}\n"
        formatted_data += f"Description: {exchange['description']}\n"
        formatted_data += f"Website: {exchange['urls']['website'][0]}\n\n"
    return formatted_data
"""
@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "I'm and echo bot.\nSend me any message!"
    await message.answer(text=text)

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
