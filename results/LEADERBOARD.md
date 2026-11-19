# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 12:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 787 windows, 21680 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1836 | 50.1 | 49.6 | $-704.68 | -3.8% | $295.32 | -1.6 | done | can't tell from luck |
| trend_filter | 1275 | 50.4 | 50.8 | $-728.93 | -5.7% | $271.07 | -2.1 | done | losing for real |
| value_ev10 | 986 | 37.3 | 39.1 | $-792.30 | -8.0% | $207.70 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2215 | 50.9 | 50.6 | $-793.18 | -3.6% | $206.82 | -1.7 | done | can't tell from luck |
| value_ev5 | 1493 | 39.7 | 41.1 | $-1020.62 | -6.8% | $-20.62 | -2.2 | done | losing for real |
| coinflip | 3140 | 50.3 | 50.3 | $-1329.43 | -4.2% | $-329.43 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1836 | 49.9 | 51.2 | $-1332.25 | -7.3% | $-332.25 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2215 | 49.1 | 50.2 | $-1391.33 | -6.3% | $-391.33 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3140 | 51.3 | 51.7 | $-1423.58 | -4.5% | $-423.58 | -2.6 | done | losing for real |
| always_up | 3140 | 47.5 | 49.6 | $-2664.63 | -8.5% | $-1664.63 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4925 | 48.3 | 49.1 | $-2904.04 |
| ETH | 5407 | 48.1 | 48.5 | $-3579.00 |
| SOL | 5646 | 48.3 | 48.6 | $-3190.04 |
| XRP | 5702 | 48.5 | 48.5 | $-2899.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
