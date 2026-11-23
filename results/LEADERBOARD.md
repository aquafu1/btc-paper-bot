# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 3:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1230 windows, 33612 settled trades, 429 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 658 | 34.3 | 35.3 | $-477.83 | -7.3% | $522.17 | -1.4 | done | can't tell from luck |
| value_ev10 | 1608 | 38.7 | 39.2 | $-801.38 | -5.0% | $198.62 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3370 | 50.8 | 50.3 | $-1082.97 | -3.2% | $-82.97 | -1.9 | done | can't tell from luck |
| value_ev5 | 2429 | 40.5 | 41.1 | $-1228.17 | -5.1% | $-228.17 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2820 | 49.5 | 49.4 | $-1284.73 | -4.6% | $-284.73 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2820 | 50.5 | 51.1 | $-1670.57 | -5.9% | $-670.57 | -3.2 | done | losing for real |
| trend_filter | 1987 | 48.7 | 50.4 | $-1685.10 | -8.5% | $-685.10 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3370 | 49.2 | 50.2 | $-2089.82 | -6.2% | $-1089.82 | -3.6 | done | losing for real |
| coinflip | 4850 | 50.0 | 50.1 | $-2234.52 | -4.6% | $-1234.52 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4850 | 50.2 | 51.4 | $-2949.22 | -6.1% | $-1949.22 | -4.4 | done | losing for real |
| always_up | 4850 | 47.9 | 49.3 | $-3559.04 | -7.3% | $-2559.04 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7839 | 48.0 | 48.9 | $-4529.08 |
| ETH | 8463 | 48.1 | 48.3 | $-4950.05 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
