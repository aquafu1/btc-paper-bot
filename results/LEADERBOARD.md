# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 5:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1046 windows, 29029 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 543 | 34.4 | 35.1 | $-325.47 | -6.0% | $674.53 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2944 | 51.2 | 50.5 | $-797.53 | -2.7% | $202.47 | -1.5 | done | can't tell from luck |
| value_ev10 | 1344 | 37.4 | 39.2 | $-1046.04 | -7.8% | $-46.04 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2479 | 49.7 | 49.6 | $-1176.03 | -4.7% | $-176.03 | -2.4 | done | losing for real |
| trend_filter | 1735 | 49.2 | 50.7 | $-1373.79 | -7.9% | $-373.79 | -3.4 | done | losing for real |
| value_ev5 | 2033 | 39.4 | 41.0 | $-1471.77 | -7.2% | $-471.77 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2479 | 50.3 | 51.0 | $-1565.77 | -6.3% | $-565.77 | -3.2 | done | losing for real |
| coinflip | 4176 | 50.5 | 50.3 | $-1668.53 | -4.0% | $-668.53 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2944 | 48.8 | 50.3 | $-2052.04 | -7.0% | $-1052.04 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4176 | 50.7 | 51.5 | $-2274.99 | -5.4% | $-1274.99 | -3.6 | done | losing for real |
| always_up | 4176 | 47.3 | 49.4 | $-3638.01 | -8.7% | $-2638.01 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6618 | 48.3 | 49.0 | $-3560.11 |
| ETH | 7192 | 48.1 | 48.5 | $-4532.27 |
| SOL | 7581 | 48.1 | 48.5 | $-4532.39 |
| XRP | 7638 | 48.1 | 48.3 | $-4765.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
