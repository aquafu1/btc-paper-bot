# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 11:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 254 windows, 6660 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 659 | 55.7 | 52.3 | $+157.72 | +2.4% | $1157.72 | +0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 531 | 53.5 | 52.0 | $-63.79 | -1.2% | $936.21 | -0.3 | done | can't tell from luck |
| value_ev20 | 119 | 33.6 | 36.7 | $-141.51 | -11.9% | $858.49 | -1.0 | Sun 9:45 AM | too few trades (119/200) |
| value_ev10 | 318 | 36.5 | 40.8 | $-444.49 | -14.0% | $555.51 | -2.1 | done | losing for real |
| trend_filter | 349 | 46.1 | 50.7 | $-450.99 | -12.9% | $549.01 | -2.5 | done | losing for real |
| value_ev5 | 470 | 39.1 | 42.4 | $-556.12 | -11.8% | $443.88 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 531 | 46.5 | 50.1 | $-623.84 | -11.7% | $376.16 | -2.8 | done | losing for real |
| coinflip | 1008 | 49.5 | 50.9 | $-725.81 | -7.2% | $274.19 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1008 | 49.9 | 51.6 | $-759.87 | -7.5% | $240.13 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 659 | 44.3 | 49.8 | $-989.01 | -15.0% | $10.99 | -3.9 | done | losing for real |
| always_up | 1008 | 47.0 | 50.4 | $-1107.47 | -11.0% | $-107.47 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1490 | 46.6 | 49.7 | $-1513.07 |
| ETH | 1659 | 46.7 | 49.1 | $-1728.86 |
| SOL | 1724 | 48.0 | 49.4 | $-1480.84 |
| XRP | 1787 | 48.7 | 49.1 | $-982.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
