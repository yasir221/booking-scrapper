from booking.booking import Booking

# Starting Block
with Booking() as bot:
  bot.land_first_page()
  # bot.change_currency(currenccy='USD')
  bot.select_place_to_go('New York')