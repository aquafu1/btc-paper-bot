# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 12:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 256 windows, 6721 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 667 | 55.3 | 52.3 | $+105.88 | +1.6% | $1105.88 | +0.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 536 | 53.4 | 52.0 | $-85.63 | -1.6% | $914.37 | -0.4 | done | can't tell from luck |
| value_ev20 | 119 | 33.6 | 36.7 | $-141.51 | -11.9% | $858.49 | -1.0 | Sun 11:00 AM | too few trades (119/200) |
| value_ev10 | 318 | 36.5 | 40.8 | $-444.49 | -14.0% | $555.51 | -2.1 | done | losing for real |
| trend_filter | 353 | 46.2 | 50.5 | $-455.04 | -12.9% | $544.96 | -2.5 | done | losing for real |
| value_ev5 | 471 | 39.3 | 42.5 | $-551.94 | -11.7% | $448.06 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 536 | 46.6 | 50.0 | $-618.95 | -11.5% | $381.05 | -2.8 | done | losing for real |
| coinflip | 1018 | 49.4 | 50.9 | $-755.01 | -7.4% | $244.99 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1018 | 49.9 | 51.6 | $-765.81 | -7.5% | $234.19 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 667 | 44.7 | 49.8 | $-955.56 | -14.3% | $44.44 | -3.8 | done | losing for real |
| always_up | 1018 | 47.2 | 50.3 | $-1074.34 | -10.6% | $-74.34 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1496 | 46.7 | 49.7 | $-1514.77 |
| ETH | 1669 | 46.7 | 49.2 | $-1713.59 |
| SOL | 1746 | 48.1 | 49.4 | $-1504.37 |
| XRP | 1810 | 48.7 | 49.1 | $-1009.66 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
