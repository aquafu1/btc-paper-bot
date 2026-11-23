# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 7:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1198 windows, 33102 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 646 | 34.7 | 35.3 | $-408.79 | -6.3% | $591.21 | -1.2 | done | can't tell from luck |
| value_ev10 | 1579 | 38.6 | 39.2 | $-833.32 | -5.3% | $166.68 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3317 | 50.8 | 50.3 | $-1098.58 | -3.3% | $-98.58 | -1.9 | done | can't tell from luck |
| value_ev5 | 2390 | 40.4 | 41.1 | $-1272.12 | -5.3% | $-272.12 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2773 | 49.5 | 49.4 | $-1279.44 | -4.6% | $-279.44 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2773 | 50.5 | 51.1 | $-1657.53 | -6.0% | $-657.53 | -3.2 | done | losing for real |
| trend_filter | 1952 | 48.7 | 50.5 | $-1684.02 | -8.6% | $-684.02 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3317 | 49.2 | 50.3 | $-2049.75 | -6.2% | $-1049.75 | -3.6 | done | losing for real |
| coinflip | 4785 | 50.1 | 50.1 | $-2138.76 | -4.5% | $-1138.76 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4785 | 50.2 | 51.4 | $-2998.61 | -6.3% | $-1998.61 | -4.5 | done | losing for real |
| always_up | 4785 | 47.9 | 49.3 | $-3503.03 | -7.3% | $-2503.03 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7603 | 48.1 | 48.9 | $-4275.06 |
| ETH | 8207 | 48.0 | 48.4 | $-5049.74 |
| SOL | 8620 | 48.2 | 48.4 | $-4431.93 |
| XRP | 8672 | 48.1 | 48.2 | $-5167.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
