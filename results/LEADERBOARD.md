# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 11:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1407 windows, 36200 settled trades, 419 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 726 | 34.8 | 35.3 | $-452.49 | -6.2% | $547.51 | -1.3 | done | can't tell from luck |
| value_ev10 | 1754 | 39.0 | 39.2 | $-707.69 | -4.0% | $292.31 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 3619 | 50.8 | 50.1 | $-1029.81 | -2.8% | $-29.81 | -1.7 | done | can't tell from luck |
| value_ev5 | 2645 | 40.7 | 41.1 | $-1172.88 | -4.4% | $-172.88 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 3037 | 49.3 | 49.3 | $-1467.78 | -4.8% | $-467.78 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 3037 | 50.7 | 51.0 | $-1547.20 | -5.1% | $-547.20 | -2.9 | done | losing for real |
| trend_filter | 2151 | 48.5 | 50.4 | $-1905.58 | -8.9% | $-905.58 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3619 | 49.2 | 50.2 | $-2196.16 | -6.1% | $-1196.16 | -3.7 | done | losing for real |
| coinflip | 5204 | 50.0 | 50.0 | $-2236.50 | -4.3% | $-1236.50 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5204 | 50.1 | 51.3 | $-3249.41 | -6.2% | $-2249.41 | -4.6 | done | losing for real |
| always_up | 5204 | 47.9 | 49.3 | $-3645.39 | -7.0% | $-2645.39 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9100 | 48.1 | 48.8 | $-4767.18 |
| ETH | 9790 | 48.0 | 48.0 | $-5259.48 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
