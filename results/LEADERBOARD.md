# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 6:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 856 windows, 23619 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 443 | 34.3 | 34.8 | $-255.60 | -5.8% | $744.40 | -0.9 | done | can't tell from luck |
| value_ev10 | 1081 | 37.7 | 39.0 | $-733.94 | -6.8% | $266.06 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2001 | 50.2 | 49.7 | $-788.01 | -3.9% | $211.99 | -1.8 | done | can't tell from luck |
| trend_filter | 1391 | 50.2 | 50.9 | $-883.02 | -6.3% | $116.98 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2411 | 50.6 | 50.5 | $-963.46 | -4.0% | $36.54 | -2.0 | done | can't tell from luck |
| value_ev5 | 1632 | 39.8 | 41.0 | $-1032.94 | -6.3% | $-32.94 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2411 | 49.4 | 50.3 | $-1399.69 | -5.8% | $-399.69 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2001 | 49.8 | 51.0 | $-1476.83 | -7.4% | $-476.83 | -3.4 | done | losing for real |
| coinflip | 3416 | 50.2 | 50.3 | $-1486.96 | -4.4% | $-486.96 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3416 | 51.3 | 51.7 | $-1543.02 | -4.5% | $-543.02 | -2.7 | done | losing for real |
| always_up | 3416 | 47.0 | 49.5 | $-3258.92 | -9.5% | $-2258.92 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5385 | 48.3 | 49.0 | $-2938.04 |
| ETH | 5881 | 48.1 | 48.5 | $-3848.68 |
| SOL | 6160 | 48.3 | 48.5 | $-3550.42 |
| XRP | 6193 | 48.3 | 48.5 | $-3485.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
