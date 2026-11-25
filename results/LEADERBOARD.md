# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 9:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1396 windows, 36038 settled trades, 392 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 724 | 34.7 | 35.4 | $-493.87 | -6.8% | $506.13 | -1.4 | done | can't tell from luck |
| value_ev10 | 1749 | 38.9 | 39.2 | $-768.67 | -4.4% | $231.33 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3599 | 50.8 | 50.1 | $-1035.82 | -2.9% | $-35.82 | -1.7 | done | can't tell from luck |
| value_ev5 | 2636 | 40.6 | 41.1 | $-1240.13 | -4.7% | $-240.13 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 3022 | 49.3 | 49.3 | $-1442.42 | -4.8% | $-442.42 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 3022 | 50.7 | 50.9 | $-1596.79 | -5.3% | $-596.79 | -3.0 | done | losing for real |
| trend_filter | 2141 | 48.6 | 50.4 | $-1851.37 | -8.6% | $-851.37 | -4.1 | done | losing for real |
| coinflip | 5182 | 50.0 | 50.0 | $-2223.31 | -4.3% | $-1223.31 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3599 | 49.2 | 50.2 | $-2224.52 | -6.2% | $-1224.52 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5182 | 50.2 | 51.3 | $-3187.62 | -6.2% | $-2187.62 | -4.6 | done | losing for real |
| always_up | 5182 | 47.9 | 49.3 | $-3706.76 | -7.2% | $-2706.76 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9020 | 48.1 | 48.8 | $-4929.01 |
| ETH | 9708 | 48.1 | 48.0 | $-5258.04 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
