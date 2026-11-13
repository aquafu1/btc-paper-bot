# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 12:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 257 windows, 6737 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 669 | 55.5 | 52.4 | $+115.27 | +1.7% | $1115.27 | +0.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 538 | 53.5 | 52.1 | $-76.25 | -1.4% | $923.75 | -0.3 | done | can't tell from luck |
| value_ev20 | 119 | 33.6 | 36.7 | $-141.51 | -11.9% | $858.49 | -1.0 | Sun 11:00 AM | too few trades (119/200) |
| value_ev10 | 318 | 36.5 | 40.8 | $-444.49 | -14.0% | $555.51 | -2.1 | done | losing for real |
| trend_filter | 355 | 45.9 | 50.4 | $-475.04 | -13.4% | $524.96 | -2.6 | done | losing for real |
| value_ev5 | 471 | 39.3 | 42.5 | $-551.94 | -11.7% | $448.06 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 538 | 46.5 | 49.9 | $-638.95 | -11.9% | $361.05 | -2.8 | done | losing for real |
| coinflip | 1020 | 49.4 | 50.9 | $-760.64 | -7.5% | $239.36 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1020 | 49.8 | 51.5 | $-785.81 | -7.7% | $214.19 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 669 | 44.5 | 49.7 | $-975.56 | -14.6% | $24.44 | -3.9 | done | losing for real |
| always_up | 1020 | 47.2 | 50.3 | $-1094.34 | -10.7% | $-94.34 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1504 | 46.5 | 49.7 | $-1564.76 |
| ETH | 1677 | 46.7 | 49.1 | $-1750.46 |
| SOL | 1746 | 48.1 | 49.4 | $-1504.37 |
| XRP | 1810 | 48.7 | 49.1 | $-1009.66 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
