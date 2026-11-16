# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 11:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 494 windows, 13579 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1154 | 51.2 | 49.9 | $-185.41 | -1.6% | $814.59 | -0.5 | done | can't tell from luck |
| value_ev20 | 251 | 34.3 | 35.8 | $-189.21 | -7.5% | $810.79 | -0.9 | done | can't tell from luck |
| value_ev10 | 639 | 38.3 | 40.0 | $-470.56 | -7.4% | $529.44 | -1.5 | done | can't tell from luck |
| trend_filter | 797 | 49.9 | 50.8 | $-494.70 | -6.2% | $505.30 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1368 | 49.9 | 49.9 | $-508.77 | -3.7% | $491.23 | -1.4 | done | can't tell from luck |
| value_ev5 | 944 | 40.6 | 41.7 | $-586.78 | -6.2% | $413.22 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1368 | 50.1 | 51.5 | $-941.24 | -6.9% | $58.76 | -2.6 | done | losing for real |
| coinflip | 1968 | 49.9 | 50.8 | $-1044.50 | -5.3% | $-44.50 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1154 | 48.8 | 51.4 | $-1079.80 | -9.4% | $-79.80 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 1968 | 49.9 | 51.7 | $-1377.25 | -7.0% | $-377.25 | -3.2 | done | losing for real |
| always_up | 1968 | 46.2 | 50.3 | $-2343.00 | -11.9% | $-1343.00 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3060 | 47.4 | 49.3 | $-2478.51 |
| ETH | 3402 | 48.1 | 48.8 | $-2208.00 |
| SOL | 3543 | 47.8 | 49.2 | $-2577.37 |
| XRP | 3574 | 48.5 | 48.9 | $-1957.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
