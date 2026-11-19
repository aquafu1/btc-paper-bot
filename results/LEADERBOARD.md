# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 11:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 830 windows, 22824 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 422 | 33.2 | 34.9 | $-390.80 | -9.3% | $609.20 | -1.4 | done | can't tell from luck |
| value_ev10 | 1043 | 37.4 | 39.1 | $-833.78 | -8.0% | $166.22 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2328 | 51.0 | 50.6 | $-835.68 | -3.6% | $164.32 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1918 | 49.9 | 49.6 | $-866.86 | -4.5% | $133.14 | -2.0 | done | can't tell from luck |
| trend_filter | 1346 | 49.8 | 50.8 | $-957.95 | -7.1% | $42.05 | -2.7 | done | losing for real |
| value_ev5 | 1579 | 39.8 | 41.1 | $-1077.89 | -6.8% | $-77.89 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1918 | 50.1 | 51.1 | $-1345.09 | -7.0% | $-345.09 | -3.2 | done | losing for real |
| coinflip | 3314 | 50.3 | 50.3 | $-1435.51 | -4.3% | $-435.51 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2328 | 49.0 | 50.3 | $-1482.17 | -6.4% | $-482.17 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3314 | 51.2 | 51.6 | $-1541.14 | -4.7% | $-541.14 | -2.8 | done | losing for real |
| always_up | 3314 | 47.3 | 49.6 | $-2975.80 | -9.0% | $-1975.80 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5190 | 48.2 | 49.1 | $-3241.20 |
| ETH | 5677 | 48.1 | 48.5 | $-3833.11 |
| SOL | 5950 | 48.3 | 48.6 | $-3410.20 |
| XRP | 6007 | 48.4 | 48.5 | $-3258.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
