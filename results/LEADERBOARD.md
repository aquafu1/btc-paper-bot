# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 8:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1155 windows, 31907 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 614 | 34.5 | 35.2 | $-397.85 | -6.5% | $602.15 | -1.2 | done | can't tell from luck |
| value_ev10 | 1504 | 38.3 | 39.2 | $-871.63 | -5.8% | $128.37 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3202 | 50.8 | 50.4 | $-1041.17 | -3.3% | $-41.17 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2691 | 49.8 | 49.5 | $-1142.34 | -4.2% | $-142.34 | -2.2 | done | losing for real |
| value_ev5 | 2275 | 40.2 | 41.1 | $-1260.59 | -5.5% | $-260.59 | -2.2 | done | losing for real |
| trend_filter | 1889 | 49.0 | 50.5 | $-1513.44 | -8.0% | $-513.44 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2691 | 50.2 | 51.0 | $-1720.43 | -6.4% | $-720.43 | -3.4 | done | losing for real |
| coinflip | 4613 | 50.2 | 50.2 | $-1920.12 | -4.2% | $-920.12 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3202 | 49.2 | 50.2 | $-1946.29 | -6.1% | $-946.29 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4613 | 50.1 | 51.4 | $-2959.33 | -6.4% | $-1959.33 | -4.5 | done | losing for real |
| always_up | 4613 | 47.7 | 49.3 | $-3527.02 | -7.6% | $-2527.02 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7316 | 48.2 | 49.0 | $-3875.91 |
| ETH | 7905 | 48.1 | 48.4 | $-4676.37 |
| SOL | 8302 | 48.0 | 48.4 | $-4675.98 |
| XRP | 8384 | 48.1 | 48.2 | $-5071.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
