# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 12:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1360 windows, 35534 settled trades, 394 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 702 | 34.0 | 35.4 | $-581.96 | -8.3% | $418.04 | -1.7 | done | can't tell from luck |
| value_ev10 | 1719 | 38.6 | 39.2 | $-858.63 | -5.0% | $141.37 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3550 | 50.9 | 50.1 | $-973.24 | -2.7% | $26.76 | -1.6 | done | can't tell from luck |
| value_ev5 | 2594 | 40.4 | 41.1 | $-1360.62 | -5.2% | $-360.62 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2984 | 49.3 | 49.4 | $-1462.31 | -4.9% | $-462.31 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2984 | 50.7 | 50.9 | $-1549.88 | -5.2% | $-549.88 | -2.9 | done | losing for real |
| trend_filter | 2115 | 48.6 | 50.4 | $-1850.35 | -8.7% | $-850.35 | -4.1 | done | losing for real |
| coinflip | 5112 | 50.0 | 50.0 | $-2241.31 | -4.4% | $-1241.31 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3550 | 49.1 | 50.3 | $-2272.93 | -6.4% | $-1272.93 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5112 | 50.2 | 51.3 | $-3136.14 | -6.1% | $-2136.14 | -4.5 | done | losing for real |
| always_up | 5112 | 47.8 | 49.3 | $-3789.63 | -7.4% | $-2789.63 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8772 | 47.8 | 48.8 | $-5351.58 |
| ETH | 9452 | 48.1 | 48.1 | $-5141.19 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
