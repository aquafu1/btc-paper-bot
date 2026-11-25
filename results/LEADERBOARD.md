# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 10:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1402 windows, 36142 settled trades, 379 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 726 | 34.8 | 35.3 | $-452.49 | -6.2% | $547.51 | -1.3 | done | can't tell from luck |
| value_ev10 | 1753 | 39.0 | 39.2 | $-724.58 | -4.1% | $275.42 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 3612 | 50.8 | 50.1 | $-1045.93 | -2.9% | $-45.93 | -1.7 | done | can't tell from luck |
| value_ev5 | 2642 | 40.7 | 41.1 | $-1193.44 | -4.5% | $-193.44 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 3031 | 49.3 | 49.3 | $-1428.07 | -4.7% | $-428.07 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 3031 | 50.7 | 51.0 | $-1592.10 | -5.3% | $-592.10 | -3.0 | done | losing for real |
| trend_filter | 2147 | 48.5 | 50.4 | $-1885.87 | -8.8% | $-885.87 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3612 | 49.2 | 50.2 | $-2185.73 | -6.1% | $-1185.73 | -3.7 | done | losing for real |
| coinflip | 5196 | 50.0 | 50.0 | $-2244.82 | -4.3% | $-1244.82 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5196 | 50.1 | 51.3 | $-3246.45 | -6.2% | $-2246.45 | -4.6 | done | losing for real |
| always_up | 5196 | 47.9 | 49.3 | $-3641.75 | -7.0% | $-2641.75 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9071 | 48.1 | 48.8 | $-4820.69 |
| ETH | 9761 | 48.1 | 48.0 | $-5236.32 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
